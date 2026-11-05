
package com.example.sre;

import java.time.LocalDateTime;
import java.util.*;
import java.util.regex.Matcher;
import java.util.regex.Pattern;
import java.util.stream.Collectors;

public final class LogAnalyzer {
    private static final Pattern LOG_PATTERN = Pattern.compile(
        "^(?<timestamp>\\d{4}-\\d{2}-\\d{2}[ T]\\d{2}:\\d{2}:\\d{2})\\s+" +
        "(?<level>TRACE|DEBUG|INFO|WARN|WARNING|ERROR|FATAL|CRITICAL|EXCEPTION)\\s+" +
        "(?<service>[\\w.-]+)\\s+(?<message>.*)$",
        Pattern.CASE_INSENSITIVE
    );

    private static final Map<String, String> SEVERITY = Map.of(
        "FATAL", "CRITICAL", "CRITICAL", "CRITICAL",
        "EXCEPTION", "HIGH", "ERROR", "HIGH",
        "WARN", "MEDIUM", "WARNING", "MEDIUM"
    );

    private LogAnalyzer() {}

    private static String normalize(String message) {
        return message.toLowerCase(Locale.ROOT)
                .replaceAll("\\b\\d+(?:\\.\\d+)?\\b", "<N>")
                .replaceAll("\\s+", " ")
                .trim();
    }

    private static String recommendation(String message, String severity) {
        String m = message.toLowerCase(Locale.ROOT);
        if (m.contains("outofmemory") || m.contains("heap space"))
            return "Inspect heap and GC logs; capture a heap dump; check for leaks and memory sizing.";
        if (m.contains("timeout") || m.contains("connection"))
            return "Check dependency health, network path, connection-pool saturation and timeout/retry settings.";
        if (m.contains("503") || m.contains("unavailable"))
            return "Verify dependency availability, service endpoints, capacity and recent deployments.";
        if (m.contains("nullpointer"))
            return "Inspect the referenced stack frame; validate inputs and add regression tests.";
        return "Review correlated logs and recent changes; triage as " + severity + " before action.";
    }

    public List<Incident> analyze(List<String> lines) {
        Map<String, List<Map<String, String>>> groups = new LinkedHashMap<>();

        for (String line : lines) {
            Matcher matcher = LOG_PATTERN.matcher(line.trim());
            if (!matcher.matches()) continue;

            Map<String, String> event = new HashMap<>();
            for (String key : List.of("timestamp", "level", "service", "message"))
                event.put(key, matcher.group(key));
            event.put("level", event.get("level").toUpperCase(Locale.ROOT));

            if (!SEVERITY.containsKey(event.get("level"))) continue;
            try {
                LocalDateTime.parse(event.get("timestamp").replace(' ', 'T'));
            } catch (Exception invalidTimestamp) {
                continue;
            }

            groups.computeIfAbsent(normalize(event.get("message")), ignored -> new ArrayList<>())
                  .add(event);
        }

        List<Incident> incidents = new ArrayList<>();
        for (var entry : groups.entrySet()) {
            List<Map<String, String>> events = entry.getValue();
            events.sort(Comparator.comparing(e -> e.get("timestamp")));

            String severity = events.stream()
                    .map(e -> SEVERITY.get(e.get("level")))
                    .max(Comparator.comparingInt(LogAnalyzer::severityRank))
                    .orElse("MEDIUM");

            List<String> services = events.stream().map(e -> e.get("service"))
                    .distinct().sorted().collect(Collectors.toList());
            String example = events.get(0).get("message");

            incidents.add(new Incident(
                    entry.getKey(), severity, events.size(),
                    events.get(0).get("timestamp"),
                    events.get(events.size() - 1).get("timestamp"),
                    services, example, recommendation(example, severity)
            ));
        }

        incidents.sort(Comparator
                .comparingInt((Incident i) -> severityRank(i.severity()))
                .thenComparing(Comparator.comparingInt(Incident::count).reversed()));
        return incidents;
    }

    private static int severityRank(String severity) {
        return switch (severity) {
            case "CRITICAL" -> 3;
            case "HIGH" -> 2;
            case "MEDIUM" -> 1;
            default -> 0;
        };
    }
}


package com.example.sre;

import java.io.IOException;
import java.nio.file.Files;
import java.nio.file.Path;
import java.util.List;
import java.util.stream.Collectors;

public class Main {
    public static void main(String[] args) throws IOException {
        Path input = args.length > 0 ? Path.of(args[0]) : Path.of("../../sample-data/application.log");
        if (!Files.exists(input)) {
            System.err.println("Log file not found: " + input.toAbsolutePath());
            System.exit(2);
        }

        List<String> lines = Files.readAllLines(input);
        List<Incident> incidents = new LogAnalyzer().analyze(lines);

        System.out.printf("Analyzed %s; found %d incident groups.%n", input, incidents.size());
        for (Incident incident : incidents) {
            System.out.printf("[%s] %dx %s: %s%n",
                    incident.severity(), incident.count(),
                    String.join(", ", incident.services()), incident.exampleMessage());
        }

        Path csv = Path.of("incident-report.csv");
        String header = "severity,count,services,first_seen,last_seen,example_message,recommendation,fingerprint";
        List<String> rows = incidents.stream().map(i -> String.join(",",
                csv(i.severity()), Integer.toString(i.count()),
                csv(String.join("; ", i.services())), csv(i.firstSeen()), csv(i.lastSeen()),
                csv(i.exampleMessage()), csv(i.recommendation()), csv(i.fingerprint())
        )).collect(Collectors.toList());

        Files.write(csv, concat(header, rows));
        System.out.println("CSV report written to " + csv.toAbsolutePath());
    }

    private static String csv(String value) {
        return "\"" + value.replace("\"", "\"\"") + "\"";
    }

    private static List<String> concat(String header, List<String> rows) {
        java.util.ArrayList<String> all = new java.util.ArrayList<>();
        all.add(header);
        all.addAll(rows);
        return all;
    }
}


package com.example.sre;

import java.util.List;

public record Incident(
        String fingerprint,
        String severity,
        int count,
        String firstSeen,
        String lastSeen,
        List<String> services,
        String exampleMessage,
        String recommendation
) {}

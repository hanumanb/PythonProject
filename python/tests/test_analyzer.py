
from log_analyzer.analyzer import analyze_lines, normalize_message, parse_line

def test_parse_error_line():
    parsed = parse_line("2026-11-05 09:03:42 ERROR payment-service Database connection timeout after 3000ms")
    assert parsed is not None
    assert parsed["service"] == "payment-service"
    assert parsed["level"] == "ERROR"

def test_normalize_groups_numbers():
    assert normalize_message("timeout after 3000ms") == normalize_message("timeout after 5000ms")

def test_repeated_errors_are_grouped():
    lines = [
        "2026-11-05 09:03:42 ERROR payment-service Database connection timeout after 3000ms",
        "2026-11-05 09:03:43 ERROR payment-service Database connection timeout after 5000ms",
    ]
    result = analyze_lines(lines)
    assert len(result) == 1
    assert result[0].count == 2
    assert result[0].severity == "HIGH"

def test_fatal_is_critical():
    result = analyze_lines([
        "2026-11-05 09:05:18 FATAL order-service OutOfMemoryError: Java heap space"
    ])
    assert result[0].severity == "CRITICAL"

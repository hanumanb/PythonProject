
"""
Optional LLM integration boundary.

Interview point: call an LLM only after deterministic filtering, grouping and redaction.
Keep this adapter separate so core analysis remains testable and works without credentials.
This starter deliberately contains no network call. Implement against your approved provider
SDK only after confirming endpoint, model, data policy, timeout and retry requirements.
"""

def build_incident_prompt(incident: dict) -> str:
    return (
        "You are an SRE assistant. Analyze the incident data below. "
        "Separate observed facts from hypotheses. Do not claim certainty without evidence. "
        "Suggest safe diagnostic steps; do not execute remediation.\n\n"
        f"Incident:\n{incident}"
    )

def safe_fallback_summary(incident: dict) -> str:
    return (
        f"{incident.get('severity', 'UNKNOWN')} severity incident affecting "
        f"{', '.join(incident.get('services', []))}. "
        f"Observed message: {incident.get('example_message', 'N/A')}. "
        f"Suggested next step: {incident.get('recommendation', 'Investigate correlated telemetry.')}"
    )

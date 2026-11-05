"""Define domain-specific exceptions."""
class ConfigurationError(Exception):
    """Raised when required application configuration is invalid."""

def load_port(value: str) -> int:
    try:
        port = int(value)
    except ValueError as exc:
        raise ConfigurationError("PORT must be an integer") from exc
    if not 1 <= port <= 65535:
        raise ConfigurationError("PORT must be between 1 and 65535")
    return port

if __name__ == "__main__":
    print(load_port("8080"))

"""Classes, encapsulation, and instance methods."""
class Service:
    def __init__(self, name: str, port: int):
        if not 1 <= port <= 65535:
            raise ValueError("Invalid TCP port")
        self.name = name
        self.port = port
        self._healthy = True

    def mark_unhealthy(self):
        self._healthy = False

    def status(self):
        return "healthy" if self._healthy else "unhealthy"

service = Service("payments", 8080)
service.mark_unhealthy()
print(service.name, service.port, service.status())

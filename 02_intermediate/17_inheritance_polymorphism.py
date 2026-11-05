"""Inheritance and polymorphism."""
class Notification:
    def send(self, message: str) -> str:
        raise NotImplementedError

class EmailNotification(Notification):
    def send(self, message: str) -> str:
        return f"EMAIL: {message}"

class SlackNotification(Notification):
    def send(self, message: str) -> str:
        return f"SLACK: {message}"

for channel in (EmailNotification(), SlackNotification()):
    print(channel.send("CPU threshold exceeded"))

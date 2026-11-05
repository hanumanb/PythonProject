"""SQLite persistence using parameterized SQL."""
import sqlite3
from pathlib import Path

DB_PATH = Path("alerts.db")

def main():
    with sqlite3.connect(DB_PATH) as connection:
        connection.execute("""
            CREATE TABLE IF NOT EXISTS alerts (
                id INTEGER PRIMARY KEY,
                service TEXT NOT NULL,
                severity TEXT NOT NULL,
                message TEXT NOT NULL
            )
        """)
        connection.execute(
            "INSERT INTO alerts(service, severity, message) VALUES (?, ?, ?)",
            ("payments", "HIGH", "Database timeout"),
        )
        rows = connection.execute(
            "SELECT service, severity, message FROM alerts WHERE severity = ?",
            ("HIGH",),
        ).fetchall()
        for row in rows:
            print(row)
    DB_PATH.unlink(missing_ok=True)

if __name__ == "__main__":
    main()

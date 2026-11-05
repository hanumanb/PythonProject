"""Async concurrency for I/O-bound work; uses simulated network waits."""
import asyncio

async def check_service(name: str) -> str:
    await asyncio.sleep(0.2)  # stand-in for an async HTTP request
    return f"{name}: healthy"

async def main():
    results = await asyncio.gather(
        check_service("api"),
        check_service("payments"),
        check_service("inventory"),
    )
    print("\\n".join(results))

if __name__ == "__main__":
    asyncio.run(main())

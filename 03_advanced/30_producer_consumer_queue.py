"""Producer/consumer pattern with a thread-safe queue."""
from queue import Queue
from threading import Thread

def worker(queue: Queue):
    while True:
        item = queue.get()
        try:
            if item is None:
                return
            print("Processed:", item)
        finally:
            queue.task_done()

if __name__ == "__main__":
    work = Queue()
    thread = Thread(target=worker, args=(work,), daemon=True)
    thread.start()
    for event in ["deployment-started", "pod-ready", "deployment-complete"]:
        work.put(event)
    work.put(None)
    work.join()
    thread.join()

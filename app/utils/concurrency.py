import threading
import time
import queue
from concurrent.futures import ThreadPoolExecutor


def task(name):
    print(f"{name} started")
    time.sleep(2)
    print(f"{name} completed")


def run_threads():
    thread1 = threading.Thread(target=task, args=("Task 1",))
    thread2 = threading.Thread(target=task, args=("Task 2",))

    thread1.start()
    thread2.start()

    thread1.join()
    thread2.join()

    print("All tasks completed")


def run_thread_pool():
    tasks = ["Task 1", "Task 2", "Task 3", "Task 4"]

    with ThreadPoolExecutor(max_workers=2) as executor:
        executor.map(task, tasks)

    print("All thread pool tasks completed")


counter = 0
lock = threading.Lock()


def increment_counter():
    global counter

    for _ in range(100000):
        with lock:
            counter += 1


def run_synchronization():
    global counter
    counter = 0

    threads = []

    for _ in range(5):
        thread = threading.Thread(target=increment_counter)
        threads.append(thread)
        thread.start()

    for thread in threads:
        thread.join()

    print("Final counter value:", counter)


def producer_consumer():
    task_queue = queue.Queue()

    def producer():
        for number in range(1, 6):
            print("Produced:", number)
            task_queue.put(number)

        task_queue.put(None)

    def consumer():
        while True:
            item = task_queue.get()

            if item is None:
                task_queue.task_done()
                break

            print("Consumed:", item)
            task_queue.task_done()

    producer_thread = threading.Thread(target=producer)
    consumer_thread = threading.Thread(target=consumer)

    producer_thread.start()
    consumer_thread.start()

    producer_thread.join()
    task_queue.join()
    consumer_thread.join()

    print("Producer-consumer completed")


def run_thread_event():
    event = threading.Event()

    def worker():
        print("Worker waiting for signal...")
        event.wait()
        print("Worker received signal!")

    thread = threading.Thread(target=worker)
    thread.start()

    time.sleep(2)

    print("Main thread sending signal...")
    event.set()

    thread.join()

    print("Event test completed")
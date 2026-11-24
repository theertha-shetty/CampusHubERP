import multiprocessing
import time


def process_task(name):
    print(f"{name} started")
    time.sleep(2)
    print(f"{name} completed")


def run_processes():
    process1 = multiprocessing.Process(
        target=process_task,
        args=("Process 1",)
    )

    process2 = multiprocessing.Process(
        target=process_task,
        args=("Process 2",)
    )

    process1.start()
    process2.start()

    process1.join()
    process2.join()

    print("All processes completed")


def calculate_square(number):
    return number ** 2


def run_process_pool():
    numbers = [1, 2, 3, 4, 5]

    with multiprocessing.Pool(processes=2) as pool:
        results = pool.map(calculate_square, numbers)

    print("Square results:", results)


if __name__ == "__main__":
    run_processes()
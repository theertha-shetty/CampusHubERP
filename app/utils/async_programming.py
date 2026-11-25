import asyncio
import time
from contextlib import asynccontextmanager
async def say_hello():
    print("Hello!")
    await asyncio.sleep(1)
    print("Welcome to CampusHubERP!")


async def main():
    await say_hello()


async def student_task(student_name):
    print(f"{student_name} task started")
    await asyncio.sleep(2)
    print(f"{student_name} task completed")


async def run_multiple_tasks():
    await asyncio.gather(
        student_task("Ananya"),
        student_task("Rahul"),
        student_task("Priya")
    )


if __name__ == "__main__":
    asyncio.run(main())
    asyncio.run(run_multiple_tasks())

async def run_with_gather():
    results = await asyncio.gather(
        student_task("Student 1"),
        student_task("Student 2"),
        student_task("Student 3")
    )

    print("All async tasks finished")

async def run_create_tasks():

    task1 = asyncio.create_task(student_task("Task 1"))
    task2 = asyncio.create_task(student_task("Task 2"))
    task3 = asyncio.create_task(student_task("Task 3"))

    await task1
    await task2
    await task3

    print("All created tasks completed")

async def run_with_timeout():

    try:
        await asyncio.wait_for(
            student_task("Timeout Student"),
            timeout=1
        )

    except asyncio.TimeoutError:
        print("Task timed out!")

async def run_sequential_tasks():

    print("Starting sequential tasks")

    await student_task("Student A")
    await student_task("Student B")
    await student_task("Student C")

    print("All sequential tasks completed")

async def fetch_student(student_id):
    print(f"Fetching student {student_id}...")
    await asyncio.sleep(1)
    return {
        "student_id": student_id,
        "name": f"Student {student_id}"
    }


async def fetch_all_students():
    students = await asyncio.gather(
        fetch_student(101),
        fetch_student(102),
        fetch_student(103)
    )

    print("\nFetched Student Records:")

    for student in students:
        print(student)

async def risky_student_task(student_id):
    await asyncio.sleep(1)

    if student_id == 102:
        raise ValueError("Student record not found!")

    return f"Student {student_id} fetched successfully"


async def run_async_error_handling():
    tasks = [
        risky_student_task(101),
        risky_student_task(102),
        risky_student_task(103)
    ]

    results = await asyncio.gather(
        *tasks,
        return_exceptions=True
    )

    for result in results:
        if isinstance(result, Exception):
            print("Error:", result)
        else:
            print(result)

            from contextlib import asynccontextmanager


@asynccontextmanager
async def student_session():
    print("Student session started")

    try:
        yield
    finally:
        print("Student session closed")


async def run_async_context_manager():
    async with student_session():
        print("Working with student records...")
        await asyncio.sleep(1)

async def write_student_data():
    student_data = "101, Ananya\n102, Rahul\n103, Priya"

    with open("students_async.txt", "w") as file:
        file.write(student_data)

    print("Student data written successfully")


async def read_student_data():
    with open("students_async.txt", "r") as file:
        data = file.read()

    print("\nStudent File Contents:")
    print(data)


async def run_async_file_handling():
    await write_student_data()
    await read_student_data()


async def process_student(student_id, semaphore):
    async with semaphore:
        print(f"Processing student {student_id}...")
        await asyncio.sleep(2)
        print(f"Student {student_id} processed")


async def run_with_semaphore():
    semaphore = asyncio.Semaphore(2)

    tasks = [
        process_student(student_id, semaphore)
        for student_id in range(101, 106)
    ]

    await asyncio.gather(*tasks)

    print("All students processed")

async def async_producer(queue):
    for student_id in range(101, 106):
        print(f"Produced student: {student_id}")
        await queue.put(student_id)
        await asyncio.sleep(0.5)

    await queue.put(None)


async def async_consumer(queue):
    while True:
        student_id = await queue.get()

        try:
            if student_id is None:
                break

            print(f"Consumed student: {student_id}")
            await asyncio.sleep(0.5)

        finally:
            queue.task_done()


async def run_async_queue():
    queue = asyncio.Queue()

    producer = asyncio.create_task(async_producer(queue))
    consumer = asyncio.create_task(async_consumer(queue))

    await producer
    await queue.join()
    await consumer

    print("Async queue processing completed")

async def long_running_task():
    try:
        print("Long-running task started...")
        await asyncio.sleep(10)
        print("Task completed")
    except asyncio.CancelledError:
        print("Task was cancelled")
        raise


async def run_task_cancellation():
    task = asyncio.create_task(long_running_task())

    await asyncio.sleep(2)

    print("Cancelling task...")
    task.cancel()

    try:
        await task
    except asyncio.CancelledError:
        print("Cancellation handled successfully")


async def update_student_record(student_id, lock):
    async with lock:
        print(f"Updating student {student_id}...")
        await asyncio.sleep(1)
        print(f"Student {student_id} updated")


async def run_async_lock():
    lock = asyncio.Lock()

    tasks = [
        update_student_record(101, lock),
        update_student_record(102, lock),
        update_student_record(103, lock)
    ]

    await asyncio.gather(*tasks)

    print("All student records updated safely")

async def student_worker(event):
    print("Student worker waiting for signal...")
    await event.wait()
    print("Student worker received signal!")


async def run_async_event():
    event = asyncio.Event()

    task = asyncio.create_task(student_worker(event))

    await asyncio.sleep(2)

    print("Sending signal...")
    event.set()

    await task

    print("Async event test completed")

async def run_async_wait():
    tasks = [
        asyncio.create_task(student_task("Wait Task 1")),
        asyncio.create_task(student_task("Wait Task 2")),
        asyncio.create_task(student_task("Wait Task 3"))
    ]

    done, pending = await asyncio.wait(
        tasks,
        return_when=asyncio.ALL_COMPLETED
    )

    print(f"Completed tasks: {len(done)}")
    print(f"Pending tasks: {len(pending)}")

    import time


async def timed_student_task(student_id):
    print(f"Student {student_id} started")
    await asyncio.sleep(2)
    print(f"Student {student_id} completed")


async def run_async_timing():
    start_time = time.perf_counter()

    await asyncio.gather(
        timed_student_task(101),
        timed_student_task(102),
        timed_student_task(103)
    )

    end_time = time.perf_counter()

    print(f"Total execution time: {end_time - start_time:.2f} seconds")
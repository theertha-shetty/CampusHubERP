import asyncio

from app.utils.async_programming import (
    main,
    run_multiple_tasks,
    run_with_gather,
    run_create_tasks,
    run_with_timeout,
    run_sequential_tasks,
    fetch_all_students,
    run_async_error_handling,
    run_async_context_manager,
    run_async_file_handling,
    run_with_semaphore,
    run_async_queue,
    run_task_cancellation,
    run_async_lock,
    run_async_event,
    run_async_wait,
    run_async_timing
)

from app.utils.async_programming import main, run_multiple_tasks

print("\n--- BASIC ASYNC TEST ---")
asyncio.run(main())

print("\n--- MULTIPLE ASYNC TASKS TEST ---")
asyncio.run(run_multiple_tasks())

print("\n--- ASYNC GATHER TEST ---")
asyncio.run(run_with_gather())

print("\n--- CREATE TASK TEST ---")
asyncio.run(run_create_tasks())

print("\n--- ASYNC TIMEOUT TEST ---")
asyncio.run(run_with_timeout())


print("\n--- SEQUENTIAL ASYNC TEST ---")
asyncio.run(run_sequential_tasks())

print("\n--- FETCH STUDENTS TEST ---")
asyncio.run(fetch_all_students())

print("\n--- ASYNC ERROR HANDLING TEST ---")
asyncio.run(run_async_error_handling())

print("\n--- ASYNC CONTEXT MANAGER TEST ---")
asyncio.run(run_async_context_manager())


print("\n--- ASYNC FILE HANDLING TEST ---")
asyncio.run(run_async_file_handling())


print("\n--- ASYNC SEMAPHORE TEST ---")
asyncio.run(run_with_semaphore())

print("\n--- ASYNC QUEUE TEST ---")
asyncio.run(run_async_queue())

print("\n--- ASYNC TASK CANCELLATION TEST ---")
asyncio.run(run_task_cancellation())


print("\n--- ASYNC LOCK TEST ---")
asyncio.run(run_async_lock())

print("\n--- ASYNC EVENT TEST ---")
asyncio.run(run_async_event())

print("\n--- ASYNC WAIT TEST ---")
asyncio.run(run_async_wait())

print("\n--- ASYNC TIMING TEST ---")
asyncio.run(run_async_timing())
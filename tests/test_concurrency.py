from app.utils.concurrency import (
    run_threads,
    run_thread_pool,
    run_synchronization,
    producer_consumer,
    run_thread_event
)

print("\n--- THREADING TEST ---")
run_threads()

print("\n--- THREAD POOL TEST ---")
run_thread_pool()

print("\n--- SYNCHRONIZATION TEST ---")
run_synchronization()

print("\n--- PRODUCER CONSUMER TEST ---")
producer_consumer()

print("\n--- THREAD EVENT TEST ---")
run_thread_event()
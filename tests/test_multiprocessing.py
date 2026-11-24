from app.utils.multiprocessing_demo import (
    run_processes,
    run_process_pool
)

if __name__ == "__main__":
    print("\n--- MULTIPROCESSING TEST ---")
    run_processes()

    print("\n--- PROCESS POOL TEST ---")
    run_process_pool()
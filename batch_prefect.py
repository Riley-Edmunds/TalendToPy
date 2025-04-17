from prefect import flow, task
from concurrent.futures import ThreadPoolExecutor
from batch1 import batch1
from batch2 import batch2
from batch3 import batch3

@task
def run_batch1():
    return batch1()

@task
def run_batch2():
    return batch2()

@task
def run_batch3():
    return batch3()

@flow
def master_flow():
    # Start all batch jobs in parallel
    future1 = run_batch1.submit()
    future2 = run_batch2.submit()
    future3 = run_batch3.submit()

    # Wait for all results
    results = [
        future1.result(),
        future2.result(),
        future3.result()
    ]

    # Print results
    for i, result in enumerate(results, 1):
        print(f"Result {i}:", result)
    
if __name__ == "__main__":
    master_flow()

from prefect import flow

@flow
def batch2():
    print("Batch 2")

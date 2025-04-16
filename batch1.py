from prefect import flow

@flow
def batch1():
    print("Batch 1")

from prefect import flow

@flow
def batch3():
    print("Batch 3")

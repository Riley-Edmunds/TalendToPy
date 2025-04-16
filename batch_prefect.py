from prefect import flow # Prefect flow and task decorators
from batch1 import batch1
from batch2 import batch2
from batch3 import batch3

@flow
def master_flow():
    batch1()
    batch2()
    batch3()

if __name__ == "__main__":
    master_flow()

from prefect import flow # Prefect flow and task decorators
from batch1 import batch1
from batch2 import batch2
from batch3 import batch3

@flow
def master_flow():
    future1 = batch1().submit()
    future2 = batch2().submit()
    future3 = batch3().submit()

    result1 = future1.result()
    result2 = future2.result()
    result3 = future3.result()
    
if __name__ == "__main__":
    master_flow()

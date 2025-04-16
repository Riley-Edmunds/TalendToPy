from prefect import flow # Prefect flow and task decorators
from batch1 import batch1
from batch2 import batch2
from batch3 import batch3

@flow
def master_flow():
    batch1 = batch1().submit()
    batch2 = batch2().submit()
    batch3 = batch3().submit()

    result1 = batch1.result()
    result2 = batch2.result()
    result3 = batch3.result()
    
if __name__ == "__main__":
    master_flow()

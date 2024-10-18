from temporalio import activity
import time


@activity.defn
async def say_hello(name: str):
    time.sleep(5)
    print(f"hello hello {name}")
    # raise Exception("hello")

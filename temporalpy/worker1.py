from temporalio.client import Client
from temporalio.worker import Worker

from a1 import say_hello
from wf1 import SayHello
import asyncio


async def main():
    client = await Client.connect("localhost:7233", namespace="default")
    worker = Worker(client, task_queue="hello-task-queue", workflows=[SayHello], activities=[say_hello])
    await worker.run()


if __name__ == "__main__":
    asyncio.run(main())
    # main()

from temporalio.client import Client
from temporalio.worker import Worker

from a2 import say_goodbye
from wf2 import SayGoodbye
import asyncio


async def main():
    client = await Client.connect("localhost:7233", namespace="default")
    worker = Worker(client, task_queue="goodbye-task-queue", workflows=[SayGoodbye], activities=[say_goodbye])
    await worker.run()


if __name__ == "__main__":
    asyncio.run(main())
    # main()

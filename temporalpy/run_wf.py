import asyncio
from uuid import uuid4
from datetime import timedelta

from temporalio.common import RetryPolicy
from temporalio.client import Client, Schedule, ScheduleActionStartWorkflow, ScheduleIntervalSpec, ScheduleOverlapPolicy, ScheduleSpec


async def main():
    client = await Client.connect("localhost:7233")
    schedule_id = str(uuid4())
    await client.create_schedule(schedule_id, Schedule(
        action=ScheduleActionStartWorkflow(
            "SayHello",
            "Shlok",
            id=str(uuid4()),
            task_queue="hello-task-queue",
        ),
        spec=ScheduleSpec(),
    ))

    handle = client.get_schedule_handle(schedule_id)
    await handle.trigger()
    # client.execute_workflow("SayGoodbye", "Patel", id=str(uuid4()), task_queue="goodbye-task-queue")

if __name__ == "__main__":
    asyncio.run(main())

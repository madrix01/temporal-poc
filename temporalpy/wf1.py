from datetime import timedelta
from temporalio import workflow
from temporalio.common import RetryPolicy


with workflow.unsafe.imports_passed_through():
    from a1 import say_hello


@workflow.defn
class SayHello:
    @workflow.run
    async def run(self, name: str):
        return await workflow.execute_activity(
            say_hello,
            name,
            start_to_close_timeout=timedelta(seconds=100),
            retry_policy=RetryPolicy(
                maximum_attempts=4,
            )
        )

from datetime import timedelta
from temporalio import workflow


with workflow.unsafe.imports_passed_through():
    from a2 import say_goodbye


@workflow.defn
class SayGoodbye:
    @workflow.run
    async def run(self, name: str):
        return await workflow.execute_activity(
            say_goodbye,
            name,
            start_to_close_timeout=timedelta(seconds=5)
        )

from temporalio import activity


@activity.defn
async def say_goodbye(name: str):
    print(f"goodbye {name}")

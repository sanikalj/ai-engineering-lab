import asyncio
async def task(name,delay):
    await asyncio.sleep(delay)
    print(f"{name} finished")

async def main():
    await asyncio.gather(
        task("Task A",2),
        task("Task B", 1),
        task("Task C", 3)
    )

asyncio.run(main())
import asyncio

async def fetch_data():
    print("fetching..")
    await asyncio.sleep(1)
    return "Data received"

async def main():
    result= await fetch_data()
    print(result)

asyncio.run(main())

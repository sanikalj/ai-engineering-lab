import asyncio

async def fetch_data():
    print("fetching data..")
    await asyncio.sleep(2)
    print("Data received")

async  def fetch_documents():
    print("analysing documents..")
    await asyncio.sleep(1)
    print("analysed documents")

async def main():
    print("started..")
    await asyncio.gather(fetch_data(),fetch_documents())
    print("...finished")

asyncio.run(main())

import asyncio

async def main():
    task = asyncio.create_task(cal())
    print("A")
    await asyncio.sleep(1)
    print("B")
    await task

async def cal():
    print(1+5)
    await asyncio.sleep(2)
    print(9+8)

asyncio.run(main())
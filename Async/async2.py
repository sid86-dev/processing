import asyncio

async def main():
    task = asyncio.create_task(cal())
    print("A")
    await asyncio.sleep(5)
    return_value = await task
    print("B")
    print(f"Return value = {return_value}")


async def cal():
    await asyncio.sleep(2)
    a = 1+5
    print(a)
    await asyncio.sleep(2)
    b = 9+8
    print(b)
    return b-a

asyncio.run(main())
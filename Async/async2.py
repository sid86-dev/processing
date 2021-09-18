import asyncio

async def main():
    task = asyncio.create_task(cal())
    print("A")
    await asyncio.sleep(5)
    return_value = await task
    c = return_value + 20
    print(f"Return value = {c}")

async def cal():
    await asyncio.sleep(2)
    a = 1+5
    print(a)
    await asyncio.sleep(2)
    b = 9+8
    print(b)
    return b-a

asyncio.run(main())
import asyncio

async def loading(id, sleep_time):
    print(f"{id} is starting to fetch data")
    await asyncio.sleep(sleep_time)
    return {"id": id, "data": f"data from id {id}"}

async def main():
    task1 = asyncio.create_task(loading(1,2))
    task2 = asyncio.create_task(loading(2,3))
    task3 = asyncio.create_task(loading(3,1))

    result1 = await task1
    result2 = await task2
    result3 = await task3

    print(result1, result2, result3)
asyncio.run(main())     
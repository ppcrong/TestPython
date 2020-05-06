import asyncio
import time

now = lambda: time.time()


async def do_something(num):
    print('第 {} 任務+++++'.format(num))
    await asyncio.sleep(2)
    print('第 {} 任務-----'.format(num))
    return '第 {} 任務完成'.format(num)


async def raise_error(num):
    raise ValueError
    print('這邊不會執行到')


async def main():
    tasks = [do_something(i) for i in range(5)]
    tasks1 = [raise_error(i) for i in range(5)]

    results = await asyncio.gather(*tasks, *tasks1, return_exceptions=True)
    print(results)


if __name__ == "__main__":
    start = now()
    asyncio.run(main())
    print('TIME: ', now() - start)

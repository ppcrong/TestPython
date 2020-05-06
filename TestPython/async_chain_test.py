import asyncio
import time
import random

# https://www.maxlist.xyz/2020/04/03/async-io-design-patterns-python/

now = lambda: time.time()


# 任務一
async def step_one(num, n):
    time_sleep = random.randint(0, 1)
    print('Task {},step one, sleep {}+++++'.format(n, time_sleep))
    await asyncio.sleep(time_sleep)
    print('Task {},step one, wakeup-----'.format(n))
    num += 1
    return num


# 任務二
async def step_two(num, n):
    time_sleep = random.randint(0, n)
    print('Task {},step two, sleep {}+++++'.format(n, time_sleep))

    await asyncio.sleep(time_sleep)
    print('Task {},step two, wakeup-----'.format(n))
    num += 2
    return num


# 任務三
async def step_three(num, n):
    time_sleep = random.randint(0, n)
    print('Task {},step three, sleep {}+++++'.format(n, time_sleep))
    await asyncio.sleep(time_sleep)
    print('Task {},step three, wakeup-----'.format(n))
    num += 3
    return [n, num]


# 任務調度
async def asyncio_chain(n):
    s1 = await step_one(n, n)
    s2 = await step_two(s1, n)
    s3 = await step_three(s2, n)
    return s3


# 收集任務結果
async def main():
    tasks = [asyncio_chain(n) for n in range(3)]
    result = await asyncio.gather(*tasks)
    print(result)


if __name__ == "__main__":
    start = now()
    asyncio.run(main())
    print('TIME: ', now() - start)

import asyncio

# https://www.maxlist.xyz/2020/04/03/async-io-design-patterns-python/

# 消費者
async def consumer(n, q):
    print('consumer {}: 進入商店'.format(n))
    while True:
        item = await q.get()
        print('consumer {}: 購買產品 {}'.format(n, item))
        await asyncio.sleep(0.15)
        q.task_done()
    print('consumer {}: ending'.format(n))


# 生產者 A
async def producer_a(q, num_workers):
    print('生產者A: 開始生產')
    for i in range(num_workers * 2):
        await q.put('A ' + str(i))
        print('生產者A: 上架產品A {}'.format(i))
        await asyncio.sleep(0.01)


# 生產者 B
async def producer_b(q, num_workers):
    print('生產者B: 開始生產')
    for i in range(num_workers * 2):
        await q.put('B ' + str(i))
        print('生產者B: 上架產品B {}'.format(i))
        await asyncio.sleep(0.02)


# 任務調度
async def main(num_consumers, num_workers):
    q = asyncio.Queue(maxsize=num_consumers)

    prod_a = [asyncio.create_task(producer_a(q, num_workers))]
    prod_b = [asyncio.create_task(producer_b(q, num_workers))]

    consumers = [
        asyncio.create_task(consumer(i, q)) for i in range(num_consumers)
    ]

    await asyncio.gather(*prod_a, *prod_b)
    print('生產者 All: ending')

    await q.join()
    print('consumers All: ending')

    for c in consumers:
        c.cancel()


# main(消費者數量, 生產者數量)
asyncio.run(main(3, 2))

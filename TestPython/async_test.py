import asyncio
import threading
import time

# https://www.maxlist.xyz/2020/03/29/python-coroutine/

now = lambda: time.time()


async def do_something(num):
    print('第 {} 任務+++++'.format(num))
    await asyncio.sleep(2)
    print('第 {} 任務-----'.format(num))
    return '第 {} 任務完成'.format(num)


async def raise_error(num):
    raise ValueError
    print('這邊不會執行到')


async def do_something_test(num):
    print('do_something_test {} +++++'.format(num))
    await asyncio.sleep(3)
    print('do_something_test {} -----'.format(num))
    return 'do_something_test {} complete'.format(num)


async def do_something_test2(num):
    print('do_something_test2() thread: {}'.format(threading.current_thread()))

    print('do_something_test2 {} +++++'.format(num))
    await asyncio.sleep(3)
    print('do_something_test2 {} -----'.format(num))
    return 'do_something_test2 {} complete'.format(num)


async def main():
    print('main() thread: {}'.format(threading.current_thread()))

    tasks0 = [do_something(i) for i in range(5)]
    tasks1 = [raise_error(i) for i in range(5)]
    tasks2 = [do_something_test(100)]

    results = await asyncio.gather(*tasks0, *tasks1, *tasks2, do_something_test2(200), return_exceptions=True)
    print(results)


if __name__ == "__main__":
    print('thread: {}'.format(threading.current_thread()))
    start = now()
    asyncio.run(main())
    print('TIME: ', now() - start)

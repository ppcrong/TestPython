import concurrent.futures
import threading
import time

now = lambda: time.time()


def foo(bar):
    print('foo: {}'.format(threading.current_thread()))
    print('hello {}'.format(bar))
    return 'foo'


if __name__ == "__main__":
    print('thread: {}'.format(threading.current_thread()))
    start = now()
    with concurrent.futures.ThreadPoolExecutor() as executor:
        future = executor.submit(foo, 'world!')
        return_value = future.result()
        print(return_value)
    print('TIME: ', now() - start)

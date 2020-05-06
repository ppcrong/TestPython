import concurrent.futures
import threading
import time

# https://stackoverflow.com/questions/6893968/how-to-get-the-return-value-from-a-thread-in-python
# https://tinyurl.com/y7wjbw6l

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

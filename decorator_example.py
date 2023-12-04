def decorator(func):
    def wrapper():
        print("Before")
        result = func()
        print("after")
        return result

    return wrapper()


@decorator
def hello():  # when we call function as this way our wrapper should be not callable, and we don't need ()
    print("hello")


# decorator(hello) if we need call function with this way our wrapper function must be callable, and we need use ()

import time


def timer(func):
    def wrapper():
        start_time = time.time()
        func()
        elapsed = time.time() - start_time
        print("took {} second to execute".format(elapsed))

    return wrapper


@timer
def counter():
    total = 0
    for i in range(0, 1000000):
        total = + i
    return total


counter()
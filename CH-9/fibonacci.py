from clockdeco0 import clock
import functools


@functools.cache
@clock
def fibonacci(n):
    if n<2:
        return n
    return fibonacci(n-2) + fibonacci(n-1)

if __name__ == "__main__":
    print(fibonacci(6))
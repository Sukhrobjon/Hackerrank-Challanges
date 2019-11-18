from functools import lru_cache


def fibonacci(n):
    if n == 1:
        return 1
    elif n == 2:
        return 1
    elif n > 2:
        return fibonacci(n-1) + fibonacci(n-2)


fibonacci_cache = {}
def fibonacci_optimized(n):
    """Return fibonacci number"""
    # if we have cached the value, then return it
    if n in fibonacci_cache:
        return fibonacci_cache[n]
    

    # else Compute the Nth term
    if n == 1:
        value = 1
    elif n == 2:
        value = 1
    elif n > 2:
        value = fibonacci_optimized(n-1) + fibonacci_optimized(n-2)

    fibonacci_cache[n] = value
    return value


@lru_cache(maxsize=1000)  # default maxsize 120
def fibonacci_builtin(n):
    if n == 1:
        return 1
    elif n == 2:
        return 1
    elif n > 2:
        return fibonacci_builtin(n-1) + fibonacci_builtin(n-2)

# ======= Test Function =======


for n in range(1, 101):
    print(n, ":", fibonacci(n))

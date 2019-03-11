# Version 1 - explicit implementation
fibonacci_cache = {}
def fibonacci(n):
    """Expects integer n>=1 and computes the fibonacci sequence"""
    # If we have cached the value, then return it
    if n in fibonacci_cache:
        return fibonacci_cache[n]
    
    # Computed the Nth term
    if n == 1 or n == 2:
        value = 1
    elif n > 2:
        value = fibonacci(n-1) + fibonacci(n-2)

    # Cache the value and return it
    fibonacci_cache[n] = value
    return value

# Test
for n in range(1, 1000):
    print(n, ":", fibonacci(n))

# Version 2 - with decorator
from functools import lru_cache

@lru_cache(maxsize = 1000)
def fibonacci_v2(n):
    """Expects integer n>=1 and computes the fibonacci sequence"""
    # Computed the Nth term
    if n == 1 or n == 2:
        value = 1
    elif n > 2:
        return fibonacci(n-1) + fibonacci(n-2)

# Test
for n in range(1, 1000):
    print(n, ":", fibonacci_v2(n))
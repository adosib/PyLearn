# Fibonacci sequence generator
def get_fib(n):
    a = 1
    b = 1
    for i in range(n):
        yield a
        a, b = b, a+b

for num in get_fib(1000):
    print(num)


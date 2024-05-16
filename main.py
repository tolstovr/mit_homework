def fib(n: int) -> int:
    if n <= 2:
        return n - 1
    else:
        return fib(n - 1) + fib(n - 2)

n = int(input("n: "))
print(f"fib({n}) = {fib(n)}")
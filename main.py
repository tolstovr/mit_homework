from typing import Generator

def fib(n: int) -> Generator[int, None, None]:
    a, b = 0, 1
    for _ in range(n):
        yield a
        a, b = b, a + b

n = int(input("n: "))
print(*list(fib(n)), sep="\n")
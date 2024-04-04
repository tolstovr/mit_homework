# import __hello__
from functools import lru_cache

@lru_cache(None)
def fib(n):
    if n <= 0:
        return "Неверный ввод"
    if n <= 2:
        return n - 1
    return fib(n-1) + fib(n-2)


def get_sequence(n):
    sequence = [0, 1]
    for i in range(2, n):
        sequence.append(fib(i + 1))
    return sequence

    
print(f"Your fibonacci sequence is:", *get_sequence(int(input("N: "))))
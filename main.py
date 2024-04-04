# import __hello__

def fib(n):
    if n <= 0:
        return "Неверный ввод"
    if n <= 2:
        return n - 1
    return fib(n-1) + fib(n-2)
    
print(f"Your fibonacci number is {fib(int(input("N: ")))}")
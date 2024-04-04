# import __hello__

def fib(n):
    if n <= 0:
        return "Неверный ввод"
    elif n == 1 or n == 2:
        return 1
    else:
        return fib(n - 1) + fib(n - 2)
    
print(f"Your fibonacci number is {fib(int(input("N: ")))}")
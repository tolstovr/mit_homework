# import __hello__

def fib(n):
    if n <= 0:
        return "Неверный ввод"
    if n == 1:
        return [0]
    if n == 2:
        return [0, 1]
    sequence = [0, 1]
    for _ in range(2, n):
        next_number = sequence[-1] + sequence[-2]
        sequence.append(next_number)
    return sequence
    
print(*fib(int(input("N: "))), sep="\n")

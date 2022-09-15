# Задайте число. Составьте список чисел Фибоначчи,
# в том числе для отрицательных индексов.

# Пример:

# для k = 8 список будет выглядеть так: 
# [-21 ,13, -8, 5, −3, 2, −1, 1, 0, 1, 1, 2, 3, 5, 8, 13, 21]

k = 8

fib = [1, 1]
ne_fib = [1, -1]

def fibo(k, fib, ne_fib):
    for i in range(2, k):
        temp = fib[i-2] + fib[i - 1]
        fib.append(temp)  
        temp_ne_fib = ne_fib[i - 2] - ne_fib[i - 1]
        ne_fib.append(temp_ne_fib)
    ne_fib.reverse()
    ne_fib.append(0)
    return (ne_fib + fib)

res = fibo(k, fib, ne_fib)
print(res)


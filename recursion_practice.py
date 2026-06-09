def sum(n):

    if n == 1:
        return 1
    
    return n + sum(n - 1)

print(sum(100))

def factorial(n):

    if n == 1:
        return 1
    
    return n * factorial(n - 1)

print(factorial(10))

def fibonacci(n):

    if n == 1:
        return 0
    elif n == 2:
        return 1

    return fibonacci(n - 1) + fibonacci(n - 2)

print(fibonacci(1))
print(fibonacci(2))
print(fibonacci(3))
print(fibonacci(4))
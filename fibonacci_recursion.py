def fibonacci_recursion(n):
    if n<3:
        return n-1
    return fibonacci_recursion(n-1)+fibonacci_recursion(n-2)
fibonacci_recursion(10)

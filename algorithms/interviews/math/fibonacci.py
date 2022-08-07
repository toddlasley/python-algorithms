# Return the nth number of the Fibonacci sequence where n starts at zero.

def fibonacci_iterative(n: int) -> int:
    if n == 0 or n == 1:
        return n
    else:
        x = 0
        i = y = 1

        while i < n:
            temp = x
            x = y
            y = temp + y
            i += 1            

        return y

def fibonacci_recursive(n: int) -> int:
    if n == 0 or n == 1:
        return n
    else:
        return fibonacci_recursive(n - 1) + fibonacci_recursive(n - 2)

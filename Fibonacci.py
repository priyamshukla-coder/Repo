def fibonacci(n):
    fib_sequence = [0, 1]
    
    if n <= 0:
        return "Input should be a positive integer."
    elif n == 1:
        return [0]
    elif n == 2:
        return fib_sequence
    
    for i in range(2, n):
        next_number = fib_sequence[-1] + fib_sequence[-2]
        fib_sequence.append(next_number)
    
    return fib_sequence

# Example usage:
n = int(input("Enter the number of Fibonacci terms you want: "))
print(fibonacci(n))
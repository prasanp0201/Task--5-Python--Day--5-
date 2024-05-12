#using the python lambda function create a fibonacci series from 1 to 50 elements

fibonacci = lambda n: n if n <= 1 else fibonacci(n-1) + fibonacci(n-2)

num_elements = 50
fib_series = [fibonacci(i) for i in range(num_elements)]

print(fib_series)
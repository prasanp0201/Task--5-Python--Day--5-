#Write a python code using lambda function to check every element of a list is an integer or string


# Sample list containing a mix of integers and strings
data = [-3, 'hello', 0, 'world', 43, 'python', 3.0]

# Lambda function to check if element is an integer or string
check_type = lambda x: 'Integer' if isinstance(x, int) else 'String'

# Use map function to apply the lambda function to each element of the list
result = list(map(check_type, data))

# Print the result
print(result)
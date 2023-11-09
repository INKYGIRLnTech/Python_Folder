
# Add function
def add(x, y):
    return x + y

# Subraction function
def subtract(x, y):
    return x - y 


# Multiplication function
def multiply(x, y):
    return x * y

# Division function
def divide(x, y):
    if y == 0:
        raise ValueError('Can not divide by zero')
    return x / y
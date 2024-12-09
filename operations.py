# operations.py

def multiply_numbers(a, b):
    """返回 a 和 b 的积"""
    print(f"multiply_numbers({a}, {b}) called")
    result = a * b
    print(f"Result of multiply_numbers: {result}")
    return result

def divide_numbers(a, b):
    """返回 a 除以 b 的商"""
    print(f"divide_numbers({a}, {b}) called")
    if b != 0:
        result = a / b
        print(f"Result of divide_numbers: {result}")
        return result
    else:
        print("Error: Division by zero")
        return "Error: Division by zero"


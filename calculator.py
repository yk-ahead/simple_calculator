# calculator.py

from operations import multiply_numbers  # 调用 operations.py 中的乘法功能

def add_numbers(a, b):
    """返回 a 和 b 的和"""
    print(f"add_numbers({a}, {b}) called")
    result = a + b
    print(f"Result of add_numbers: {result}")
    return result

def subtract_numbers(a, b):
    """返回 a 和 b 的差"""
    print(f"subtract_numbers({a}, {b}) called")
    result = a - b
    print(f"Result of subtract_numbers: {result}")
    return result

def multiply_and_add(a, b, c):
    """先做乘法再做加法，作为加法扩展"""
    print(f"multiply_and_add({a}, {b}, {c}) called")
    product = multiply_numbers(a, b)
    print(f"Multiplication result inside multiply_and_add: {product}")
    result = add_numbers(product, c)
    print(f"Final result inside multiply_and_add: {result}")
    return result


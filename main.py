from calculator import add_numbers, subtract_numbers
from operations import multiply_numbers, divide_numbers

def main():
    num1 = 10
    num2 = 5
    
    print(f"Starting main calculations...\n")
    
    print(f"Adding {num1} and {num2}: {add_numbers(num1, num2)}")
    print(f"Subtracting {num1} and {num2}: {subtract_numbers(num1, num2)}")
    print(f"Multiplying {num1} and {num2}: {multiply_numbers(num1, num2)}")
    print(f"Dividing {num1} by {num2}: {divide_numbers(num1, num2)}")

if __name__ == "__main__":
    main()


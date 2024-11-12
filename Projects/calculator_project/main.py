from addition import Addition
from subtraction import Subtraction
from multiplication import Multiplication
from division import Division

# Main function to demonstrate the calculator operations
def main():
    a = 10
    b = 5

    # Addition
    # addition_result = Addition.add(a, b)
    # print(f"Addition: {a} + {b} = {addition_result}")

    # # Subtraction
    subtraction_result = Subtraction.subtract(a, b)
    print(f"Subtraction: {a} - {b} = {subtraction_result}")

    # # Multiplication
    # multiplication_result = Multiplication.multiply(a, b)
    # print(f"Multiplication: {a} * {b} = {multiplication_result}")

    # # Division
    # try:
    #     division_result = Division.divide(a, b)
    #     print(f"Division: {a} / {b} = {division_result}")
    # except ValueError as e:
    #     print(e)

# Run the main function
if __name__ == "__main__":
    main()
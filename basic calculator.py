"""
A simple command-line calculator application.

This module provides a basic calculator that performs arithmetic operations
(addition, subtraction, multiplication, and division) with user input validation
and error handling.
"""


def get_numbers() -> tuple[float, float]:
    """
    Retrieve two numbers from the user.

    Returns:
        tuple[float, float]: A tuple containing the first and second numbers.

    Raises:
        ValueError: If the user input cannot be converted to a float.
    """
    try:
        num1 = float(input("Enter the first number: "))
        num2 = float(input("Enter the second number: "))
        return num1, num2
    except ValueError:
        print("Error: Please enter valid numbers.")
        raise


def display_menu() -> None:
    """Display the calculator menu options."""
    print("\nSelect operation:")
    print("1. Addition (+)")
    print("2. Subtraction (-)")
    print("3. Multiplication (*)")
    print("4. Division (/)")
    print()


def perform_operation(num1: float, num2: float, operation: str) -> None:
    """
    Perform the selected arithmetic operation.

    Args:
        num1 (float): The first number.
        num2 (float): The second number.
        operation (str): The operation code ('1', '2', '3', or '4').
    """
    operations = {
        '1': (lambda a, b: a + b, "Addition"),
        '2': (lambda a, b: a - b, "Subtraction"),
        '3': (lambda a, b: a * b, "Multiplication"),
        '4': (lambda a, b: a / b if b != 0 else None, "Division"),
    }

    if operation not in operations:
        print("Invalid input! Please select a valid operation (1/2/3/4).")
        return

    operation_func, operation_name = operations[operation]

    try:
        if operation == '4' and num2 == 0:
            print("Error: Cannot divide by zero!")
            return

        result = operation_func(num1, num2)
        print(f"\n{num1} {operation_name.lower()} {num2} = {result}\n")
    except Exception as e:
        print(f"Error during calculation: {e}")


def calculator() -> None:
    """Run the calculator application."""
    print("=" * 50)
    print("         Welcome to the Simple Calculator!")
    print("=" * 50)

    while True:
        try:
            num1, num2 = get_numbers()
            display_menu()
            choice = input("Enter choice (1/2/3/4): ")
            perform_operation(num1, num2, choice)

            again = input("Do you want to perform another calculation? (yes/no): ").strip().lower()
            if again not in ['yes', 'y']:
                print("Thank you for using the calculator. Goodbye!")
                break
        except ValueError:
            continue
        except KeyboardInterrupt:
            print("\nCalculator closed.")
            break


if __name__ == "__main__":
    calculator()

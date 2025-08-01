# hello_world.py
from warnings import catch_warnings


def factorial(number):
    if number < 0:
        return "Number is illegal!"
    elif 0 <= number <=1:
        return 1
    else:
        return number * factorial(number - 1)

if __name__ == "__main__":
    try:
        number = int(input("Enter your integer number: "))
        print(factorial(number))
    except ValueError:
        print("Please enter a valid integer.")


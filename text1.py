# hello_world.py

def greet(number):
    while number > 1:
        number = number * number - 1
        # 小心：这个可能会变得非常大，甚至死循环！
        if number > 1e10:
            return "Number is too large!"
    return f"Hello, {number}!"

if __name__ == "__main__":
    number = int(input("Enter your number: "))
    print(greet(number))

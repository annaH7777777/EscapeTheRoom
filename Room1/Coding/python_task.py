#Write a function sum_digits(n: int) -> int that returns the sum of the digits in an integer.
def sum_digits(n: int):
    int_list = [int(d) for d in str(n)]

    number = 0
    for num in int_list:
        number += num
    return number


if __name__ == '__main__':
    print("Enter numbers to sum, separated by spaces:")
    input_str = input()
    try:
        result = sum_digits(int(input_str))
        print(f"The sum of the numbers is: {result}")
    except ValueError:
        print("Error: Please enter a valid integer.")

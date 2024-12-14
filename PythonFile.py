# Input number from the user
number = int(input("Enter a number: "))

# Check if the number is even or odd and perform a calculation
if number % 2 == 0:
    result = number + 5
    print(f"The number {number} is even. After adding 5, the result is {result}.")
else:
    result = number * 2
    print(f"The number {number} is odd. After multiplying by 2, the result is {result}.")


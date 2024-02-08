def add_numbers(num1, num2):
    sum = num1 + num2
    return sum

# Call the add_numbers() function and store the result
num1 = int(input("input ur first number:"))
num2 = int(input ("input ur second number:"))
result = add_numbers(num1, num2)

# Print the result
print("\033[33m" , end = " " )
print(f"The sum is:{result}")
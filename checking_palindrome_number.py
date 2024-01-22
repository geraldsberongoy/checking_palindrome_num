# Exercise 9: Check Palindrome Number
# Write a program to check if the given number is a palindrome number.

# A palindrome number is a number that is the same after reverse. For example, 545, is the palindrome numbers

# Expected Output:

# original number 121
# Yes. given number is palindrome number

# original number 125
# No. given number is not palindrome number

#CODE
number1 = "123454321"
lenght = len(number1)

print(f"Original number {number1}")
reversed_number = number1[-1:-(lenght+1):-1]
if number1 == reversed_number:
    print(True)
else:
    print(False)
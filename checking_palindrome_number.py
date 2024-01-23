# Exercise 9: Check Palindrome Number
# Write a program to check if the given number is a palindrome number.

# A palindrome number is a number that is the same after reverse. For example, 545, is the palindrome numbers

# Expected Output:

# original number 121
# Yes. given number is palindrome number

# original number 125
# No. given number is not palindrome number

# Pseudocode
# assigning variable for the number
# transforming the variable to str
# reversing the number using index and storing it to new variable(reversed)
# if-else start if number equals reversed, True, if not, False

def palindrome(number):
    print(f"Original number {number}")
    number = str(number)
    reversed_number = number[::-1]
    if number == reversed_number:
        print('Yes. Given number is palindrome number.\n')
    else:
        print("No. Given number is not palindrome number\n")

number=input("Input number: ")
palindrome(121)
palindrome(123)
palindrome(number)
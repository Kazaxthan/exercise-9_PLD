
#Exercise 9: Check Palindrome Number
#Write a program to check if the given number is a palindrome number.
#A palindrome number is a number that is the same after reverse. For example, 545, is the palindrome numbers.

# Get user input for the number
user_input = input("Enter a number: ")

try:
    # Convert the user input to an integer
    num = int(user_input)
except ValueError:
    print("Invalid input. Please enter a valid number.")
    exit()



#Backend
def result(number):
    # Convert the number to a string for easy reversal
    num_str = str(number)
    
    # Check if the reversed string is equal to the original string
    return num_str == num_str[::-1]


# Check if the number is a palindrome
if result(num):
    print(f"{num} is a palindrome number.")
else:
    print(f"{num} is not a palindrome number.")
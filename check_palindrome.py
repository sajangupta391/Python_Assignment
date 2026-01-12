# Question 6

def check_palindrome():
    user_input = input("Enter a string: ")

    original_string = user_input.lower()
    
    reversed_string = ""

    for i in range(len(original_string) - 1, -1, -1):
        reversed_string += original_string[i]

    if original_string == reversed_string:
        print("The string is a palindrome.")
    else:
        print("The string is NOT a palindrome.")

check_palindrome()
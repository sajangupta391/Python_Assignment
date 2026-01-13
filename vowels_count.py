# Question 7

def vowels_count():
    name = input("Enter a string: ")
    
    vowels = "aeiou"
    
    count = 0
    
    for char in name.lower():
        if char in vowels:
            count += 1

    print(f"Number of vowels: {count}")

vowels_count()
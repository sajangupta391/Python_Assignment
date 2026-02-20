# Question 17

def even_numbers(n):
    try:
        # the input an integer
        even_limit = int(n)
        
        if even_limit < 2:
            return []
            
        return [num for num in range(2, even_limit + 1) if num % 2 == 0]
    
    except (ValueError, TypeError) as e:
        return f"Error: provide a valid number. (Details:{e})"

print(f"Input : {even_numbers(5)}")

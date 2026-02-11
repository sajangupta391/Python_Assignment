def fibonacci_iterative(n):
    """
    Prints the first n numbers of the Fibonacci sequence using iteration.
    Includes exception handling for invalid inputs.
    """
    try:
        # 1. Validate Input
        n = int(n) # convert input to integer
        
        if n <= 0:
            print("Input must positive integer greater than 0.")
            return

        # 2. Variable Initialization
        # 'a' is current number, 'b' is next number
        a, b = 0, 1
        result = []

        # 3. Iterative Loop
        for _ in range(n):
            result.append(str(a)) # Store current number string 
            
            temp = a
            a = b
            b = temp + b

        # 4.formatted output
        print(", ".join(result))

    except ValueError:
        print("Error: Invalid input enter a whole number.")
    except Exception as e:
        print(f"An unexpected error: {e}")

# --- Run ---

print("Test Case 1 (n = 6):")
fibonacci_iterative(6)

print("\n Test Case 2 (n = 1):")
fibonacci_iterative(1)

print("\n Test Case 3 (Invalid Input):")
fibonacci_iterative("Hello")
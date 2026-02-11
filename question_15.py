def leap_year(year_input):
    """
    Determines if a given input is a leap year.
    Handles exceptions for non-integer inputs.
    """
    try:
        # 1. Input Validation and Conversion
        # We convert the input to an integer first.
        # This handles inputs like "2020" (string) or 2020.0 (float).
        val = float(year_input)
        if not val.is_integer():
            raise ValueError("Year must whole number.")
        
        year = int(val)

        if year <= 0:
            print(f"Input: {year_input} -> Error: Year must positive number.")
            return None
        
        if (year % 4 == 0):
            if (year % 100 == 0):
                if (year % 400 == 0):
                    result = True  # Divisible 400 -> Leap Year
                else:
                    result = False # Divisible 100 but not 400 -> Not Leap Year
            else:
                result = True      # Divisible 4 but not 100 -> Leap Year
        else:
            result = False         # Not divisible 4 -> Not Leap Year

        # 3. Output
        return result

    except ValueError:
        print(f"Input: {year_input} -> Error: Invalid input. Please enter a valid integer year.")
        return None
    except Exception as e:
        print(f"An unexpected error occurred: {e}")
        return None

# --- Execution & Cases ---

print("--- Standard Cases ---")
print(f"Input: 2020 -> {leap_year(2020)}")  # True (Divisible by 4)
print(f"Input: 1900 -> {leap_year(1900)}")  # False (Divisible by 100, not 400)
print(f"Input: 2000 -> {leap_year(2000)}")  # True (Divisible by 400)

print("\n--- Exception Handling Cases ---")
leap_year("Hello")   # Invalid string
leap_year(2023.5)    # Decimal 
leap_year(-500)      # Negative
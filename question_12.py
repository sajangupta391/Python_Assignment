def count_characters(text_input):
    if text_input is None:
        raise ValueError("Input cannot be None. Please provide a valid string.")

    if not isinstance(text_input, str):
        raise TypeError(f"Input must be a string. You provided: {type(text_input).__name__}")

    frequency = {}
    for char in text_input:
        if char in frequency:
            frequency[char] += 1
        else:
            frequency[char] = 1
            
    return frequency

# --- Exception Handling ---

test_cases = [
    12345,        
    ["a", "b"],   
    None,          
    "", 
]

print("--- Starting Tests ---\n")

for item in test_cases:
    try:
        result = count_characters(item)
        print(f"Input: {repr(item)} -> Result: {result}")
    
    except (ValueError, TypeError) as e:
        print(f"Input: {repr(item)} -> Error: {e}")

print("\n Complete ")
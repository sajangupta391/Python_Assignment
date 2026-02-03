from collections import Counter

def check_anagram(str1, str2):
    if str1 is None or str2 is None:
        raise ValueError("Inputs cannot be None. Please provide valid strings.")

    if not isinstance(str1, str) or not isinstance(str2, str):
        raise TypeError(f"Inputs must be strings. Received types: {type(str1).__name__} and {type(str2).__name__}")

    s1_clean = str1.lower().replace(" ", "")
    s2_clean = str2.lower().replace(" ", "")

    if len(s1_clean) != len(s2_clean):
        return False

    return Counter(s1_clean) == Counter(s2_clean)

# --- Exception Handling ---

test_cases = [
    ("listen", "silent"),   # Valid: True
    ("hello", "world"),     # Valid: False
    ("Triangle", "Integral"), # Valid: True Case insensitive
    ("test", 123),          # Invalid: Integer
    (None, "silent"),       # Invalid: None
    (["a"], ["a"])          # Invalid: List
]

print("--- Starting ---\n")

for val1, val2 in test_cases:
    try:
        result = check_anagram(val1, val2)
        print(f"Input: '{val1}' vs '{val2}' -> Anagram? {result}")
    
    except (ValueError, TypeError) as e:
        print(f"Input: '{val1}' vs '{val2}' -> Error: {e}")

print("\n--- Complete ---")
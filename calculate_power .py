# Qustion 16

def calculate_power(x, y):
    result = 1
    
    abc_y = abs(y)
    
    for _ in range(abc_y):
        result = result * x
        
    if y < 0:
        return 1 / result
    
    return result

base = 2
exponent = 3

output = calculate_power(base, exponent)
print(f"Input: x = {base}, y = {exponent}")
print(f"Expected Output: {output}")
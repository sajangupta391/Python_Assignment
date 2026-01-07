# Question 5

def calculate_factorial(n):
    """
    Calculates the factorial of non-negative int.
    """
    if not isinstance(n, int):
        return "Error: Input must be int."

    if n < 0:
        return "Error: Input must be non-negative int."

    if n == 0:
        return 1

    result = 1
    for i in range(1, n + 1):
        result *= i
    return result

print(f"Factorial :", {calculate_factorial(5)})

# Question 9

def sum_digits(n):
    n = abs(n)
    
    total = 0
    while n > 0:
        digit = n % 10
        total += digit
        n = n // 10     
    return total

print(sum_digits(123))
print(sum_digits(4567))
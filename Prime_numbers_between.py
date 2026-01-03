def is_prime(n):
    if n <= 1:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True

def find_primes_in_range():
    print("Prime Number Finder:")
    
    while True:
        try:
            start_input = input("Enter start num: ")
            end_input = input("Enter end num: ")

            start = int(start_input)
            end = int(end_input)

            if start < 0 or end < 0:
                raise ValueError("Numbers must positive.")
            if start > end:
                raise ValueError("Start number cannot be larger end number.")

            primes = []
            for num in range(start, end + 1):
                if is_prime(num):
                    primes.append(num)

            print(f"\nSuccess! Found {len(primes)} prime numbers between {start} and {end}:")
            print(primes)
            break 

        except ValueError as e:
            print(f"\n[!] Invalid Input. {e}")

        except Exception as e:
            print(f"\n[!] Unexpect Error: {e}")
            break


find_primes_in_range()

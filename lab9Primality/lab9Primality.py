import math
import random

def is_prime_optimized_school(n):
    """
    Determines if a number 'n' is prime using the Optimized School Method.
    It checks for divisibility from 2 up to the square root of 'n'.
    """
    if n <= 1:
        return False
    if n <= 3:
        return True
    
    # Check if 'n' is divisible by 2 or 3
    if n % 2 == 0 or n % 3 == 0:
        return False
    
    # Check for divisors from 5 up to sqrt(n)
    # The loop steps by 6 (i, i+2) because all primes > 3 are of the form 6k ± 1
    i = 5
    limit = int(math.sqrt(n))
    '''
    print(f"--- Optimized School Method Steps for {n} ---")
    print(f"Checking divisors up to floor(sqrt({n})) = {limit}")
    '''
    
    while i <= limit:
        print(f"Checking divisibility by {i}...")
        if n % i == 0:
            print(f"Found divisor {i}. {n} is not prime.")
            return False
        
        #print(f"Checking divisibility by {i + 2}...")
        if n % (i + 2) == 0:
            print(f"Found divisor {i + 2}. {n} is not prime.")
            return False
        i += 6
        
    print(f"No divisors found up to {limit}. {n} is prime.")
    return True

# ----------------------------------------------------------------------

def power(a, d, n):
    """
    Utility function: Computes (a^d) % n
    using binary exponentiation (modular exponentiation).
    """
    res = 1
    a = a % n
    print(f'Before power loop: a: {a}, d: {d}, res: {res}')
    while d > 0:
        if d & 1:
            res = (res * a) % n
        d = d >> 1
        a = (a * a) % n
        print(f'After a power loop: a: {a}, d: {d}, res: {res}')
    return res

def miller_rabin_test(n, k=1):
    """
    Determines if a number 'n' is (probably) prime using the Miller-Rabin test.
    'k' is the number of times to run the test (i.e., the number of 'witnesses' to check).
    """
    if n <= 1:
        return False
    if n == 2 or n == 3:
        return True
    if n % 2 == 0:
        return False

    # Write n-1 as 2^r * d, where d is odd
    r, d = 0, n - 1
    while d % 2 == 0:
        d //= 2
        r += 1

    print(f"\n--- Miller-Rabin Test Steps for {n} (k={k}) ---")
    print(f"Decomposition: {n} - 1 = 2^{r} * {d}")

    # Witness Loop
    for _ in range(k):
        #a = random.randint(2, n - 2)
        a = 2
        print(f"Testing with random base 'a' = {a}...")
        x = power(a, d, n)
        
        print(f'x: {x}')
        if x == 1 or x == n - 1:
            print(f"Passed initial check (a^d mod n = {x}). Base '{a}' is not a witness.")
            continue

        # Squaring loop
        for _ in range(r - 1):
            x = power(x, 2, n)
            if x == n - 1:
                print(f"Passed check in squaring loop (x^2 mod n = n-1). Base 'a' is not a witness.")
                break
        else:
            # If the loop completes without finding x = n - 1, then 'n' is composite
            print(f"Failed check in squaring loop. {n} is composite (witness: {a}).")
            return False  # n is composite (a is a strong witness)
    
    print(f"Passed {k} iterations. {n} is probably prime.")
    return True  # n is probably prime

# ----------------------------------------------------------------------

# Example Usage
print("Running tests...")

'''
# Test 1: A small prime number
test_number_1 = 821
print(f"\nTesting number: {test_number_1}")
result_1_school = is_prime_optimized_school(test_number_1)
print(f"Result (School Method): {test_number_1} is prime: {result_1_school}")
result_1_mr = miller_rabin_test(test_number_1)
print(f"Result (Miller-Rabin): {test_number_1} is prime: {result_1_mr}")

print("\n" + "="*50 + "\n")

# Test 2: A small composite number
test_number_2 = 2047
print(f"Testing number: {test_number_2}")
result_2_school = is_prime_optimized_school(test_number_2)
print(f"Result (School Method): {test_number_2} is prime: {result_2_school}")
result_2_mr = miller_rabin_test(test_number_2, k=5) # Reduced 'k' for a quicker example
print(f"Result (Miller-Rabin): {test_number_2} is prime: {result_2_mr}")
'''

for _ in range(1):
    print(f'\nTesting number: 2047')
    result_1_school = is_prime_optimized_school(2047)
    print(f'Result (School Method): 2047 is prime: {result_1_school}')
    result_1_mr = miller_rabin_test(2047)
    print(f'Result (Miller-Rabin): 2047 is prime: {result_1_mr}')
    print('\n' + '='*50)


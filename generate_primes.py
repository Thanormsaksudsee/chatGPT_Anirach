def generate_primes(n):
    # Initialize a list to keep track of prime numbers
    primes = []
    
    # Create a boolean list "is_prime" and initialize all elements as True
    is_prime = [True] * (n + 1)
    
    # Mark 0 and 1 as non-prime
    is_prime[0] = is_prime[1] = False
    
    p = 2
    while p * p <= n:
        # If is_prime[p] is not changed, it is a prime
        if is_prime[p] == True:
            # Update all multiples of p
            for i in range(p * p, n + 1, p):
                is_prime[i] = False
        p += 1
    
    # Collect prime numbers
    for i in range(2, n + 1):
        if is_prime[i]:
            primes.append(i)
    
    return primes

# Generate the first 1000 prime numbers
first_1000_primes = generate_primes(7919)  # 7919 is an arbitrary upper limit for the first 1000 primes

# Print the result
print(first_1000_primes)

def is_prime(num):
    if num < 2:
        return False
    for i in range(2, int(num**0.5) + 1):
        if num % i == 0:
            return False
    return True

def primes_generator(n):
    for i in range(2, n+1):
        if is_prime(i):
            yield i

# Ask user for input
n = int(input("Enter a number: "))

# Generate prime numbers less than or equal to n
primes = primes_generator(n)

# Print the generated prime numbers
print("Prime numbers less than or equal to", n, ":")
for prime in primes:
    print(prime)

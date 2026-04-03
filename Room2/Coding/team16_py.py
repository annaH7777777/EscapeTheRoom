def primes(numbers):
    def is_prime(n):
        if n < 2:
            return False
        for i in range(2, n):
            if n % i == 0:
                return False
        return True

    primes = []
    for num in numbers:
        if is_prime(num):
            primes.append(num)
    
    return primes
    

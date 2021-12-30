import itertools as it
from utils import PrimeGenerator, get_digits_from_num, get_num_from_digits

# generate digit list from num DONE
# generate permutations 

def generate_permutations(digits):
    permutations = list(it.product([0, 1], repeat=len(digits)))
    permutations = permutations[1:-1]
    return permutations

def is_valid_permutation(permutation, digits):
    filtered_digits = [i for idx, i in enumerate(digits) if not permutation[idx]]
    for idx in range(len(filtered_digits)):
        if filtered_digits[0] != filtered_digits[idx]: return False
    return True

def filter_valid_permutations(perms, digits):
    return [perm for perm in perms if is_valid_permutation(perm, digits)]

def replace_digits(perm, digits, replace_digit):
    perm_digits = [0]*len(digits)
    for idx in range(len(digits)):
        perm_digits[idx] = digits[idx] if perm[idx] else replace_digit
    
    return perm_digits

def count_prime(perm, digits, primes):
    start_digit = 1 if perm[0] == 0 else 0
    count = 0
    for replace_digit in range(start_digit, 10):
        perm_digits = replace_digits(perm, digits, replace_digit)
        perm_num = get_num_from_digits(perm_digits)
        if primes[perm_num]: count+=1
    
    return count


def replacement_primes(perms, digits, primes):
    max_prime_count = 0
    max_perm = None
    for perm in perms:
        count = count_prime(perm, digits, primes)
        if count > max_prime_count:
            max_prime_count = count
            max_perm = perm
    return max_prime_count, max_perm

def main():
    prime_generator = PrimeGenerator()
    max_num = 999999
    primes = prime_generator.generate_prime_list(max_num)
    max_prime_counts = [0]*len(primes)
    max_perm_dict = {}
    max_seen = 0
    for i in range(10, max_num):
        if not primes[i]: continue
        digits = get_digits_from_num(i)
        perms = generate_permutations(digits)
        perms = filter_valid_permutations(perms, digits)
        max_prime_count, max_perm = replacement_primes(perms, digits, primes)
        max_prime_counts[i] = max_prime_count
        max_perm_dict[i] = max_perm
        if max_prime_count>max_seen:
            print(i, max_seen)
            max_seen = max_prime_count
        
    return

if __name__ == "__main__":
    main()





def check_prime(n):
    """
    checks if a number is prime.
    NOTE: gives incorrect answer ONLY for 2
    """
    if n & 1 == 0:
        return False
    d = 3
    while d * d <= n:
        if n % d == 0:
            return False
        d = d + 2
    return True

def _order(num1, num2):
    # makes a bigger than b
    sum = num1+num2
    num1 = max(num1, num2)
    num2 = sum-num1
    return num1, num2

def factorize(n):
    """
    returns a list of tuple containing prime factor, power pairs 
    """
    factors_tuple = []
    power = 0
    while n%2 == 0:
        n = n/2
        power += 1
    if power: factors_tuple.append([2, power])
    factor=3
    while n!=1:
        power = 0
        while n%factor == 0:
            n = n/factor
            power += 1
        if power: factors_tuple.append([factor, power])
        factor += 2
    return factors_tuple

def get_num_from_factor(factors_tuple):
    output = 1
    for factor, power in factors_tuple: output = output * (factor**power)
    return output


def gcd(num1, num2):
    num1, num2 = _order(num1, num2)
    while num2:
        temp = num2
        num2 = num1%num2
        num1 = temp
    return num1

def factor_pow(factors, power):
    """
    n^power but operates on the factors instead 
    """
    for pair in factors:
        pair[1] = pair[1]*power
    return factors


class PrimeGenerator(object):
    def generate_prime_list(self, max_num):
        """
        returns an array P. P[n] = 1 if n is prime and P[n] = 0 if P is not prime
        """
        P = [-1]*(max_num+1)
        P[0], P[1] = 0, 0

        for i in range(2, max_num+1):
            if P[i]!=-1: continue
            P[i] = 1 if check_prime(i) else 0
            j = i+i
            while j < max_num+1:
                P[j] = 0
                j+=i
        P[2] = 1

        return P


def get_digits_from_num(n):
    digits = []
    while n:
        rem = n%10
        n = int(n/10)
        digits.append(rem)
    digits.reverse()
    return digits

def get_num_from_digits(digits):
    num = 0
    for digit in digits:
        num = num*10+digit
    return num


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



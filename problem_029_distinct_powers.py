import copy
from utils import factorize, factor_pow

def convert_factors_to_tuple(factors):
    output = []
    for factor in factors: output.append(tuple(factor))
    return tuple(output)

unique_factors_set = set()
for a in range(2, 101):
    # get prime representation of a
    factors = factorize(a)
    for b in range(2, 101):
        a_raise_b = factor_pow(copy.deepcopy(factors), b)
        unique_factors_set.add(convert_factors_to_tuple(a_raise_b))
    

print(len(unique_factors_set))
    
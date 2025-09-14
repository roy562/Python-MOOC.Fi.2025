# Write your solution to exercise 3 here
from fractions import Fraction


def fraction_calculator(calculation: str):
    
    if calculation.find(" + ") != -1:                       #Addition operation
       #print('addition')
       operands = calculation.split(" + ")
       frac1 = convert_to_fraction(operands[0])
       frac2 = convert_to_fraction(operands[1])
       sum = frac1+frac2
       #print(sum)
       return f"{sum.numerator}/{sum.denominator}"
    
    elif calculation.find(" - ") != -1:                     #Subtraction operation
        #print("subtraction")
        operands = calculation.split(" - ")
        frac1 = convert_to_fraction(operands[0])
        frac2 = convert_to_fraction(operands[1])
        diff = frac1-frac2
        #print(diff)
        return f"{diff.numerator}/{diff.denominator}"
    
    elif calculation.find(" * ") != -1:                     #Multiplication operation
        #print("multiplication")
        operands = calculation.split(" * ")
        frac1 = convert_to_fraction(operands[0])
        frac2 = convert_to_fraction(operands[1])
        product = frac1*frac2
        #print(product)
        return f"{product.numerator}/{product.denominator}"
    
    else:                                                   #Reduction operation
        #print("reduction")
        reduced = convert_to_fraction(calculation)
        return f"{reduced.numerator}/{reduced.denominator}"


def convert_to_fraction(fraction: str):
    return Fraction(fraction)

def fraction_test():
    calculation1 = "1/2 + 3/4"
    calculation2 = "1/2 - 1/3"
    calculation3 = "-1/2 * 1/4"
    to_be_reduced = "15/375"

    result_of_addition = fraction_calculator(calculation1)
    result_of_subtraction = fraction_calculator(calculation2)
    result_of_multiplication = fraction_calculator(calculation3)
    reduced = fraction_calculator(to_be_reduced)

    print(type(to_be_reduced))
    print(type(reduced))

    print(f'the sum of {calculation1} is', result_of_addition)
    print(f'the difference of {calculation2} is', result_of_subtraction)
    print(f'the product of {calculation3} is', result_of_multiplication)
    print(f'fraction {to_be_reduced} in reduced form is', reduced)

    # We'll calculate (1/2 + 3/4) * (1/2 - 1/3) using the results of the previous calculations
    calculation4 = f"{result_of_addition} * {result_of_subtraction}"
    print(fraction_calculator(calculation4))

#fraction_test()
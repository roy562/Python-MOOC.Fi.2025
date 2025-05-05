# Write your solution here
import fractions

def fractionate(number:int):
    fracs = []
    for i in range(1, number+1):
        fracs.append(fractions.Fraction(1,number))

    return fracs

def main():
    for p in fractionate(3):
        print(p)

    print()

    print(fractionate(5))

#main()
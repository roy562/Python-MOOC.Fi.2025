
def balanced_brackets(my_string: str):
    new_string = ""
    for char in my_string:
        if char in ['(',')','[',']']:
            new_string+=char

    if len(new_string) == 0:
        return True
    if not (new_string[0] == '(' and new_string[-1] == ')'):
        if not (new_string[0] == '[' and new_string[-1] == ']'):
            return False

    # remove first and last character
    return balanced_brackets(new_string[1:-1])

def test():
    ok = balanced_brackets("([([])])")
    print(ok)

    ok = balanced_brackets("(python version [3.7]) please use this one!")
    print(ok)

    # this is no good, the closing bracket doesn't match
    ok = balanced_brackets("(()]")
    print(ok)

    # different types of brackets are mismatched
    ok = balanced_brackets("([bad egg)]")
    print(ok)

      # different types of brackets are mismatched
    ok = balanced_brackets("((x)")
    print(ok)

#test()
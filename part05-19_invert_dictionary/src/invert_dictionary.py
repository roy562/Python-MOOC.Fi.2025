# Write your solution here
def invert(s:dict):
    for key in s.copy():
        value = s.pop(key)
        s[value] = key
        

if __name__ == "__main__":
    s = {1: "first", 2: "second", 3: "third", 4: "fourth"}
    invert(s)
    print(s)
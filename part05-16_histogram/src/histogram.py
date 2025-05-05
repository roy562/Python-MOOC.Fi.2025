# Write your solution here
def histogram(ip_string:str):
    dict = {}
    for char in ip_string:
        if char in dict:
            dict[char]+=1
        else:
            dict[char] = 1

    for key,value in dict.items():
        print(f"{key} {'*' * value}")

if __name__ == "__main__":
    histogram("abba")
    print()
    histogram("statistically")

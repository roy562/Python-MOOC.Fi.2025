# Write your solution here
# Write your solution here
def squared(text, size):
    full_text = ""
    if size == 1:
        print(text)
    else:
        while len(full_text) <= (size**2):
            full_text+=text
    
    i=1
    new_text=""

    while i<=size:
        print(full_text[0:size])
        full_text = full_text[size:] 
        i+=1

# Testing the function
if __name__ == "__main__":
    squared("aybabtu", 5)

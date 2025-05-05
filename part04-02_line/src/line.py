# Write your solution here
def line(times, text):
    if text == "":
        text = "*"
    
    first_char_of_text = text[0]
    print(first_char_of_text*times)

# You can test your function by calling it within the following block
if __name__ == "__main__":
    line(5, "x")
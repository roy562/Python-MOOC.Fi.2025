def line(times, text):
    if text == "":
        text = "*"
    print(text[0]*times)

def shape(width,tri_char,height,rect_char):
    i=1
    while i<=width:
        line(i,tri_char)
        i+=1
    j=1
    while j<=height:
        line(width,rect_char)
        j+=1

# You can test your function by calling it within the following block
if __name__ == "__main__":
    shape(3, ".", 0, ",")
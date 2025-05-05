# Write your solution here
word = input("Word:")
frame_length = 30
word_location_start = round((frame_length-len(word))/2)
word_location_end = word_location_start+len(word)

print("*" * frame_length)
print("*"+" " * (word_location_start-1) + word 
+ " " * (frame_length-1-word_location_end)+"*")
print("*" * frame_length)
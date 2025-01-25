# A spam comment is definted as a text containing following Keywords: 
# "make a lot of money" "buy now", "Subscribe this, "click this". 
# Write a program to detect these spams.

p1 = "Make a lot of money"
p2 = "buy now"  
p3 = "subscribe this"  
p4 = "click this"

message = input("Enter your comment: ")

if((p1 in message) or (p2 in message )or (p3 in message) or (p4 in message)):
    print("This comment is a spam")

else:
    print("This comment is not a spam")
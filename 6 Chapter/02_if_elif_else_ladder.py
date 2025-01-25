a = int(input("Enter your age: "))

# If elif else ladder
if(a<0):
    print("You are entering an invalid negative age")

elif(a==0):
    print("You are entering 0 which is not a valid age") 

elif(a>=18):
    print("You are eligible for consent")
    print("Good for you")

else:
    print("You are below the age of consent")

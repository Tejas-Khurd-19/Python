# Write a program to find out whether a given post is talking about "Tejas" or not..

post = input("Enter the post: ")

if("tejas" in post.lower()): # This means if Tejas in post is written in any form eg:- teJas, TEjas,
# It will get convert into tejas because of lower function 
#if("Tejas".lower() in post.lower()): also correct

    print("This post is talking about tejas")

else:
    print("This post is not talking about tejas")
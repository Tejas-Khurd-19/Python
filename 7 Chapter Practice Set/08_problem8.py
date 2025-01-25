# Write a program to print the following star pattern.
'''
for n = 4  
*
**
***
****
'''
n = int(input("Enter the number: "))
for i in range(1, n+1): 
    print("*"* i, end="")
    print("")
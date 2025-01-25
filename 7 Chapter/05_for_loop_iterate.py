## For Loop with Lists
l = [1, 4, 6, 234, 6, 764]
for i in l:
    print(i)

print("\n")

## For Loop with Tuples
t = (6, 231, 75, 122)
for i in t:
    print(i)

print("\n")

## For Loop with Strings
s = "Tejas"
for i in s:
    print(i)

print("\n")

# If you don’t want each character to be printed on a new line, 
# you can use the end parameter in the print() function to specify what should be printed after each character. 
# For example:
s = "Tejas"
for i in s:
    print(i, end="")
    # print(i, end=" ")


# The end parameter in the print() function specifies
#  what to print at the end of the output, 
# instead of the default newline (\n).
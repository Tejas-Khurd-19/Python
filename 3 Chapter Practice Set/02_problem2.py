# Write a program to fill in a letter template given below with name and date.

# letter = 111 Dear

# <I NAME 17,

# You are selected!

# <DATE> 

letter = '''Dear <|Name|>, 
You are selected! 
<|Date|> '''

l = (letter.replace("<|Name|>", "Tejas").replace("<|Date|", "24 September 2050"))
print(l)
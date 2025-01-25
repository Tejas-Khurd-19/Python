# Write a program to create a dictionary of Hindi words with values as their english translation. 
# Provide user with an option to look it up!

words = {
    "Madad": "Help",
    "Kursi": "Chair",
    "Billi": "Cat"
}

print("Enter the following word as it is; you want meaning of: ")
print("Madad")
print("Kursi")
print("Billi")

word_var = input("Enter the word you want meaning of: ")
print(words[word_var])
marks = {
    "Tejas": 100,
    "Shiva": 56,
    "Rohan": 23,
    0: "Harsh"
}

print(marks.items())
print(marks.keys())
print(marks.values())
marks.update({"Tejas": 99, "Renuka": 100})
print(marks)

print(marks.get("Tejas")) # Prints None
# print(marks["Tej"]) # Returns an error

# marks.get("Tejas")
# The get method retrieves the value for the specified key if it exists.
# If the key does not exist, it returns None (or a default value if you specify one, like marks.get("Tejas", default_value)).
# This is safer as it avoids raising an error when the key is missing.

# marks["Tejas"]
# This directly accesses the value for the key "Tejas".
# If the key does not exist, it raises a KeyError, which can crash your program if not handled properly.
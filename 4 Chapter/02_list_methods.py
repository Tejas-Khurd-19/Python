Mix = ["Apple", "Orange", 5, 345.06, False, "Tejas", "Rohan"]
print(Mix)
Mix.append("Banana")
print(Mix)

l1 = [1, 34, 62, 2, 6, 11]

# c = sorted(l1)
# print(c)  # This prints the sorted list
# print(l1)  # The original list remains unchanged

l1.sort()  # Sort the list
print(l1)  # Print sorted list


l1.reverse()  # Reverse the list
print(l1)  # Print reversed list

l1.insert(3, 333333)  # Insert 333333 at index 3
print(l1)  

value = l1.pop(3)  # Pop element at index 3
print(value) # Return the pop element and delete it

print(l1) # New list
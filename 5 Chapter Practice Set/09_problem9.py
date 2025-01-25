# Can you change the values inside a list which is Contained in Set s?
# s = 8, 7, 12, "Harry", [1, 2]}

# s = {8, 7, 12, "Tejas", [1,2]}

# s[4][0] = 9

# Since frozenset is immutable, you cannot modify it directly. However, you can remove the original frozenset from the set and replace it with a new one.
s = {8, 7, 12, "Tejas", frozenset([1, 2])} # frozenset() is a set which is fixwd

# To modify the frozenset, we remove it and add a new one:
s.remove(frozenset([1, 2]))
s.add(frozenset([3, 4]))

print(s)
# Actually, sets themselves are mutable in Python, which means you can modify the set by adding or removing elements. 
# However, the elements inside the set must be immutable (hashable).
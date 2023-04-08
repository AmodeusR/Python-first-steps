# Tuples

# Tuple values can't be changed

tuple_constructor = tuple(("Rick", 24, True))
number_tuple = (1, 2, 3, 4) 

print(tuple_constructor)
print(number_tuple)

newlist = list(tuple_constructor)
newlist.append("2548")
newtuple = tuple(newlist)
print(newtuple)

# Unpacking tuple

# Asterisk works similar to the javascript spread operator
# If the asterisk were in the middle value, the first and last would respectively get the first and last number of the tuple
(one, two, *others) = number_tuple

print(one, two, others)
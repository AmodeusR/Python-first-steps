# Sets

nums = {1, 2, 3, 4}
nums2 = set((1, 2, 3, 4))

# No duplicates are allowed

nums3 = {1, 2, 3, 3, 4}
print(nums3)

# Add value to set
nums.add(8)
print(nums)

# Add numbers from another set
morenums = {5, 6, 7}
nums.update(morenums)
print(nums)

# Update can be used with lists, tuples and dictionaries

# Merge two sets
a = {1, 2, 3, 4}
b = {3, 4, 5, 6}

union_set = a.union(b)
print(union_set)

# Keep duplicates
# a.intersection_update(b) updates a
duplicates = union_set.intersection(a, b)
print(duplicates)

# Keep differences
# a.difference_update(b) removes from "a", "b" numbers
differences = a.symmetric_difference(b)
print(differences)
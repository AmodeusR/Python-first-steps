# Just like an array
users = ["Rick", "John", "Sara"]

# Can hold multiple values
data = ["Rick", 42, True]

emptylist = []

# Check if value exists in array
print("Sara" in users)

print(users[0])
# It's possible to use negative index to count backwards
print(users[-1])
# Get index number of a value in an array
print(users.index("Sara"))

# Get values from x to y, being y not inclusive
print(users[0:2])
# Get values from x to end of array
print(users[1:])
# Can use negative index only
print(users[-3: -1])

# Get array length
print(len(users))

users.append("Nanoha")

print(users)

  # Ways to concatenate arrays

# users += ["Maria"]
users.extend(["Maria"])
# Insert can put a value in a specific position
users.insert(0, "Morty")
# It's possible to use indexes to do the same
users[2:2] = ["Sora", "Akane"]

# Change array value
users[4:5] = ["Hector"]
print(users)

  # Ways to remove value of an array

users.remove("Akane")

# users.pop() // Removes last value in an array and returns it
# del users[0]

# Removes all values from an array
print(data)
data.clear()
print(data)


# Others

# Sort array in alphabetical order
users.sort()

# Sort without considering lower or uppercase
# users.sort(key=str.lower)

nums = [5, 10, 75, 34, 1]
# It inverts the array order
# nums.reverse()
# print(nums)

# It sorts in descending order
# nums.sort(reverse=True)
# print(nums)

 # Immutable ways of doing the above

print(sorted(nums, reverse=True))

# Create copies of an array
numscopy = nums.copy()
numscopy2 = list(nums)
numscopy3 = nums[:]
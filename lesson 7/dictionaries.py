# Dictionaries
# Used to store data values that are in key/value pairs (essentially objects)

band = {
    "vocals": "Plant",
    "guitar": "Page"
}

band2 = dict(vocals="Plant", guitar="Page")

print(band)
print(band2)
print(type(band))
print(len(band))

# Access values
print(band["vocals"])
print(band.get("guitar"))

# Get dict keys or values
print(band.keys())
print(band.values())

# Like javascript Object.entries(), gets keys and values as a tuple
print(band.items())

"guitar" in band # True

# Change values
band["vocals"] = "Coverdale"
band.update({
    "bass": "JPJ"
})

print(band)

# Remove items
# band.pop("bass")
# del band["bass"]

# popitem removes the last item added and returns the removed value as a tuple
popped_item = band.popitem()
print(popped_item)
print(band)

band2.clear()
print(band2)
del band2 # Deletes dict

# Making copies

# band2 = band makes a reference, it doesn't copy

band2 = band.copy()
band3 = dict(band)


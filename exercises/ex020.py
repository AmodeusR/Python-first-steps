# Get user's input and randomly organize it
 
from random import shuffle

list: str = []

for i in range(4):
    user_input = input(f"Type the name of the {i + 1}º person: ")
    list.append(user_input)

shuffle(list)

print(f"The order of presentation will be the following:")
print(list)

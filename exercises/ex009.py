# Create a multiplication table from the user's input

user_number = int(input("Insert the number to create a multiplication table from: "))

print("-" * 12)
for i in range(10):
    table_number = i + 1
    justified_table_number = str(table_number).rjust(2, " ")
    print(f"{user_number} * {justified_table_number} = {user_number * table_number}")
print("-" * 12)


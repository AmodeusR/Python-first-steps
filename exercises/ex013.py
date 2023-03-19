# Make a 15% of salary readjustment in a worker's salary

worker_salary = float(input("Insert worker's salary: $"))

adjusted_salary = round(worker_salary + worker_salary * (15/100), 2)

print(f"The worker salary of ${worker_salary}, with a increase of 15%, will now earn ${adjusted_salary}")
# Determine the salary increase of a worker
# If it's a low salary, increase by a higher percentage

worker_salary = float(input("What's the worker salary?\n"))

if worker_salary <= 1250:
  print(f"His new salary will be R${round(worker_salary * 1.15, 2)}")
else:
  print(f"His new salary will be R${round(worker_salary * 1.1, 2)}")


def factorial_of(num):
  if num == 1:
    return 1
  
  return factorial_of(num - 1) * num

print("\nFactorial")
print(factorial_of(5))


def count_to_ten(num):
  if num > 9:
    print(num)
    return num + 1

  print(num)
  count = num + 1
  return count_to_ten(count)

print("\nCount")
count_to_ten(5)
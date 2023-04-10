count = 1

while count <= 6:
  if count == 5:
    count += 1
    continue # Jumps an iteration
    # break
  print(count)
  count += 1
else:
  print("Finished")
  # Else won't run if break is used


names = ["Maria", "Antonieta", "Leopoldo"]

for name in names:
  print(name)

for n in range(0, 51, 5):
  print(n)
else:
  print("Finished counting")
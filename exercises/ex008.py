# Convert meter measurement to the other metrics

meter = float(input("Insert a meter measurement: "))

print(f"{meter / 1000}km")
print(f"{meter / 100}hm")
print(f"{meter / 10}dam")
print(f"{round(meter * 10)}dm")
print(f"{round(meter * 100)}cm")
print(f"{round(meter * 1000)}mm")
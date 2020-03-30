

     # KEY : VALUE
cars={"colour":"red","Doors":"4"}

print(cars.keys())
print(cars.values())

print(cars)

for l in cars.items():
    print(l)


cars["wheels"]="4"

print(cars)

cars.pop("Doors")
print("After pop",cars)

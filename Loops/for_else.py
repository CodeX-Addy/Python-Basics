names = [("A", 12), ("B", 18), ("C", 19)]

for name, age in names:
    if age >= 18:
        print(f"{name} is eligible for voting..")
        break
else:
    print("No one is eligible")

## B is eligible for voting..

i = 1
while i < 6:
    print(i, end=" ")
    i += 1
print()
i = 1
while i < 6:
    print(i, end=" ")
    if i == 3:
        break
    i += 1

print()
i = 0
while i < 6:
    i += 1
    if i == 3:
        continue
    print(i, end=" ")
print()

i = 0
while i < 6:
    print(i, end=", ")
    i += 1
else:
    print("While loop terminated!")

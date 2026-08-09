## Reading a file

file = open("test.txt", "r")
print(file.read())

## Reading first few words

f1 = open("test.txt", "r")
print(f1.readline(5))

## Appending into the file
f2 = open("test.txt", "a")
f2.write("Another line")

f3 = open("test.txt", "r")
print(f3.read())

## To overwrite the file

f4 = open("test.txt", "w")
f4.write("Overwrited...")

f5 = open("test.txt", "r")
print(f5.read())

## NOTE: to open any file, appending something, behind the scenes, a dunder is called and which is __enter__() and closing calls __exit__()

## To create a new file

f6 = open("new_test.txt", "x")

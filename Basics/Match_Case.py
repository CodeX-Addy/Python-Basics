#The match case statement is introduced in new version of python
def table(n):
    for i in range(1, 11):
        print(n*i,end=" ")

a = int(input("Enter a number:"))
match a:
    case 1:
        print(table(1))
    case 2:
        print(table(2))
    case 3:
        print(table(3))
    case 4:
        print(table(4))
    case 5:
        print(table(5))
    case 6:
        print(table(6))
    case 7:
        print(table(7))
    case 8:
        print(table(8))
    case 9:
        print(table(9))
    case 10:
        print(table(10))
    case _:
        print("Enter number between 1 and 10")

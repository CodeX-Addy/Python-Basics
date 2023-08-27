try:
    a = int(input("Enter your number:"))
    print(a + 1)
except:
    print("Some error occured!!")
    
try:
    a = int(input("Enter your number:"))
    print(a + 1)
except Exception as ex:
    print("Some error occured due to",ex)
    # It'll give the reason for error


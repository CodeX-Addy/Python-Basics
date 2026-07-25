## pure function

def multiply_by_ten(num):
    return num * 10
    
mf = 20

## impure function -> not recommended
def add_by_twenty(num):
    global mf
    mf = 30
    num += mf
    return num
    
print(f"First func: {multiply_by_ten(10)}")
print(f"Second func: {add_by_twenty(20)}") 

#Local Scope
# A variable created inside a function is available inside that function
def myfunc():
  x = 300
  print(x)

myfunc()

#Global Scope
#A variable created outside of a function is global and can be used by anyone:
x = 300
def myfunc():
  print(x)
myfunc()
print(x)

#Naming variables
# The function will print the local x, and then the code will print the global x:
x = 300

def myfunc():
  x = 200
  print(x)

myfunc()

print(x)

#Global keyword
def myfunc():
  global x
  x = 300

myfunc()
print(x)

## Non local keyword demonstration:
## Non local limitation is to just look variable above the function like just above print_anything(), that's where global comes into the picture

def print_something():
    char = 'a'
    def print_anything():
        nonlocal char
        char = 'b'
    print_anything()
    print(f"The char value: {char}")
    
print_something()


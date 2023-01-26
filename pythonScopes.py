#Local Scope
# A variable created inside a function is available inside that function
def myfunc():
  x = 300
  print(x)

myfunc()

#Function inside function
# The local variable can be accessed from a function within the function
def myfunc():
  x = 300
  def myinnerfunc():
    print(x)
  myinnerfunc()

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


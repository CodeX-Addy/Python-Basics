Ex-
def func1():
	print(“Hello”)
  
func1()          #This is called function call

#Functions with arguments
def greet(name):
	gr = “Hello” + name
	return gr
a = greet(“python”) #“python” is passed to greet in name

# a will now contain “Hello World”

# Default Parameter Value
def greet(name=’stranger’):
	#function body
greet()                       #Name will be ‘stranger’ in function body(default)

greet(“Aditya”)        #Name will be “Aditya” in function body(passed)


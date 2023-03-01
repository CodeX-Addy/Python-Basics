Class Employee:		[classname is written in PascalCase]
	#methods & variables

#Class Attributes  
Class Employee:
	company = “Google” 	#Specific to each class
Aditya = Employee()	#Object instantiation
Aditya.company
Employee.company = “Github”	#changing class attribute

#Instance Attributes
print(“Hello World”)         # print is a function (more later)

harry.getSalary()

class Employee:
	company = “Google”
	def getSalary(self):
		print(“Salary is not there”)

#Static method
@staticmethod	#decorator to mark greet as a static method
def greet():
	print(“Hello user”)

#__init__() constructor
class Employee:
	def __init__(self,name):
		self.name = name
	def getSalary(self):
		#Some code…
harry = Employee(“Aditya”)	#Object can be instantiated using constructor like this!







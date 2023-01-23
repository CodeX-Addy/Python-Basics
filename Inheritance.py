#Syntax:
class Employee:	#Base Class
	#Code
class Programmer(Employee):	#Derived or child class
	#Code
  
# Super() method
super().__init__()  #Calls constructor of the base class

# Class methods
@classmethod
def (cls, p1, p2):
	#code
# @property decorators
class Employee:
	@property 
	def name(self):
		return self.ename

#   @.getters and @.setters
@name.setter
def name(self, value):
	self.ename = value

	
#Operator overloading in Python
p1 + p2 -> p1.__add__(p2)

p1 – p2 -> p1.__sub__(p2)

p1 * p2 -> p1.__mul__(p2)

p1 / p2 -> p1.__truediv__(p2)

p1 // p2 -> p1.__floordiv__(p2)

#Other dunder/magic methods in Python
__str__() -> used  to set what gets displayed upon calling str(obj)

__len__() -> used to set what gets displayed upon calling .__len__() or len(obj)










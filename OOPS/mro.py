## method resolution order

class A:
    label = "A class"
    
class B(A):
    label = "B class"
    
class C(A):
    label = "C class"
    
class D(B, C): ## it'll give preference from left to right, if C is present first, then C label will print
    pass

label_check = D()
print(label_check.label)
print(D.__mro__)

"""
B class
(<class '__main__.D'>, <class '__main__.B'>, <class '__main__.C'>, <class '__main__.A'>, <class 'object'>)
"""

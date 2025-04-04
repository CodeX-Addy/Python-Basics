for val in sequence:
    # statement(s)
    
languages = ['Swift', 'Python', 'Go', 'JavaScript']

# access items of a list using for loop
for language in languages:
    print(language)
# Output
# Swift
# Python
# Go
# JavaScript

#By using range function
# use of range() to define a range of values
values = range(4)

# iterate from i = 0 to i = 3
for i in values:
    print(i)
# Output
# 0
# 1
# 2
# 3
#Similarly if we write
for i in values:
    print(i,end='')
#Output:- 0 1 2 3


# For loop with else
digits = [0, 1, 5]

for i in digits:
    print(i)
else:
    print("No items left.")
# Output
# 0
# 1
# 5
# No items left.
 
# Printing sum of n 
num = int(input("Enter value of n:"))
sumofn = 0
for i in range(num+1):
    sumofn += i
print(sumofn)

# Printing product of n 
num = int(input("Enter value of n:"))
productofn = 1
for i in range(num+1):
    productofn *= i
print(productofn)

    

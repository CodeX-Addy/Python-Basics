# Python Lists are containers to store a set of values of any data type.
random = [‘Apple’, ‘Orange’, ‘table’, 7, False]

# List indexing
L1 = [7, 9, ‘python’]
L1[0] – 7
L1[1] – 9
L1[70] – Error
L1[0:2] – [7,9]         #(This is known as List Slicing)

#List methods
L1 = [1, 8, 7, 2, 21, 15]
sort() – updates the list to [1,2,7,8,15,21]
reverse() – updates the list to [15,21,2,7,8,1]
append(8) – adds 8 at the end of the list
insert(3,8) – This will add 8 at 3 index
pop(2) – It will delete the element at index 2 and return its value
remove(21) – It will remove 21 from the last
extend([2,3,4]) - It will extend the existing list as [1,8,7,2,21,15,2,3,4]

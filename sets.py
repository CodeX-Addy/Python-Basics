set = {'a', 'b', 'c', 'd', 'e'}
print(set)

set = {'a','a','b','b'}
print(set)
#Output :- {'a','b'}

s = {4, 5, 8, 6, 3, 2, 5}
key = 3
x = key in s # containment check
y = key not in s # non-containment check
print(x, y)
#Output - True False

s1 = {'t', 3, 6, 5, 7, 8, 4, 9}
s2 = {5, 7, 8, 9, 't', 4, 3, 6}

# equivalent check
x = s1 == s2

# non-equivalent check
y = s1 != s2
print(x)
print(y)
# Oputput- True
#          False

#Union and intersection of sets
a = {1,2,3}
b = {4,5,6}

print(a.union(b))
#Output :- {1,2,3,4,5,6}

print(a.intersection(b))
#Output:- set() which indicates the empty set

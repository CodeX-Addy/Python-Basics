## Dictionary is a collection of key-value pairs.
''' a = {“key”: “value”,
“python”: “code”,
“marks” : “100”,
“list”: [1,2,9]}
a[“key”]	# Prints value
a[“list”] 	# Prints [1,2,9] '''

## Various Dictionary Methods
a = {"name": "Aditya",
	"country": "India",
	"marks": [92,98,96]}

'''
items() : returns a list of (key,value) tuple.
keys() : returns a list containing dictionary's keys.
update({“friend”: “Max”}) : updates the dictionary with supplied key-value pairs.
get(“name”) : returns the value of the specified keys
clear() : Will clear the dictionary or returns the empty dictionary
'''

## Set is a collection of non-repetitive elements.
S= Set()        
S.add(1)
S.add(2)

# or Set = {1,2}

## Different Operations on a set
S = {1,8,2,3}

'''
len(s) : Returns 4, the length of the set
remove(8) : Updates the set S and removes 8 from S
pop() : Removes an arbitrary element from the set and returns the element removed.
clear() : Empties the set S
union({8, 11}) : Returns a new set with all items from both sets. #{1,8,2,3,11}
intersection({8, 11}) : Returns a set which contains only items in both sets. #{8}
'''
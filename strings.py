# STRING SLICING 
word = "amazing"
word[1:6:2]           # It will return ’mzn’

word = "amazing"
word[:7] or word[0:7]      #It will return ‘amazing’
word[0:] or word[0:7]      #It will return ‘amazing’

# STRING FUNCTIONS(COMMONLY USED)
## len() function : It returns the length of the string.

len("python")               #Returns 6

'''
endswith("on") : This function tells whether the variable string ends with the string “rry” or not. If string is “harry”, it returns for “rry” since harry ends with rry.

count("c") : It counts the total number of occurrences of any character.

capitalize() : This function capitalizes the first character of a given string.

find(word) : This function finds a word and returns the index of first occurrence of that word in the string.

replace(oldword, newword) : This function replaces the old word with the new word in the entire string.
'''

#ESCAPE SEQUENCE CHARACTERS
'''
Sequence of characters after backslash '\' [Escape Sequence Characters]
Escape Sequence Characters comprises of more than one character but represents one character when used within the string.
Examples: \n (new line), \t (tab), \' (single quote), \\ (backslash), etc.
'''
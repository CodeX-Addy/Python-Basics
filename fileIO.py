#Opening a file
open(“this.txt”, “r”)

#Reading a file in Python
f = open(“this.txt”, “r”)     #Opens the file in r mode

text = f.read()          #Read its content

print(text)     #Print its contents

f.close()         #Close the fie

f.read(2)       #Reads first 2 characters

f.readline()               #Reads one line from the file

#Writing files in python
f = open(“this.txt”, “w”)

f.write(“This is nice”)        #Can be called multiple times

f.close()

#With statement
with open(“this.txt”) as f:

            f.read()

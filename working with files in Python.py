f = open('input.txt', 'r')
f.readline()
f.readlines()
f.readlines()[2] # returns the third line of the file object f (don't forget that Python utilizes 0-based numbering!)

for line in f: print(line) # Using this loop, you can do anything you need with every line in the file

'Simple is\nbetter than\ncomplex.\n'.splitlines()

f = open('output.txt', 'w') # To save a file, output the desired file in write mode (if there is no such file, it will be created automatically)

f.write(string) # writes the contents of string to file f

# If you want to write something other than a string (an integer say), you must first convert it to a string by using the function str():
inscription = ['Rosalind Elsie Franklin ', 1920, 1958] s = str(inscription) f.write(s)

for i in inscription: output.write(str(i) + '\n')
# Adding \n to str(i) means that every item will start with a new line.

# When you are finished writing file, don't forget that you must close it using the command 
f.close() # It's a good habit to get into.
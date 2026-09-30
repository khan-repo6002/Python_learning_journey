# Strings
# Spillting and joining of String

Students = "John, Peter, Tom, Michael"
print(Students.split())

Students2 = "Andrew", "Henry", "Bradd", "George"
print(":".join(Students2))

# String Indexing
Word = "Environment"
print(len(Word))
print(Word[0])
print(Word[1])
print(Word[2])
print(Word[3])
print(Word[4])
print(Word[5])
print(Word[6])
print(Word[7])
print(Word[8])
print(Word[9])
print(Word[10])


#String Slicing
print(Word[:4])
print(Word[:9])
print(Word[-10:-1])

#String Functions/Methods

str = "I am practicing Python"
print(len(str))                            #finds the length of the string
print(str.endswith("on"))                  #It returns True/False based on argument
print(str.startswith("o"))                 #It returns True/False based on argument
print(str.upper())                         #returns the string in upper case
print(str.lower())                         #returns the string in lower case
print(str.strip())                         #returns the string in proper case
print(str.replace("practicing", "doing"))  #Returns the replaced value of the given string
print(str.__add__(" Course"))              #Adds substring
print(str.count("I"))                      #counts substring
print(str.find("practicing"))              #returns 1st index of 1st occurence
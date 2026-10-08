# #File I/O

file = open("Students.txt","w")
data = file.read()
print(data)
file.close

f = open("Day8.txt","r")
data = f.read(100)            #Passing an argument while reading will print no.of characters passed as argument
print(data)
f.close

# #WITH syntax

with open("Student.txt","w") as file:
    file.write("My name is Fardeen")
with open("Student.txt","r") as file:
    data1 = file.read()
    print(data1)

user_info = input("Enter the info:")
with open("Census.txt","w") as file:
    file.write(user_info)
with open("Census.txt", "r") as file:
    reading = file.read()
    print(user_info)

import os
if os.path.exists("Census.txt"):
    print("File already exist")
else:
    print("File not found")
    #OR
    with open("Census.txt","x") as file:     #by this we can create a new file, if the file given does not exist 
        file.read()
        

Salary = int(input("Enter you Salary: "))
with open("Designation.txt","w") as file:
    file.write("Salary")

with open("Designation.txt","r") as file:
    Mathew = file.read()
    print(Mathew)

os.remove("Designation.txt")

#DAYTEST

# Create a new file "practice.txt". Add the following data in it
# Hi Everyone
# we are learning File I/O
# using Java.
# I like programming in Java.

with open("practice.txt","w") as javafile:
    text = javafile.write("Hi Everyone \n we are learning File I/O \n using Java.\n I like programming in Java.")
    
#WAF that replaces all occurances of JAVA with PYTHON in above file

with open("practice.txt", "r") as jf:
    rea = jf.read()
    print(rea)

new_data = rea.replace("Java","Python")    #as the data is in string format we can use replace function of strings to replace it
print(new_data)

with open("practice.txt","w") as javafile:
    javafile.write(new_data)

#Search if the word "learning" exists in the file or not
with open("practice.txt", "r") as jf:
    rea = jf.read()
    if(rea.find("learning")):          #find() is a string method used to find the substrings
        print("word found")
    else:
        print("word not found")

    #OR

def find_a_word():
    word = "learning"
    with open("practice.txt", "r") as jf:
        rea = jf.read()
    if(word in rea):         
        print("word found")
    else:
        print("word not found")
        
find_a_word("learning")

# WAF to find in which line of the file does the wprd "learning" occur first. Print -1 if word not found

def check_for_line():
    word = "learning"
    data = True
    line_number = 1
    with open("practice.txt", "r") as jf:
        while data:
            data = jf.readline()
            if(word in data):
                print(line_number)
                return
            line_number += 1
    return -1

check_for_line()

#From a file containing numbers separated by comma, print the count of even numbers.

with open("Day8num.txt","r") as f:
    data = f.read()
    print(data)

num = ""
for i in range(len(data)):
    if(data[i] == ","):
        print(int(num))
        num = ""
    else:
        num += data[i]

#OR

with open("Day8num.txt","r") as f:
    data = f.read()
    print(data)
n = data.split(",")
print(n)
count = 0
for val in n:
    if ((int(val)) %2 == 0):
        count += 1

print(count)
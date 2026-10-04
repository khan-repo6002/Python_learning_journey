file = open("Students.txt","w")
data = file.read()
print(data)
file.close

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
        
os.remove("Census.txt")
print(file.tell("Census.txt"))


Salary = int(input("Enter you Salary: "))
with open("Designation.txt","w") as file:
    file.write("Salary")

with open("Designation.txt","r") as file:
    Mathew = file.read()
    print(Mathew)

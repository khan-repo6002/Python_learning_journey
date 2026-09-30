# #DICTIONARIES

null_dict = {}
null_dict["Name"] = "Fardeen"
print(null_dict)

# Nested Dictionary
student1 = {
    "name":"fardeen",
    "subjects":{
        "Hindi":91,
        "Telugu":71,
        "English":95,
        "Math":85,
        "Science":98,
        "Social":99}
}
print(student1)
print(student1["subjects"])                 #will print subjects
print(student1.get("Name"))                 #safely gets a value without throwing error
print(student1["subjects"]["Social"])       #will print marks of that particular subject which is defined in 2nd bracket
print(list(student1))
student1.update({"City": "Hyderabad"})      #it helps in updating a key value pair in the dictiionary
print(student1)
print(student1.keys())
print(student1.values())
print(student1.items())

#Dictionary using for loop

Employees = [{"Name":"Faisal","Age":22,"Designation":"Data Analyst","Salary":90000},
             {"Name":"Waseem","Age":23,"Designation":"Data Scientist","Salary":190000},
             {"Name":"Faizan","Age":20,"Designation":"Data Engineer","Salary":120000}]
for Employee in Employees:
    if Employee["Salary"] >=120000:
        print(Employee["Designation"])
    print(Employee["Name"])
    print(Employee["Age"])
    print(Employee["Salary"])
    print(Employee["Designation"])


 #Password format using while loop
# Password = ""
# while True:
#     if Password !="Fardeen":
#         Password = input("Enter the Password:")
#     print("access")
#     break

#Dictionary using while loop and password access

students = [{"Name": "Fardeen", "Age": 22, "Group":"Data Analytics", "Entrance Test":23},
            {"Name": "Waseem", "Age": 23, "Group":"Data Analytics", "Entrance Test":23},
             {"Name": "Faizan", "Age": 21, "Group":"Data Analytics", "Entrance Test":19},
             {"Name": "Shuja", "Age": 22, "Group":"Data Analytics", "Entrance Test":16},
             {"Name": "Abid", "Age": 23, "Group":"Data Analytics", "Entrance Test":20},
             {"Name": "Muzammil", "Age": 22, "Group":"Data Analytics", "Entrance Test":18},
             {"Name": "Rehan", "Age": 24, "Group":"Data Analytics", "Entrance Test":20},
             {"Name": "Ather", "Age": 22, "Group":"Data Analytics", "Entrance Test":21} ]

while True:
    password = input("Enter the Password: ")
    if password == "Fardeen6002":
        print("Access Granted")
        break;
    else:
        print("Enter correct password")

print(students)
for student in students:
    print(student.keys())              #prints keys' 
    print(student.items())              #prints items in the keys
    print(student.values())                 #prints all the values in tuple pairs
    
for student in students:
    if student["Entrance Test"] >=20:
        print(student["Name"],student["Age"], "years old.")
    else:
        print(student["Name"], "is not eligible.")


#SETS

s1 = {1,2,3,4,"hello","sets"}     #sets are also case sensitive
print(s1)
print(type(s1))

s2 = set()                        #Format of an empty set
s2.add(1)                           #it is used to add an element to the set
s2.add(3)
s2.add(6)
s2.add(3)
s2.add(2)
s2.add("Fardeen")
print(s2)
s2.remove("Fardeen")                #it is used to remove an element from the set
print(s2)
s2.add((1,2,7,9,4,6,3,0))
print(s2)
print(s2.pop())                       #It is used to pop random values from the set

s3 = {1,4,6,4,4,6,4,3,2,7,9,8,4}
s4 = {2,2,3,4,6,7,8,9,5,4,3,3,4,5,7}
print(f"The Union of s3 & s4:", s3.union(s4))                #It is used to perform union function of the sets
print(f"The Intersection of s3 & s4:", s3.intersection(s4))  #It is used to perform intersection funtion of the sets
print(f"The Difference of s3 & s4:",s3.difference(s4))       #It gives the difference between the sets
print(f"The Symmetric Difference of s3 & s4",s3.symmetric_difference(s4))   #It gives the symmetric difference of the sets

# #We can do the above program in a different way, which is shown below

Rank_1 = {1,2,3,4}
Rank_2 = {3,4,5,6}
print(Rank_1 | Rank_2)
print(Rank_1 & Rank_2)
print(Rank_1 - Rank_2)
print(Rank_2 - Rank_1)
print(Rank_1 ^ Rank_2)


# #DAYTEST

# Store the following word meanings in a python dictionary:
# table : "a piece of furniture", "list of facts and figures"
# cat : "a small animal"
# ubiquitous : "existing or seeming to exist everywhere at the same time

english_dict = { "Table":["a piece of furniture, list of facts and figures"],
                "Cat":"a small animal",
                "Ubiquitous":"existing or seeming to exist everywhere at the same time"
}
print(english_dict)

# WAP to enter marks of 3 subjects from the user and store them in a dictionary.
# Start with an empty dictionary & add one by one. Use subject name as key & marks as values

marks = {}
social_marks = int(input("Enter the social marks: "))
science_marks = int(input("Enter the science marks: "))
math_marks = int(input("Enter the math marks: "))
marks.update({"Social":social_marks})
marks.update({"Science":science_marks})
marks.update({"Math" :math_marks})
print(marks)

'''You're given a list of subjects for students. Assume that one classroom is required for 1 subjects.
How many classroom are needed by all students:"python","java","c++","python","javascript","java","python","java",
"c++","c","R","Golang","R"'''

subjects = {"python","java","c++","python","javascript","java","python","java","c++","c","R","Golang","R"}
print(len(subjects))
print(subjects)

# Figure out a way to store 9 & 9.0 as separate values in the set.(You can take help of built in data types)

value = {9,"9.0"}           #if same number is given to be shown in 2 different values, then one number should be in a string format
print(value)
 #or

value2 = {("Float", 9.0),
          ("int", 9)
}
print(value2)
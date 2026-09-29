# Conditional Statements

age = int(input("Enter your age:"))
print(f"The student's age is {age}")  #f strings are used to embed expressions and variables directly inside a string
if(age>=18):
    print("Student is an adult")
else :
    print ("Student is a minor")


#Awarding grades

marks_scored = int(input("Enter your Marks: "))
if(marks_scored >= 90 and marks_scored <=100):
    print("Grade A+")
elif(marks_scored >=80 and marks_scored <=90):
    print("Grade A")
elif(marks_scored >=70 and marks_scored <=80):
    print("Grade B")
elif(marks_scored >= 60 and marks_scored <=70):
    print("Grade C")
elif(marks_scored >= 50 and marks_scored <=60):
    print("Grade D")
elif(marks_scored >= 40 and marks_scored <=50):
    print("Grade E")
else:
    print("Grade F")


#Check if the number is positive or negative

number = int(input("Enter the number: "))
if(number>0):
    print("Number is positive")
elif(number<0):
    print("Number is negative")
else :
    print("Number is zero")

#check whether the number is even or odd

number1 = int(input("Enter the Number ="))
if(number1 %2==0):
    print("The Number is Even")
else:
    print("The Number is Odd")

#Checking which number is greatest

x = int(input("Enter the number x: "))
y = int(input("Enter the number y: "))
z = int(input("Enter the number z: "))
if(x >= y and x >= z):
    print("The Number x is greater",x)
elif(y >= x and y>= z):
    print("The Number y is greater",y)
else:
    print("The Number z is greater",z)

#To check whether the number is a multiple of 7
a = int(input("Enter the Number: "))
if(a %7 == 0):
    print("The number is a multiple of 7")
else:
    print("The number is not a multiple of 7")
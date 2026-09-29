"""Learning Python for Data Analytics"""

#Data Types
#1. Integers(int) = whole numbers | Eg: 8,4,25,24,21 etc
#2. Strings(str) = characters enclosed in quotation marks | Eg: "John","25"
#3. Float(float) = Decimal numbers | Eg: 8.4,24.135
#4. Boolean(bool) = True or False | Eg: True

#You can check the data type with the help of 'type()' function.
# name = "tom"
# print(type(name))

# #Type Casting
# #It is a method of changing the data type of a data to another
# a = 31
# print(str(a))
# print(float(a))

#Operators in Python
#1. Arithmetic Operators (+,-,*,**,/,//,%)
#2. Assingment Operators (=,+=,-=)
#3. Comparison Operators (==,>=,<=,!=,<,>)
#4. Logical Operators (and, or, not)


print("---------Arithmetic Operations----------")
x = int(input("\nEnter number1: "))    #input is a function by using which a variable can be derived by the end-user
y = int(input("\nEnter number2:"))
add =  x+y
subtract = x-y
multiply = x*y
divide =  x/y
floor_division = x//y
power = x**y
Modulus = x%y
Operations = [add, subtract, multiply, divide, floor_division, power]
print(Operations)


#Comparative Operators        It will return output in boolean form(true/false)
p = 10
print(p==10)
print(p<10)
print(p>9)
print(p!=9)
print(p<=11)
print(p>=8)
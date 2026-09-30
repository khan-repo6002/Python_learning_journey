# Functions
# Addition
def addition(a,b):
    {print("Addition=",a+b)}
print(addition(4,4))

# addition with return function
def add1(x,y):
    return x+y
result = add1(5,5)
print(result)

# Addition where arguments are defined while function is being written
def add2(a=3,b=4):
    print(a+b)
    return(a+b)
add2()

def add3(a,b=3):            #Here, default argument is given first. If writing a function like this always write non-default argument later
    print(a+b)
    return(a+b)
add3(1)


# Subtraction
def sub1(p,x):
    return p-x
result = sub1(11,8)
print(result)

# Multiplication
def mult(a,z):
    return a*z
result = mult(83,33)
print(result)

# Simple Division
def div(a,d):
    return a/d
result = div(78,9)
print(result)

# Floor Division
def div2(a,k):
    return a//k
result = div2(89,32)
print(result)

# Power
def pow(s,d):
    return s**d
result = pow(2,8)
print(result)

# Modulus
def mod(d,f):
    return d%f
result = mod(89,32)
print(result)



def greet_user(name="Guest"):
    return f"Hello {name}!"
print(greet_user("Faisal"))

# DAYTEST

# WAP to create a function calculating average of 5 numbers
def average(a,b,c,d,e):
    sum = a+b+c+d+e
    avg = sum/5
    print(avg)
    return avg

average(3,4,2,5,4)

# WAF to print the length of a list(list is the parameter)

city = ["Hyderabad","Delhi","Mumbai","Chennai","Pune","Kolkatta"]

def print_len(list):
    print(len(list))
    return(len(list))
print_len(city)

#WAF to print the length of a tuple(tuple is the parameter)

marks = (89,93,39,49,98,99,90)
def print_tup(tuple):
    print(len(tuple))
    return(len(tuple))
print_tup(marks)

#WAF to print the elements of a list in a single line

country = ["India","USA","Australia","UK","Saudi Arabia","UAE"]
def print_list(list):
    for items in list:
        print(list,end=";")

print_list(country)
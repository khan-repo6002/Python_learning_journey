# loops
#while loop
count = 1
while count <=10:
    print("Faisal",count)
    count = count +1
print(count)

#Printing numbers from 1-10 using while loop
i = 1
while i <=10:
    print(i)
    i += 1

#Printing vise versa of the above condition
i = 10
while i >=1:
    print(i)
    i = i - 1

#printing range 1-15 using break keyword
i = 1
while i <= 15:
    print(i)
    if(i == 8):
        break
    i += 1

#priting range 1-10 using continue
i = 1
while i <= 10:
    if(i == 8):
        i += 1
        continue
    print(i)
    i += 1

#Priting odd numbers from 1-50 using while loop & if
i = 0
while i <= 50:
    if(i%2 == 0):
        i += 1
        continue
    print(i)
    i += 1

##Priting even numbers from 1-50 using while loop & if
i = 0
while i <= 50:
    if(i%2 != 0):
        i += 1
        continue
    print(i)
    i += 1

#For Loop

for (i) in range(5):
    {
    print("hello world"),
    print(i)
    }

for (i) in range(1,5,2):
    {
    print("hello world"),
    print(i)
    }

CGC = ["TDC","ASDC","PZC","MTC"]
for i in CGC:
    print(i)


#printing numbers from 1 to 100 using for loop
for i in range(1,101):
    print(i)

# #priting odd numbers using for loop and if statement
for i in range(1,100):
    if i%2 !=0:
        print(i)

# #printing odd numbers using for loop only
for i in range(1,100,2):
    print(i)

# #printing multiplication table using for loop 
for i in range(1,11):
    print("2 x",i,"=",2*i)
for i in range(1,11):
    print("3 x",i,"=",3*i)
for i in range(1,11):
    print("4 x",i,"=",4*i)
for i in range(1,11):
    print("5 x",i,"=",5*i)
for i in range(1,11):
    print("6 x",i,"=",6*i)
for i in range(1,11):
    print("7 x",i,"=",7*i)
for i in range(1,11):
    print("8 x",i,"=",8*i)
for i in range(1,11):
    print("9 x",i,"=",9*i)
for i in range(1,11):
    print("10 x",i,"=",10*i)


# #printing sum of numbers from 0 to 10
sum = 0
for i in range(1,11):
    sum = sum + i
print(sum)

#subtracting
sub = 10
for i in range(10,1):
    sub = sub - i
print(sub)

#printing avaerage using a list
List1 = [1,2,3,4,5,6,7,8,9,10]
sum = 0 
for i in List1:
    sum = sum + i 
print("Sum of the list:", sum)
lenght_of_the_list = len(List1)
print("Lenght of the list:",lenght_of_the_list)
average = sum/lenght_of_the_list
print("Average of the list is", average)


#DAYTEST

#Print numbers from 1-100
i = 1
while i <= 100:
    print(i)
    i += 1

#Print numbers from 100-1
i = 100
while i >=1:
    print(i)
    i = i - 1

#Print multiplication table of number n
n = int(input("Enter the number: "))
i = 1
while i <=10:
    print(n*i)
    i +=1

#Print the elements of a list using a loop

L1 = [1,4,9,16,25,36,49,64,81,100]
index = 0
while index < len(L1):
    print(L1[index])
    index +=1

L2 = ["Kingdom of Solomon","Epytian Kingdom","Rashidoon Caliphate","Ummayid Caliphate","Mughal Empire","Roman Empire","Osmania Sultanate","Asaf Jahi Dynasty","Maurya Empire","British Empire","Mongolian Empire","Byzantine Empire"]
index = 0
while index < len(L2):
    print(L2[index])
    index +=1

"""Search for a number x in the following loop:
(1,4,16,25,36,49,64,81,100)"""
T1 = (1,4,16,25,36,49,64,81,100)
i = 0            #This step is also known as initialization
x = 36
while i < len(T1):
    if(T1[i] == x):
        print("x found at index", i)
        break
    i += 1 
print("End of loop")

#WAP to find the sum of the n natural numbers using while loop
sum = 0
while i <= 10:
    sum += 1
    i += 1
    print(f"Total sum = ",{sum})

"""Print the elements of the list using for loop:
[1,4,9,16,25,36,49,64,81,100]"""
squares = [1,4,9,16,25,36,49,64,81,100]
for i in squares:
    print(i)

"""Search for a number x in the following loop:
(1,4,16,25,36,49,64,81,100)"""
sq1 = (1,4,9,16,25,36,49,64,81,100)
x = 64
idx = 0
for i in sq1:
    if(i == x):
        print("x found at index", idx)
        
    idx += 1


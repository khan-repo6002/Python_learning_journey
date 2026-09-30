#Lists
data_analytics = ["Python", "SQL", "Microsoft Excel", "Power BI"]

#list indexing
print(data_analytics[0])
print(data_analytics[1])
print(data_analytics[2])
print(data_analytics[3])
print(data_analytics[-1])
print(data_analytics[-2])
print(data_analytics[-3])
print(data_analytics[-4])
print(data_analytics[1:3])
print(data_analytics[:3])
print(data_analytics[0:])
print(data_analytics[0:4:2])

# #List Functions/Methods
data_analytics.append("Tableau")           #Adds an item to the end of the list
print(data_analytics)                      
data_analytics.remove("Power BI")          #Removes the first occurance of the value
print(data_analytics)
data_analytics.sort()                      #Sorts the list in ascending order
print(data_analytics)
data_analytics.reverse()                   #Sorts the list in descending order
print(data_analytics)
data_analytics.insert(3,"Tableau")         #Insert an item at specific position
print(data_analytics)


#Tuples
tup = ()                                   #Empty tuple
tup1 = (1,)                                #single element tuple is written using a trailing comma at the end
colors = "red","green","blue","yellow"     #a tuple without () is called tuple packing
tup2 = (2,3,5,89,90,32,423,30)
print(tup2)
print(tup2.count())
point = (10,20)
x,y = point
print(x)
print(y)


#DAYTEST

#WAP to ask the user to enter the names of their 3 fav movies & store them in a list

mov1 = input("Enter the 1st Movie: ")
mov2 = input("Enter the 2nd Movie: ")
mov3 = input("Enter the 3rd Movie: ")

L1 = [mov1,mov2,mov3]
print(L1)

#OR a second method
L2 = []
mov4 = input("Enter the 4th Movie: ")
mov5 = input("Enter the 5th Movie: ")
mov6 = input("Enter the 6th Movie: ")

L2.append(mov4)
L2.append(mov5)
L2.append(mov6)
print(L2)

#OR a shortest form
L3 = []
L3.append(input("Enter the 7th Movie: "))
L3.append(input("Enter the 8th Movie: "))
L3.append(input("Enter the 9th Movie: "))
print(L3)

#WAP to check if a list contains a palindrome of elements.(Hint: use copy() method)
L4 = [1,2,1,2,1,2,1,2,1,2,1,2,1]
copy_of_L4 = L4.copy()
copy_of_L4.reverse()

if(copy_of_L4 == L4):
    print("It is a Palindrome")
else:
    print("Not a Palindrome")

#WAP to count the no.of students with the Grade "A" in the following tuple
grades = ("A","C","D","A","B","B","D","A","C","D","A",)
print(grades)
print(grades.count("A")) 

#Store the above values in a list & sort them from A - D
grades1 = ["A","C","D","A","B","B","D","A","C","D","A"]
grades1.sort()
print(grades1)


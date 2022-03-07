print("ASSIGNMENT 1")


###  1. Write a Python program to find average of three numbers entered by the user.  ###

print(" 1. Write a Python program to find average of three numbers entered by the user.")

### input three numbers ###
a=float(input("Enter first number : "))
b=float(input("Enter second number : "))
c=float(input("Enter third number : "))

### average of three numbers ###
avg=(a+b+c)/3

print("Average : ",avg)



###  2. Write a python program to compute a person's income tax. ###

print(" 2. Write a python program to compute a person's income tax. ")

### inputs from user ###
gross_income = float(input("Enter the Gross Income to the nearest penny : "))
dependents = int(input("Enter the number of Dependents : "))

### calculation of tax ###
Taxable_income = gross_income - 10000 - (3000*dependents)
Tax=(Taxable_income*20)/100

if Tax<0:
    print("Your income tax is 0$")
else:
    print(Tax)
    


####  3. Write a python program to store different data type values into a list. ####

print("3. Write a python program to store different data type values into a list.")

### input from user ###
SID=int(input("Enter your SID : "))
name=input("Enter your name : ")
gender=input("Enter your Gender-(M,F,U) :  ")
course=input("Enter the course name : ")
CGPA=float(input("Enter the CGPA : "))

Student=[SID,name,gender,course,CGPA]

print(Student)




####  4. Write a python program to enter marks of 5 students into a list and display them in sorted manner.####

print("4. Write a python program to enter marks of 5 students into a list and display them in sorted manner.")

### inputs from user ###
a=float(input("Enter the marks in subject 1 = "))
b=float(input("Enter the marks in subject 2 = "))
c=float(input("Enter the marks in subject 3 = "))
d=float(input("Enter the marks in subject 4 = "))
e=float(input("Enter the marks in subject 5 = "))

Marks=[a,b,c,d,e]
Marks.sort()
print(Marks)




#### 5. a) List: color ['Red', 'Green', 'White', 'Black', 'Pink', 'Yellow'] ####
print("5. a) List: color ['Red', 'Green', 'White', 'Black', 'Pink', 'Yellow']")

color=['Red', 'Green', 'White', 'Black', 'Pink', 'Yellow']
color.remove('Black')
print(color)



#### 5. b) List: color ['Red', 'Green', 'White', 'Black', 'Pink', 'Yellow'] ####
print("5. b) List: color ['Red', 'Green', 'White', 'Black', 'Pink', 'Yellow']")

color=['Red', 'Green', 'White', 'Black', 'Pink', 'Yellow']
color[3:5]=["Purple"]
print(color)

print("ASSIGNMENT 2")

print(" Q1 For a given input string “Python is a case sensitive language”. Write python code for the following")

###input from the user ###
      
input_str = "Python is a case sensitive language"
print("(a)\tThe length of the given string is : %s" % len(input_str))

###reverse string creation ###      
reversed_str = input_str[ : : -1 ]                                                                         
print("(b)\tThe string in reverse would be : %s" % reversed_str)

###creation of new string ###      
new_str = input_str[10:26]                                                                                               
print("(c)\tThe new string becomes : %s" % new_str)

###replacing value and formation of duplicate input ###      
dup_input_str = input_str.replace("a case sensitive", "object oriented")                                    
print("(d)\tThe replaced substring will be : %s" % dup_input_str)
substr = "a"
indx = input_str.find(substr)                                                                               
if indx == -1:
    print("(e)\tThe given substring was not found in the inputted string")
else:
    print("(e)\tThe first occurence of the given substring \"%s\" is at index no. = %d" % (substr, indx))

###removal of white spaces ###
no_white_spaces_str=input_str.replace(" ","")                                                               
print("(f)\tThe inputted strings with no white spaces will be \"%s\"\n" % no_white_spaces_str)



print(" Q2 Store your name, SID, department name and CGPA into different variables. With the help of String formatting print the following output")

###storing data ###
name='Sugam Arora'
SID=21105021
department='ECE'
CGPA=9.9
print("Hey, %s Here! \nMy SID is %d \nI am from %s department and my CGPA is %f." % (name, SID, department, CGPA), end='\n')


print(" Q3 For a=56 and b=10 with the help of bitwise operators calculate the following")

### assigning values  ###
a=56
b=10
###calculation  ###
print("a.\a & b= ", (a & b))
print("b.\a | b= ", (a | b))
print("c.\a ^ b= ", (a ^ b))
print("d.\Left shift both a and b with 2 bits : a= ",a<<2, "b= ", b<<2)
print("e.\Right shift a with 2 bits and b with 4 bits : a= ", a>>2, "b= ", b>>4)



print(" Q4 Write a python program to find the greatest of three numbers entered by the user.")

### input from user  ###

a = int(input("Enter 1st number : "))
b = int(input("Enter 2nd number : "))
c = int(input("Enter 3rd number : "))

### greatest number  ###
if a > b:
    if a > c:
        greatest_number = a
    else:
        greatest_number = c

if b > a:
    if b > c:
        greatest_number = b
    else:
        greatest_number = c


print("Greatest number = " ,greatest_number)



print(" Q5 Write a python program to check if the word “name” is present in the string entered by the user (Print : “Yes” or “No”).")




input_string = input("Enter input string : ")

if "name" in input_string:
    print("Yes")
else:
    print("No")



print(" Q6 For any three lengths, there is a simple test to see if it is possible to form a triangle. If any of the three lengths is greater than the sum of the other two,then you cannot form a triangle. Otherwise, Enter three sides of a triangle, converts them to integers, and to check whether the given input lengths can form a triangle or not (Print : “Yes” or “No”) ")

      
### input from user  ###
a = int(input("Enter 1st length : ")) 
b = int(input("Enter 2nd length : "))
c = int(input("Enter 3rd length : "))
 
if a+b > c and a+c > b and b+c > a:
    print("Yes")
else:
    print("No")
    


























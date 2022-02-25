

print("ASSIGNMENT 4")

print("\n Q1Write a recursive python function to solve the problem of tower of Hanoi with three disks.\n")

#define tower of hanoi
def tower_of_hanoi(n , source, destination, auxiliary):
    step_number=1
    if n==1:
        print ("Move disk 1 from",source,"to",destination)
        return
    tower_of_hanoi(n-1, source, auxiliary, destination)
    print ("Move disk",n,"from",source,"to",destination)
    tower_of_hanoi(n-1, auxiliary, destination, source)
#input from user
no_of_disk=int(input("Enter number of disk in tower of Hanoi:"))
print("\nThe Disks are numbered starting from top of the tower."
      "\nSteps to move all disks from Source Tower to Destination Tower "
      "is given below:\n")
tower_of_hanoi(no_of_disk,"Source Tower","Destination","Auxiliary")


print("\n Q2 Write a python program to print the Pascal’s triangle for n number of rows given by the user using both recursive and iterative procedures (for/while loop).")
#input rows from user
row=int(input("Enter number of rows:"))

if row<=16:
      def psum(list1, row):
        i1 = 0
        i2 = 1
        l = []
        for i1 in range(row - 1):
            l.append(list1[i1] + list1[i2])
            i1 = i1 + 1
            i2 = i2 + 1
        l.insert(0, 1)
        l.append(1)
        return (l)

    #formation of a new function
    def ptriangle(rows):
        if rows == 1 :
            print(1) 
        elif rows == 2 :
            print(f" 1\n1 1")
        else:
            f = "{p:^90}".format(p=1)
            print(f)
            f = "{p:^90}".format(p="1  1")
            print(f)
            l1 = [1, 1]
            row = 2
            for i in range(rows - 2):
                v = psum(l1, row)
                v2 = v.copy()
                v2 = list(map(str, v2))
                n = rows
                k = "  ".join(v2)
                f = "{p:^90}".format(p=k)
                print(f)
                row = row + 1
                l1 = v
    ptriangle(row)
#for row>16 
elif row>16 and row<=20:
    def psum(list1, row):
        i1 = 0
        i2 = 1
        l = []
        for i1 in range(row - 1):
            l.append(list1[i1] + list1[i2])
            i1 = i1 + 1
            i2 = i2 + 1
        l.insert(0, 1)
        l.append(1)
        return (l)


    def ptriangle(rows):
        if rows == 1:
            print(1)
        elif rows == 2:
            print(f" 1\n1 1")
        else:
            f = "{p:^120}".format(p=1)
            print(f)
            f = "{p:^120}".format(p="1  1")
            print(f)
            l1 = [1, 1]
            row = 2
            for i in range(rows - 2):
                v = psum(l1, row)
                v2 = v.copy()
                v2 = list(map(str, v2))
                n = rows
                k = "  ".join(v2)
                f = "{p:^120}".format(p=k)
                print(f)
                row = row + 1
                l1 = v
    ptriangle(row)
# row>20 
elif row>20 and row<=30:
    def psum(list1, row):
        i1 = 0
        i2 = 1
        l = []
        for i1 in range(row - 1):
            l.append(list1[i1] + list1[i2])
            i1 = i1 + 1
            i2 = i2 + 1
        l.insert(0, 1)
        l.append(1)
        return (l)


    def ptriangle(rows):
        if rows == 1:
            print(1)
        elif rows == 2:
            print(f" 1\n1 1")
        else:
            f = "{p:^240}".format(p=1)
            print(f)
            f = "{p:^240}".format(p="1  1")
            print(f)
            l1 = [1, 1]
            row = 2
            for i in range(rows - 2):
                v = psum(l1, row)
                v2 = v.copy()
                v2 = list(map(str, v2))
                n = rows
                k = "  ".join(v2)
                f = "{p:^240}".format(p=k)
                print(f)
                row = row + 1
                l1 = v
    ptriangle(row)
#for large row value
else:
    def psum(list1, row):
        i1 = 0
        i2 = 1
        l = []
        for i1 in range(row - 1):
            l.append(list1[i1] + list1[i2])
            i1 = i1 + 1
            i2 = i2 + 1
        l.insert(0, 1)
        l.append(1)
        return (l)


    def ptriangle(rows):
        if rows == 1:
            print(1)
        elif rows == 2:
            print(f" 1\n1 1")
        else:
            f = "{p:^700}".format(p=1)
            print(f)
            f = "{p:^700}".format(p="1  1")
            print(f)
            l1 = [1, 1]
            row = 2
            for i in range(rows - 2):
                v = psum(l1, row)
                v2 = v.copy()
                v2 = list(map(str, v2))
                n = rows
                k = "  ".join(v2)
                f = "{p:^700}".format(p=k)
                print(f)
                row = row + 1
                l1 = v
    ptriangle(row)


    
print("\n Q3 Input two integer values from user, calculate and print the quotient and reminder obtained from the two values")

#input from the user
n1=int(input("\nEnter an Integer:"))
n2=int(input("Enter another Integer:"))

def q_and_r_finder(x,y):
    quotient = (x // y)
    remainder = (x % y)
    return quotient,remainder

list1=list(q_and_r_finder(n1,n2))

q=list1[0]

r=list1[1]
#printing the quotient and remainder
print(f"\nThe quotient when {n1} is divided by {n2} is {q}.")
print(f"The remainder when {n1} is divided by {n2} is {r}.")

#Q3.a
print("\nQue3.a")
c1=callable(q_and_r_finder)
c2=callable(n1)
c3=callable(n2)
if c1==True:
    print(f"Function is callable")
if c1==False:
    print(f"Function is Not-callable")
if c2==True:
    print(f"{n1} is callable")
if c2==False:
    print(f"{n1} is Not-callable")
if c3==True:
    print(f"{n2} is callable")
if c3==False:
    print(f"{n2} is Not-callable")
#Q3.b
print("\nQue3.b")
#list of values
listv=[q,r]
zero=False
if zero in listv:
    zero=True
else:
    zero=False
if zero==True:
    print("All result values are NOT 'non-zero'")
elif zero==False:
    print("All result values are 'non-zero'")
#Q3.c
print("\nQue3.c")
#new values of list
listr=[q,r]
for i in range (4,7):
    listr.append(i)
listv2=[]
#adding number > 4 from listr to listv2
for i in listr:
    if i>4:
        listv2.append(i)
#a new list listv3 with same elements as listv2 but in string form
listv3=list(map(str,listv2))
#Using join
v=",".join(listv3)
print(f"Values greater than 4 is {v}")
#Q3.d
print("\nQue3.d")
set1={1,2}
set1.clear()
#adding above result in set datatype
for el in listv2:
    set1.add(el)
print("Above result in set form is shown below:")
print(set1)
#Q3.e
print("\nQue3.e")
#Making set1 immutable
frozenset(set1)
print("The above set has been converted to immutable.")
#Q3.f
print("\nQue3.f")
print(f"Max value from set is {max(set1)}")
#using hash function
hash_value=hash(max(set1))
print(f"Hash value of {max(set1)} is {hash_value}")




print("\n Q4 Create a class named Student, use the_init_() function to assign values for name and roll number. And also call _del_() function to destroy object that is created.\n")

class student:
    #using constructor to create class objects
    def __init__(self,name,roll_no):
        self.name=name
        self.roll_no=roll_no
    #defing print function
    def pfun(self):
        print(f"Hello, My name is {self.name} and my "
              f"roll no. is {self.roll_no}")
    #calling destructor
    def __del__(self):
        print("Destructor Called")
        
sugam=student("SUGAM ARORA",21105021)
sugam.pfun()
del sugam



print("\n Q5 Write a program to store details of three employees: name and salary using class.\n")

class employees:
    #Using constructor to for class objects
    def __init__(self,name,salary):
        self.name=name
        self.salary=salary
    def pfun(self):
        print(f"Employee Name is {self.name} and Salary is {self.salary} ")
#emp_n name and salaray
emp_1=employees("Mehak",40000)
emp_2=employees("Ashok",50000)
emp_3=employees("Viren",60000)
#print employee detail
emp_1.pfun()
emp_2.pfun()
emp_3.pfun()
#Updating salary of Mehak to 70000
print("\nQue.5a")
emp_1.salary=70000
print("Mehak salary Updated to 70000")
emp_1.pfun()
#Deleting Viren's data
print("\nQue.5b")
del emp_3
print("Employee Viren's data has been removed.")



print("\n Q6 Barbie and George are the two friends. On Saturday, they decided to travel to a fair where they discovered a fun game that put their friendship to the test. The test required George to utter a word and Barbie to create a new meaningful word using the exact same letters as George. If Barbie fails to form a word then their friendship is a fake.Can you assist the shopkeeper by writing a piece of code for him to use so that the test runs smoothly?")

gap=" "*10
print(f"\n{gap}WELCOME TO THE FRIENDSHIP GAME")
#definig principle of game i.e. anagram
def anagram(word1,word2):
    #converting all letters to lowercase
    word1=word1.lower()
    word2=word2.lower()
    #form empty list to store letters of words
    l1=[]
    l2=[]
    for e in word1:
        l1.append(e)
    for el in word2:
        l2.append(el)
    #sorting the list alphabetically
    l1.sort()
    l2.sort()
    if l1==l2:
        return True
    else:
        return False

#taking player name input
player1=str(input("\nEnter Player1 name:"))
player2=str(input("Enter Player2 name:"))
#taking words spoken by written
word_player1=str(input(f"\nEnter Word by {player1}:"))
word_player2=str(input(f"Enter Word by {player2}:"))
#using anagram function
result=anagram(word_player1,word_player2)
#printing the final result
if result==True:
    print(f"\nFriendship of {player1} and {player2} is REAL")
elif result==False:
    print(f"\nFriendship of {player1} and {player2} is FAKE")










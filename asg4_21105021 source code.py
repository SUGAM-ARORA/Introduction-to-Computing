

print("ASSIGNMENT 4")

print("\n Q1Write a recursive python function to solve the problem of tower of Hanoi with three disks.\n")

count = 0
def towerofhanoi(n, initial_rod, final_rod, extra_rod):
    global count
    if n == 0:                                                                                        
        return
    count += 1
    towerofhanoi(n-1, initial_rod, extra_rod, final_rod)                                                
    print("Move disk",n,"from rod",initial_rod,"to rod",final_rod)
    towerofhanoi(n-1, extra_rod, final_rod, initial_rod)

no_of_discs = int(input("Number of discs: "))
print("\nA is the initial rod\nB is the extra rod\nC is the final rod\n\nSteps:")
towerofhanoi(no_of_discs, 'A', 'C', 'B')
print("\nNumber of steps will be: %d" % (count))


print("\n Q2 Write a python program to print the Pascal’s triangle for n number of rows given by the user using both recursive and iterative procedures (for/while loop).")

def fact(n):
    if n==0:
        return 1
    return n*fact(n-1)
n=int(input("Enter the number of rows = "))
for i in range(n):
    for j in range(1,((2*n+1)//2)-i):                ##### or (n+1-i)
        print(end=" ")
    for t in range(i+1):
        print((fact(i)//(fact(i-t)*fact(t))),end=" ")
    print()



    
print("\n Q3 Input two integer values from user, calculate and print the quotient and reminder obtained from the two values")

n=int(input("Enter the Dividend = "))
m=int(input("Enter the Divisor = "))
a,b=divmod(n,m)
print("The Quotient is- {} and The Remainder is - {} ".format(a,b))
g=callable(divmod)
print("a). Is the function - divmod callable?     - Ans.",g)
if a!=0 and b!=0:
    print("b). All the values are non zeros or not?   -Ans.",True)
else:
    print("b). All the values are non zeros or not?   -Ans.",False)
li=[]
li.append(a)
li.append(b)
for i in (4,5,6):
    li.append(i)

for j in li[0:]:
    if j>4:
        pass
    else:
        li.remove(j)
print("c). The database - ",li)
set1=set(li)
print("d). The required database is - ",set1)
set_frozen= frozenset(set1)
print("e). The required immutable set is - ",set_frozen)
d=max(set_frozen)
print("f). The maximum value in the set is - ",d,"and its hash value is - ",hash(d))



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

class Employee:
    def __init__(self, name, salary):
        self.name = name
        self.salary = salary
    
    def __del__(self):
        print(f"Employee {self.name} record deleted")

# creating records
employee1 = Employee("Mehak", 40000)
employee2 = Employee("Ashok", 50000)
employee3 = Employee("Viren", 60000)

# a).
employee1.salary = 70000
print(f"a). The updated salary of the employee {employee1.name} is {employee1.salary}")

# b).
print("b). ", end='')
del employee3

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










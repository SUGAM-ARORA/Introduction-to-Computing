#Q1  Write a Python program to count the number of occurrences of each word or character in the string entered by the user. (Count the Number of Occurrences of each character only if the single word is entered by the user).

print("\nQuestion 1")

n=input("Enter the string - ")
# converting the string to lower case
a= n.lower()
## splitting the string into words
new_list=a.split()
# declaring two empty lists
letter_list=[]
word_list=[]
# Conditioning to distinguish if the entered string is a single word or a sentence... 
if len(new_list)==1:
    ## if the string is a word..
    for i in a:
         # adding each letter in the letter_list
        letter_list.append(i) 
    # introducing an empty dictionary    
    di1={}
    # here letters take place of key and number of their occurences take place of corresponding values in di1
    for j in letter_list:
        if j in di1:
            di1[j]=di1[j]+1
        else:
            di1[j]=1
    print(di1)
        
else:
    # if the string is not a word..
    for w in new_list:
        ### adding each word in the letter_list
        word_list.append(w)
    # introducing an empty dictionary  
    di4={}
    # here words take place of key and number of their occurences take place of corresponding values in di4
    for s in word_list:
        if s in di4:
            di4[s]=di4[s]+1
        else:
            di4[s]=1
            
    print(di4)


#Q2 Write a python script to print next date of input date. It must meet following conditions(use if-elif)

print("\nQuestion 2")

print("Enter Date below to get date of next day.\n")
# introducing leap year function
def leapyear(x):
    # leap year condition
    if (x%400)==0 or ((x%100!=0) and (x%4==0)):
        return True
    else:
        return False
#input from user
day=int(input("Enter Day [1-31]:"))
month=int(input("Enter Month [1-12]:"))
year=int(input("Enter Year [1800-2025]:"))
#condition 1
if day<1 or day>31 or month<1 or month>12 or year<1800 or year>2025:
    condition1=False
else:
    condition1=True

#condition 2
month_31 = [1, 3, 5, 7, 8, 10,12]  #List containing month with 31 days
month_30 = [4, 6, 9, 11]    #List containing month with 30 days
#for day entered 31 does not present in that month
c1a= day==31 and (month in month_30)
#for day entered greater than 29 in month february i.e 2
c1b= day>29  and month==2
#for day entered greater than 28 in february in non leapyear
c1c= day==29 and (not leapyear(year)) and month==2
if c1a or c1b or c1c :
    condition2=False
else:
    condition2=True
#printing error when date entered is not correct
if c1a:
    print(f"\nError\n{day} day can't be in month {month}")
elif c1b:
    print(f"\nError\n{day} day can't be in month {month}")
elif c1c:
    print(f"\nError\n{day} day can't be in month {month} as the year {year} in not leapyear")
elif condition1==False:
    print(f"\nError\nPlease enter date in range day[1-31], month[1-12], year[1800-2025] ")

#correct data
if condition1==True and condition2==True :
    month_31 = [1, 3, 5, 7, 8, 10,12]  #List containing month with 31 days
    month_30 = [4, 6, 9,11]    #List containing month with 30 days
    #For month with 31 days
    if (month in month_31) == True:
        if day == 31:
            day = 1
            month = month + 1
        elif 1 <= day <= 30:
            day = day + 1
    #For month with 30 days
    elif (month in month_30) == True:
        if day == 30 and month == 12:
            day = 1
            month = 1
            year = year + 1
        elif day == 30 and month != 12:
            day = 1
            month = month + 1
        elif 1 <= day <= 29:
            day = day + 1
    #for february month i.e. month 2
    elif month == 2:
        # If year is leap year
        if leapyear(year) == True:
            if day == 29:
                day = 1
                month = month + 1
            elif 1 <= day <= 28:
                day = day + 1
        # If year is not leap year
        elif leapyear(year) == False:
            if day == 28:
                day = 1
                month = month + 1
            elif 1 <= day <= 27:
                day = day + 1
    # Printing Next date
    print(f"\nNext Date in format Day/Month/Year is: {day}/{month}/{year}")

    

#Q3 . Write a Python program to create a list of tuples with the first element as the number and Second element as the square of the number.
    
print("\nQuestion 3")

#input list
list1=list(map(int,input("Enter the numbers separated by space:").split()))
#blank list
list2=[]
for e in list1:
    t=(e,e*e)
    list2.append(t)
# Printing the final result
print("\nList containing (n,n^2) is shown below:")
print(list2)



#Q4 Write a program to prompt the user for a grade between 4 and 10. If the grade is out of range print error message. If the grade is between 4 and 10 Print the grade and the performance using the following:


print("\nQuestion 4")

grade_point=int(input("Enter grade points:"))
dic={10:"Your grade is 'A+' and Outstanding performance.",
     9:"Your grade is 'A' and Excellent performance.",
     8:"Your grade is 'B+' and Very Good performance.",
     7:"Your grade is 'B' and Good performance.",
     6:"Your grade is 'C+' and Average performance.",
     5:"Your grade is 'C' and Below Average performance.",
     4:"Your grade is 'D' and Poor performance."}
#Applying Conditions for correct grade range
if 4<=grade_point<=10:
        statement=dic.get(grade_point)
        print(statement)
else:
       print("\nError\nPlease enter grade in range [4,10]")
       



#Q5 Write a python program to print following pattern.

print("\nQuestion 5")

string = "ABCDEFGHIJK"
j = 0
while len(string)-j*2 >= 1:
    print(" "*j, string[0 : len(string) - j*2])
    j += 1



#Q6 Write a python script that repeatedly ask user to enter name and SID of students (use ‘Y’ or ‘N’). Store them in a dictionary whose keys are SID’s and values are student’s name. Perform the following operations on Dictionary :

print("\nQuestion 6")

repeat="Y"
dic={}
dic2={}
#List containing Y or N
liste=["Y","y","n","N"]
while repeat=="Y" or repeat=="y":
    
    name = str(input("Enter student name:"))
    sid = int(input("Enter student SID:"))
    if sid<0:
        print("\nError\nSID can't be negative\n")
    else:
       
        dic.update({sid: name})
        
        dic2.update({name:sid})
       
        repeat = str(input("Enter Y to continue or N to end:"))
    if repeat=="N" or repeat=="n":
        break
    elif (not (repeat in liste)):
        print("\nError\nPlease enter valid input['Y' or 'N']")
        repeat=str(input("\nEnter Y to continue or N to end:"))

# a
#printing the dictionary
print("\nQ.6(a)")
print("The Dictionary containing {'SID':'Name'} is shown below")
print(dic)
# b
#sorting according to name
print("\nQ.6(b)")
list_k=sorted(dic2)
dic3={}
for ele in list_k:
    dic3.update({dic2.get(ele):ele})
print("The Dictionary after sorting according to name:")
print(dic3)

# c
#sorting according to SID
print("\nQ.6(c)")
sort_dic = sorted(dic)
dic4 = {}
for va in sort_dic:
    dic4.update({va: dic.get(va)})
print("The Dictionary after sorting according to SID:")
print(dic4)
# d
print("\nQ.6(d)")
# Taking input SID to be searched
enter_sid = int(input("Enter SID to get name of student:"))
# Searching for sid as key in dic
output_name = str(dic.get(enter_sid))
# printing name with key sid
print(f"Name of student with SID {enter_sid} is {output_name}.")





#Q7 Write a python program to print Fibonacci sequence also print average of the resultant Fibonacci series.

print("\nQuestion 7")

a = 0
b = 1
sum = 0
while True:                                                                                                         
    num = int(input("Enter the no. of terms of the Fibonacci sequence: "))
    if num < 0:
        print("Number of terms must be non-negative\nPlease enter again\n")
        continue
    if num == 0:
        print("As the number of terms = 0, the average of all terms = 0")
        break
    else:
        print("The Fibonacci sequence is as follows:")
        print(a,end=" ")
        for i in range(1,num):
            sum += b
            print(b, end=" ")
            c = a + b
            a = b
            b = c
        print("\nThe average of the terms of Fibonacci sequence upto %d terms is %0.2f" % (num,sum/num))
        break



#Q8 Given the sets below, write python statement to:

        
print("\nQuestion 8")
set1 = {1,2,3,4,5}
set2 = {2,4,6,8}
set3 = {1,5,9,13,17}
print("a. Set of all elements that are in Set1 and Set2 but not both:",end=" ")
set4 = set1^set2
print(set4)
print("b. Set of all elements that are in only one of the three sets Set1, Set2 and Set3:",end=" ")
set5 = set1^set2^set3
print(set5)
print("c. Set of elements that are in exactly two of the sets Set1, Set2 and Set3:",end=" ")
set6 = (set1|set2|set3) - (set1^set2^set3) - (set1&set2&set3)
print(set6)
print("d. Set of all integers in the range 1 to 10 that are not in Set1:",end=" ")
set7 = set()
for i in range(1,11):
    if i not in set1:
        set7.add(i)
print(set7)
print("e. Set of all integers in the range 1 to 10 that are not in Set1, Set2 and Set3:",end=" ")
set8 = set(range(1,11)) - (set1|set2|set3)
print(set8)

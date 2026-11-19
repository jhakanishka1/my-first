#1.Write a program to check if a number is positive.
"""num=int(input("enter the number:"))
if(num>=0):
    print("the number is positive")
else:
    print("the number is negative")


#2.Write a program to check if a character is a vowel.
char=input("enter the character you want to check:")
if(char == "a" or char =="e" or char == "i" or char == "0" or char =="u" or char == "A" or char =="E" or char == "I" or char =="0" or char == "U"):
    print("vowel")
else:
    print("consonants")

#3.Write a program to check if a person is eligible to vote (age >= 18).
age=int(input("enter the age:"))
if(age>=18):
    print("eligible to vote")
else:
    print("not eligible")

#4.	Write a program to check if a number is divisible by 5.
num=int(input("enter the number:"))
if(num%5 == 0):
    print("number is divisible by 5")
else:
    print("number is not divisible by 5")

#5.Write a program to check if a number is even.
num=int(input("enter the number:"))
if(num%2 == 0):
    print("even")
else:
    print("not even")



#6.	Write a program to check whether a number is even or odd.
num=int(input("enter the number:"))
if(num%2 == 0):
    print("even number")
else:
    print("odd")

#7.	Write a program to check if a year is a leap year.
year=int(input("enter the year:"))
if(year%4 == 0):
    print("leap year")
else:
    print("not an leap year")

#8.Write a program to check whether a person passed or failed (pass if marks >= 33).
marks=int(input("enter the marks of the student:"))
if(marks >= 33):
    print("student passed the subject")
else:
    print("student failed the subject")

#9.Write a program to find the greatest of two numbers.
num_1=int(input("enter the first number:"))
num_2=int(input("enter the second number:"))
if(num_1>num_2):
    print("num_1 is greatest")
elif(num_1<num_2):
    print("num_2 is greatest")
else:
    print("num_1 and num_2 are equal")

#10.Write a program to check whether a character is uppercase or lowercase.
char=input("enter any letter :")
if(char == 'A-Z'):
    print("uppercase")
elif(char == "a-z"):
    print("lowercase")
else:
    print("it can be anything")

#12.Write a program to assign a grade based on marks:
#90-100:A
#80-89: B
#70-79:C
#60-69:D	
#50<60:F
marks=int(input("enter the marks:"))
if(marks >= 90 and marks <= 100):
    print("grade A")
elif(marks >= 80 and marks <= 90):
    print("grade B")
elif(marks >= 70 and marks <= 80):
    print("grade C")
elif(marks >=60 and marks <= 70):
    print("grade D")
else:  
    print("grade E")

#18.Write a program to find the largest among three numbers.
first=int(input("enter the first number:"))
second=int(input("enter the second number:"))
third=int(input("enter the third number:"))
if(first >= second and first >= third):
    print("first number is largest")
elif(second >= first and second >= third):
    print("second number is largest")
elif(third >= first and third >= second):
    print("third number is largest")
else:
    print("none is largest")


#19.	Write a program to categorize age groups:
#20.	0-12: Child
#21.	13-19: Teenager
#22.	20-59: Adult
#23.	60 and above: Senior

age = int(input("enter the age of the person:"))
if(age>=0 and age<=12):
    print("child")
elif(age>=13 and age <=19):
    print("teenager")
elif(age >= 20 and age <= 59):
    print("adult")
else:
    print("senior")


#24.Write a program to check the type of triangle based on sides (equilateral, isosceles, scalene).
side_1=float(input("enter the first side of triangle:"))
side_2=float(input("enter the second side of triangle:"))
side_3=float(input("enter the third side of a triangle:"))
if(side_1 == side_2 == side_3):
    print("equilateral triangle")
elif(side_1 == side_2 or side_2 == side_3 or side_3 == side_1):
    print("isoceles triangle")
elif(side_1 != side_2 or side_2 != side_3 or side_3 != side_1):
    print("scalene triangle")

"""



#26.Write a program to check if a number is positive and even.
"""
num=int(input("enter the number you want to check :"))
if(num%2 == 0):
    if(num >= 0):
        print("number is positive and even",num)
    else:
        print("number is negative and even",num)
else:
    print("number is odd")

    
#question no 27
maths=int(input("enter the marks of maths:"))
physics=int(input("enter the marks of physics:"))
chemistry=int(input("enter the marks of chemistry :"))
pass_marks=33
distinction_marks=75
if(maths>=33 and physics>=33 and chemistry>=33):
    print("student passed in every subject")

    average=(maths+physics+chemistry)/3
    print("the marks abtained by the student:",average)
    if(average >= distinction_marks):
        print("student passed all and got distinction in the sunjects")
    else:
        print("student passed all subjects without distinction")
else:
    print("student didn't passed")


#question no 29
num = int(input("enter the number:"))
if(num%3==0 and num%5==0):
    print(f"{num}number is divisible by 3 and 5 ")
else:
    print(f"{num}number is not divisible by 3 and 5")
"""

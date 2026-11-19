#intermediate level
#1.Check roots of a quadratic equation using discriminant (real & distinct, real & equal, imaginary).
"""
a=int(input("enter the a of quadratic equation:"))
b=int(input("enter the b of quadratic equation:"))
c=int(input("enter the c of quadratic equation:"))
D=(b*b-4*a*c)
print("the discriminant of quadratic equation:",D)
if(D>0):
    print("roots found to be real and distinct")
elif(D<0):
    print("roots are imaginary")
else:
    print("roots are real and equal")

#2.Calculate income tax based on income slabs using if-else ladder.
income=int(input("enter the income to calculate income tax:"))
if(income == 400000):
    print("the tax is not payable")
elif(income >= 400001 and income <= 800000):
    print("income tax will be 5% of 400000")
    print("tax",5/100*400000)
elif(income >= 800001 and income <= 1200000):
    print("income tax will be 10% of 400000")
    print("tax",10/100*400000)
elif(income >= 1200001 and income <= 1500000):
    print("income tax will be 15%of 300000")
    print("tax",15/100*300000)


#3.	Find the day of the week based on a number (1–7), and validate input.
number=int(input("enter the number between (1-7):"))
if(number >=1 and number<=7):
    if(number == 1):
        print("MONDAY")
    elif(number == 2):
        print("TUESDAY")
    elif(number == 3):
        print("WEDNESDAY")
    elif(number == 4):
        print("THURSDAY")
    elif(number == 5):
        print("FRIDAY")
    elif(number == 6):
        print("SATURDAY")
    else:
        print("SUNDAY")
else:
    print("error")

#4.Check if a triangle is valid given three sides (triangle inequality).
a=int(input("enter the side of a triangle a="))
b=int(input("enter the side of a triangle b="))
c=int(input("enter the side of a triangle c="))
if((a+b >c) and (a+c >b) and (b+c >a)):
    print("triangle is valid")
else:
    print("triangle is not valid")


#6.Check if a given time (hh:mm:ss) is valid or not.
hour=int(input("enter the hour:"))
minute=int(input("enter the minute:"))
second=int(input("enter the second:"))
if((24>hour>0) and(60>minute>0) and (60>second>0)):
    print("the time is correct",hour,minute,second)
else:
    print("the time is not correct")

#7.	Input a 3-digit number and check if it is an Armstrong number.
num=int(input("enter the three digit number:"))
if(num > 0):
    digit=num % 10
    middle=((num//10)%10)
    hundred=num//100
    unit=(digit)**3
    centre=(middle)**3
    temp=(hundred)**3
    sum_num=unit+centre+temp
    print("the sum of cubes of digit is:",sum_num)
if(num==sum_num):
    print("armstrong number")
else:
    print("not an armstrong number")

#8.	Take date (dd, mm, yyyy) and check if it is valid, considering leap years.
date=int(input("enter the date between (1-31):"))
month=int(input("enter the month between(1-12):"))
year=int(input("enter the year :"))
if((31>=date>0)and(13>month>0)):
    if(year%4 == 0):
        if(0<date<29):
            print("leap year")
        else:
            print("not an leap year")
    else:
        print("normal year")
else:
    (print("dates and month are not correct"))


#9.	Input coordinates (x, y) and determine the quadrant, origin, or axis.
x=float(input("enter the x coordiante:"))
y=float(input("enter the y coordiante:"))
if(x==0 and y==0):
    print("origin")
elif(x!=0 and y==0 and x<0):
    print("negative x axis")
elif(x==0 and y!=0 and y<0):
    print("negative y axis")
elif(x>0  and y>0):
    print("top right quadrant")
elif(x<0 and y>0):
    print("top left quadrant")
elif(x<0 and y<0):
    print("bottom left quadrant")
elif(x>0 and y<0):
    print("bottom right quadrant")
else:
    print("none")


#10.Check if a number is palindrome without using loops (3-digit only).
num=int(input("enter the three digit number:"))
if(num>100 and num<=999):
    hundred=num//100
    tenth=((num//10)%10)
    unit=num%10
    reverse=(unit*100)+(tenth*10)+hundred
    print("reverse:",reverse)

    if(num==reverse):
        print("pallindrome number")
    else:
        print("not a pallindroem number")
        """
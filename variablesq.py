#question 1
#1 Write a program to take two numbers as input and perform all arithmetic operations (+, -, *, /, %,//,**). 
"""a=int(input("enter the number a:"))
b=int(input("enter the number b:"))
print("the addition of two number is:",a+b)
print("the substraction of two number is:",a-b)
print("the multiplication  of two number is:",a*b)
print("the division of two number is:",a/b)
print("the floor division of two number is:",a//b)
print("the power of two number is:",a**b)
print("the modulus of two number is:",a%b)


#question 2
#Take two numbers as input and swap their values without using a third variable. 
a=int(input("enter the number a:"))
b=int(input("enter the number b:"))
a=a+b
b=a-b
a=a-b
print(a)
print(b)

#question 3
#3.	Given a number, calculate its square and cube. 
a=int(input("enter the number:"))
print("the sqaure of a is :",a*a)
print("the cube of a is :",a*a*a)

#question no 4
4.	Write a program to find the sum and average of three numbers. 
a=int(input("enter the number a:"))
b=int(input("enter the number b:"))
c=int(input("enter the number c:"))
print("the sum of a b and c is:",a+b+c)
print("the average of a b and c is",a+b+c/3)
  

#question 5 
5.	Compute the perimeter and area of a rectangle using given length and breadth.
length=float(input("enter the length of rectangle:"))
breadth=float(input("enter the breadth of rectangle:"))
print("the perimeter of rectangle:",2*(length+breadth))
print("the area of rectangle:",length*breadth)

#6.Take a number as input and reverse its digits using arithmetic operators.
n=int(input("enter the three digit number:"))
hundred=n//100
tens=((n//10)%10)
unit=(n%10)
reverse=((unit)*100+(tens*10)+hundred)
print("the reverse of n will be:",reverse)

6.#Take a number as input and reverse its digits using arithmetic operators.
n=int(input("enter the three digit number:"))
#question no 7
#7.	Given the radius of a circle, calculate its circumference and area. (Use 3.1416 for π).
r=float(input("enter the radius of a circle:"))
circumference=2*3.14168*r
area_of_circle=3.1416*r*r
print("thr circumference of a circle:",circumference)
print("thr area of circle:",area_of_circle)


#question no 8
8.	Write a program to convert temperature from Celsius to Fahrenheit and vice versa.
celsius=float(input("enter the temperature in celsius:"))
fahrenheit=(celsius*9/5)+32
print("celsius is equals to {fahrenheit}\n",fahrenheit)
fahrenheit_input=float(input("enter the temaperature in fahrenheit:"))
celsius_output=(fahrenheit_input-32)*5/9
print("the fahrenheit is equals to the celsius",celsius_output)


#question no 9 
9.	Take a 3-digit number and find the sum of its digits using arithmetic operators.(list)
num=input("enter the three digit number:")
first_digit=num[0]
second_digit=num[1]
third_digit=num[2]
sum=int(first_digit)+int(second_digit)+int(third_digit)
print("the sum of three digit number:",sum)


#question no 9 by arithmetic operator

num=int(input("enter the three digit number:"))
hundred=num/100
tenth=(num/10)%10
unit=num%10
print("the sum of a three digit number:",hundred+tenth+unit)
num=int(input("enter the three digit number:"))
mod=

#question no 10
#10.Compute Simple Interest and Compound Interest using given principal, rate, and time.
p=float(input("enter the principal :"))
r=float(input("enter the rate of interest:"))
t=float(input("enter the time money is invested:"))
SI=p*r*t/100
amount=p*(1+r/100)**t
CI=amount - p
print("the simple interest:",SI)
print("the compound interest:",CI)
 

#11.Write a program to add, subtract, multiply, and divide two floating-point numbers.
num_1=float(input("enter the first number:"))
num_2=float(input("enter the second number:"))
print("the addition of two no's :",num_1+num_2)
print("the substraction of two no's :",num_1-num_2)
print("the multiplication of two no's :",num_1*num_2)
print("the division of two no's :",num_1/num_2)

#12.Given three numbers, find the smallest among them.
a=int(input("enter the number a:"))
b=int(input("enter the number b:"))
c=int(input("enter the number c:"))
if(a>b and b>c):
    print(f"{c} is the smallest number")
elif(b>a and c>b):
    print(f"{a} is smallest number")
elif(c>a and a>b):
    print(f"{b} is smallest")


#13.Compute the area and perimeter of a square given its side length.
side=float(input("enter the side of a square:"))
area=side*side
perimeter_of_square=4*side
print("the area of square:",area)
print("the perimeter of a square:",perimeter_of_square)


#14.Write a program to calculate the area of a triangle
base=float(input("enter the base of a triangle:"))
height=float(input("enter the height of a triangle:"))
area_of_triangle=1/2*base*height
print("the area of triangle:",area_of_triangle)


#15.Take a number as input and check whether it is divisible by 2, 3, or both.
num=int(input("enter the number:"))
if(num%2 ==0 and num%3 ==0):
    print("the number is divisible by both 2 and 3")
elif(num%2 != 0 and num%3 ==0):
    print("the number is divisible by 2 but not 3")
elif(num%2 == 0 and num%3 != 0):
    print("the number is divisible by 2 but not 3")
elif(num%2 != 0 and num%3 !=0):
    print("the number is not divisible either by 2 or 3")


    #16.Given the cost price and selling price of an item, calculate the profit or loss.
cost_price=int(input("enter the cost price:"))
selling_price=int(input("enter the selling price:"))

if(selling_price == cost_price):
    print("no profit and no loss will occur")
elif(selling_price > cost_price):
    print("profit will occur")
    print("the profit will be :",selling_price - cost_price)
elif(cost_price > selling_price):
    print("loss will happen")
    print("the loss will be:",cost_price - selling_price)

#17.	Compute the electricity bill based on given units consumed with the following rates: 
#o	First 100 units: ₹5 per unit
#o	Next 200 units: ₹7 per unit
#o	Above 300 units: ₹10 per unit


#18.Convert a given kilometers value into meters, centimeters, and millimeters.
kilometer = float(input("enter the value in kilometer:"))
meter = kilometer * 1000
centimeter = kilometer * 100000
millimeter = kilometer * 1000000
print("the values converted from km to m:",meter)
print("the values converted from km to cm:",centimeter)
print("the values converted from km to mm:",millimeter)



#19.Write a program to check if a given year is a leap year or not.
year=int(input("enter the year you want to check:"))
if(year%4 == 0):
    print("leap year")
else:
    print("not a leap year")


#20.Given a number, find whether the sum of its digits is odd or even.
num=int(input("enter the three digit number:"))
first_digit=num//100
second_digit=(num//10)%10
last_digit=num%10
print("first digit:",first_digit)
print("second digit:",second_digit)
print("third digit:",last_digit)
sum_digit=first_digit+second_digit+last_digit
if(sum_digit%2 == 0):
    print("the sum of number is even",sum_digit)
else:
    print("the sum of number is odd",sum_digit)
"""

#21.Write a program to find the difference between the sum of even and odd digits of a number. 






#question no 22
"""
number=int(input("enter the number:"))
if (number%2 != 0):
    print("the number is odd")
    sum_odd=number*number
    print("the sum of odd n digit number",sum_odd)
else:
    print("the number is even")



#22.Compute the sum of the first N odd numbers. 
n=int(input("enter the number:"))
if(n%2 != 0):
    print("odd number")
    sum_odd=((n+1)/2)**2
    print("the sum of N odd number are:",sum_odd)
else:
    print("even number",n)

#23.Write a program to find the percentage of a student’s marks in 5 subjects. 
math=int(input("enter the marks of maths:"))
physics=int(input("enter the marks of physics:"))
chemistry=int(input("enter the marks of chemistry:"))
english=int(input("enter the marks of english:"))
hindi=int(input("enter the marks of hindi:"))
total_max=500
total_marks=math+physics+chemistry+english+hindi
percentage=(total_marks/total_max)*100
print(total_marks)
print("the percentage of 5 subjects:",percentage)

#24.Compute the sum of all digits in an N-digit number without using loops. 
num=int(input("enter the N digit number:"))
hundred=(num//100)
tens=((num//10)%10)
unit=(num%10)
print("the sum of N digit number taken from input:",hundred+tens+unit)


#25.Given a person's age in years, calculate their age in months, weeks, and days.
age=int(input("enter the age of a person in years:"))
months=age*12
weeks=age*52
days=age*365
print("the age of person:",age)
print("the age in months,weeks,days will be",months)
print("the age in months,weeks,days will be",weeks)
print("the age in months,weeks,days will be",days)



#26.Convert a given time in 12-hour format to 24-hour format.
hours=int(input("enter the hours(1-12):"))
minutes=int(input("enter the minutes:"))
period=input("enter the AM or PM:")
if(period =="AM" and hours ==12):
    hours=0
elif(period =="PM" and hours != 12):
    hours=hours+12
print("24 hour format:",hours,minutes)


#27.Compute the absolute difference between the sum of squares and the square of sum of first N natural numbers. 
n=int(input("enter the number:"))
sum_of_square=(n*(n+1)*(2*n+6)/6)
square_of_sum=(n*(n+1)/2)**2
difference =  square_of_sum - sum_of_square
print("the difference between sum of squares and square of=",difference)



#28.Given two numbers, check if their product is a perfect square
num_1=int(input("enter the first number:"))
num_2=int(input("enter the second number:"))
product=num_1*num_2
if(product<0):
    print("perfect square does not exist")
else:
    root=int(product**0.5)
    if(root*root == product):
        print(f"{product} is a perfect square")
    else:
        print(f"{product} is not a perfect square")


#25.Given a person's age in years, calculate their age in months, weeks, and days. 

age=int(input("enter the age of a person in years:"))
months=age*12
weeks=age*52
days=age*365
print("the age of person:",age)
print("the age in months,weeks,days will be",months)
print("the age in months,weeks,days will be",weeks)
print("the age in months,weeks,days will be",days)

"""

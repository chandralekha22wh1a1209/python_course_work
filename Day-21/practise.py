'''
n = int(input("enter a number: "))
if n > 0:
    print('positive number')
else:
    print('negative number')


n = int(input("enter a number: "))
if n%2==0:
    print("even number")
else:
    print("odd number")

n = int(input("enter a number: "))
if n%5==0:
    print("Divisible by 5")
else:
    print("not divisible by 5")

n = int(input("enter a number: "))
if n%3==0 and n%7==0:
    print("divisble by 3 and 7") 
else:
    print("not divisible by both")

year = int(input("enter a year: "))
if year%400==0:
    print("it is a leap year")
else:
    print("not a leap year")
    
marks = int(input("enter the marks: "))
if marks <= 35:
    print("Fail")
else:
    print("pass")
    
n = int(input("Enter a number: "))

if 100 <= n <= 999:
    print("Three digit number")
else:
    print("Not a three digit number")




units = int(input("Enter units: "))

if units <= 100:
    bill = units * 1.5
elif units <=200:
    Bill =  units * 1.5 + units * 2.5 + (units - 100)
elif units <= 500:
    bill = units * 1.5 + units * 2.5 + units * 4 + (units - 200) 
else:
    bill = units * 1.5 + units * 2.5 + units * 4 + units * 6 + (units - 500)

senior = input("senior citizen? yes/no: ")
if senior == "yes":
    bill = bill * 0.90
if bill > 800:
    bill = bill * 1.05
print("Bill =", bill)
'''
units = int(input("enter units: "))

if units <= 100:
    bill = units * 1.5
elif units <= 200:
    bill = units * 2.5
elif units <= 500:
    bill = units * 4
else:
    bill = units * 6
senior = input("senior citizen? yes/no: ")
if senior == "yes":
    bill = bill * 0.90
if bill > 800:
    print("bill =", bill)
    

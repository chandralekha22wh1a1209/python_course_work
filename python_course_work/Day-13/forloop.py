#for loop
#range-numeric values,it gives index values
'''
s = 'python programming'
for i in range(len(s)):
    if s[i] in 'aeiouAEIOU':
         print(i,s[i])
   

l=[24,56,67,78,89,90,43,54,76]
sum=0
for i in range(len(l)):
    if l[i]%2==0:
        sum=sum+i
print(sum)
#factorial
n= int(input("enter the number"))
fact = 1
for i in range(1,n+1):
    fact *= i
print(f"Factorial of {n} is {fact}")
#maximum marks

data = {}
n = int(input("Enter the no of students: "))
max_marks = 0
for i in range(n):
    name = input("Enter the name: ")
    marks = int(input("enter the marks: "))
    if marks > max_marks:
        max_marks = marks
    data[name] = marks
print(data)
print("Maximum Marks:",max_marks)
#minimum marks
data = {}
n = int(input("enter the no of students: "))
min_marks = 0
for i in range(n):
    name = input("Ennter the name: ")
    marks = int(input("enter the marks: "))
    if marks > min_marks:
        min_marks = marks
    data[name] = marks
print(data)
print("Minimum Marks:",min_marks)
#generate a bill ask a user to enter the no of products to buy 5 products and price and quantity of products and finally bill the products
data = {}
bill = 0
n =int(input("enter no of items: "))
for i in range(n):
    print(input("enter the products: "))
    price=int(input("enter the price: "))
    q=int(input("enter the quantity: "))
    r=q*price
    bill+=r
print(data)
print(bill)
#2nd method
n = int(input("Enter the no of products: "))
total_bill = 0
for i in range(n):
    product = input(f"Product - {i}: ")
    price = float(input(f"price - {i}: "))
    quantity = int(input(f"quantity - {i}: "))
    final_price = price*quantity
    total_bill += final_price
    products[product] = f'{price} * {quantity} = {final_price}'
print(products)
print("Total Bill:",total_bill)
product = input("enter the products: ")
price = int(input("enter the price: "))

if product == "exit":
    break
price = int(input("enter price: "))
products[product] = price
print(products)
'''
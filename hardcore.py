# qu1 > Write a Python Program to Find Armstrong Number in an Interval. 

# n1 = int(input("Enter a Upper Number : "))
# n2 = int(input("Enter a Lower Number : "))

# for i in range(n1,n2+1):
#     sum=0
#     order =len(str(i))
#     temp=i
#     while temp>0:
#         digit=temp%10
#         sum+=digit**order
#         temp//=10
#     if sum==i:
#         print(i)
     

# Question 3 >> How to convert any number in binary code ?
# number = int(input("enter a Number : "))
# print(bin(number))


# question how to convert any alphabet into ASCII Values
# char = str(input("Enter any name : "))
# print("The ASCII Values of",char,"is",ord(char))

# write a program that behave like a real calculator ?
# def add(x,y):
#     return x+y
# def sub(x,y):
#     return x-y
# def multi(x,y):
#     return x*y
# def divide(x,y):
#     return x//y

# print("Select Operation")
# print("1. Add")
# print("2. Subtract")
# print("3. Multiply")
# print("4. Divide")

# while True:
#     choice = input("Enter Your Choice : ")
#     if choice in ('1','2','3','4'):
#         try:
#             num1 = float(input("Enter first Number : "))
#             num2 = float(input("Enter Second Number : "))
#         except ValueError:
#             print("Please Enter a Number ")
#             continue

#         if choice=='1':
#             print(num1,'+',num2," = ",add(num1,num2))
#         elif choice=='2':
#             print(num1,'-',num2," = ",sub(num1,num2))
#         elif choice=='3':
#             print(num1,'*',num2," = ",multi(num1,num2))
#         elif choice=='4':
#             print(num1,'//',num2," = ",divide(num1,num2))

#         option = input("Do you want to continue Yes//no")
#         if option=='no':
#             break
#     else:
#         print("Invalid")
            
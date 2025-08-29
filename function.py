# def hello_world():
#     print("hello, world")
# hello_world()
# def hello_world():
#     print("Hello, World!")

# Call the function
# hello_world()

# def print_name():
#     for i in range(5):
#         print("Krish Gour")
# print_name()

# def number():
#     for i in range(1,11):
#         print(i)
# number()

# def check_even_odd():
#     for i in range(12453,12497):
#         print(chr(i),end=" ")

# check_even_odd()


# def sum():
#     print("The Sum Of",a,b," is", a+b )
# a = int(input("Enter a Number 1: "))
# b = int(input("Enter a Number 2: "))
# sum()


# def square():
#     if a>b and a>c:
#         print(a," is greater")
#     elif(b>a and b>c):
#         print(b," is greater")
#     elif(c>a and c>b):
#         print(c," is Greater")
# a = int(input("Enter a Number : "))
# b = int(input("Enter a Number : "))
# c = int(input("Enter a Number : "))
# square()



# def reverse():
#     a = 678
#     rev = 0
#     digit = a % 10
#     rev = rev * 10 + a
#     a = a / 10
#     print(a)


# reverse()



# to reverse a string using function:
# def rev_str(s):
#     rever_str=" "
#     for char in s:
#         rever_str=char+rever_str
#     return rever_str
# s=input("enter a name ")
# print(rev_str(s))\





# def greet(name):
#     if name == "":
#         print("hello Guest ")
#     else:
#         print("Hello " ,name)
# greet(input("Enter Your name :"))

# def max_2 (a,b):
#      if a>b:
#           return a
#      else:
#           return b
# print()

# def max_3(a,b,c):
#     if a>b and a>c:
#         return a
#     elif b>a and b>c:
#         return b
#     else:
#         return c
# print(max_3(12,20,34))


# def prime(n):
#     if n==0 or n==1:
#         print("not prime number")
#     elif n>1:
#         for i in range(2,n):
#             if n%i==0:
#                 print("Not a prime number")
#                 break
#             else:
#                 print("Prime number")
#     else:
#         print("not")
            
# prime(7)



# #without argument and without return type--------------
# def fibo():
#     a = 0
#     b = 1
#     n = int(input("enter a Number :"))
#     print(a,b,end=" ")
#     for i in range(2,n+1):
#         c = a+b
#         print(c,end=" ")
#         a = b
#         b = c
# fibo()




# def number():
#     for i in range(1,11):
#         print(i)
# number()

# def check_even_number():
#     for i in range(1,21):
#         if i%2==0:
#             print(i,"even number")
#         else :
#             print(i,"odd")
# check_even_number()



# def factorial(n):
#     if n==0 or n==1:
#         return 1
#     else:
#         return n* factorial(n-1)
# print(factorial(10))


# def factorial(n):
#     if n == 1 or n==0:
#         return 1
#     return n * factorial(n -1 )
# n = int(input ("Enter a Number :"))
# print(factorial(n))









#   1
# def fact(n):
#     if n==1 or n==0:
#         return 1
#     else:
#         return n*fact(n-1)
# print(fact(5))

#2
# def sum(n):
#     if n==1:
#         return 1
#     else:
#         return n+sum(n-1)
# print(sum(10))

# def max(a):
#     if a==0 or a == 1:
#         return 1
    
# li = list()
# for i in range(1,11):
#     li.append(i)
# print(li)

# li = [i for i in range(1,11)]
# print(li)

# positional argument
# 1 key word argument
# 2 defaukt argument
# 3 variable length argument
# 4 key word variable length arguent


# Hof (high Order Functions)

# def square(x):
#     return x*x
# def apply(func,value):
#     return func(value)
# print(apply(square,5))


# Built in Hofs


# using of map >>><<<<<
# a = [1,2,3,4,5]
# square = list(map(lambda x:x*x,a))
# print(square)


# using of filter functions 

# a = [1,2,3,4,5,6,7,8,9,10]
# even = list(filter(lambda x:x%2==0,a)) # it can only print matching condition
# print(even)




# types of arguments
# 1 key-word argument
# 2 default argument 
# 3 variable length argument
# 4 key-word variable length argument 

# 1 key-word argument

# def studentdata(name,rollno):
#     print(f"Welcome {name} your rollno is {rollno} ")

# studentdata(rollno=100,name="raj")

# # 2 default argument 

# def addition(a=0,b=0):
#     print(a+b)

# addition(8)


# def function(name,rollno):
#     print(f"your name {name} and your rollno is {rollno}")
# function("Krish",101)

# def sum(a=0,b=0):
#     if a!=0 and b!=0:
#         print(a+b)
#     else:
#         print(a*b)
    
# sum(0,3)

# with the help of high order function we can make capital and small
# a = ["upper","pYTHon"]
# upper_case = list(map(str.upper,a))
# lower_case = list(map(str.lower,a))
# print(lower_case)
# print(upper_case)

# from functools import reduce
# a = [2,3,4]
# products_a=reduce(lambda x,y:x*y,a )
# print(products_a)


# import calendar
# yy = 2025
# mm =8
# print(calendar.month(yy,mm))

def prime_number(n):
    if n<2:
        return 0
    else:
        for i in range(3,n-1):
            if i%n==0:
                return False
            return True
            
print(prime_number(4))

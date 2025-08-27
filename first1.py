# a=int(input("Enter a Number :"))
# if(a%2==0):
#     print("Even Number")
# else:
#     print("Odd Number")

#Account Number is 1234
# balance = 1000
# a=int(input("Enter your account Number = "))
# b=int(input("1.Withdrawel 2. Deposit 3. Credit =" ))
# a==1234
# if(b==1):
#     print(balance)
# elif(b==2):
#     print(b+balance)
# elif(b==3):
#     a=int(input("enter a deposit amount"))
#     print(balance-a)
# else:
#     print("No Valid Option")



#Using Uppercase in Pyhton?

# a="krisgour"
# uppercase_b = a.upper()
# print(uppercase_b)


# spilting the sentance

# a = "Krish,gour"
# b= a.split(",")
# print(b)


# a="I am Boy"
# b="z" in a
# print(b)

# def greet(name):
#     print("hello ,"+name+ "!")
# greet()

# num= int(input("Enter a number: "))
# fraction = 1
# if num <0:
#     print("factorial is not defined for negative numbers")
# elif num==0:
#     print("the factorial of 0 and 1 is 1")
# else:
#     for i in range(1,num+1):
#         fraction *= i
#         print("The factorial of ", num, "is", fraction)


# start = int(input("enter a start  number:"))
# end = int(input("Enter a end number :"))
# for i in range (start, end+1):
#     if i%3==0 and i%5==0:
#         print("Number is divisible by 3 and 5:", i)
    
# num =int (input("enter a number:"))
# sum=0
# i=1
# while i<=num:
#     sum +=i
#     i +=1
#     print(sum)



# Q.1 Write a table of any Number ?    
# table = int(input("Enter a number for table:"))
# for i in range(1,11):
#     print(table, "x", i,"=",table*i)

# num = int(input("enter a number:"))
# count = 0
# for i in range (1,num+1):
#     if num%i==0:
#         count +=1
# if count==2:
#     print(num," is a prime number")
# else:
#     print(num,"is not a prime number")


# start = int(input("Enter a number"))
# end = int(input("enter a number"))
# for i in range(-end,start):
#     print(i)

# num = int(input("enter a number:"))
# reverse = 0
# while num>0:
#     digit = num % 10
#     reverse = reverse * 10 + digit
#     num = num//10
# print("the reverse of the number is:", reverse)


#---------------PDF QUESTION--------------------------

# 1. Question No.1
# i=10
# for i in range(1,i+1):
#     print(i)


# i=2
# while i<=20:
#     print(i)
#     i += 2

# 2. Question No.2

# table = int(input("Enter a Number "))
# for i in range(1,10+1):
#     print(table,"*",i,"=",i*table)


# num=1
# sum=0
# while num<=10:
#     sum +=num
#     print(sum)

# sum of natural number using while Loop

# num = int(input("Enter a Number:"))
# sum=0
# i=1
# while i<=num:
#     sum +=i
#     i +=1
# print("The sum of natural Number is ",sum)

# Keep asking the user to input a number until they enter a number greater than 10 using a
# do-while loop logic

# num = 0
# while True:
#     num = int(input("Enter a Number greater than 10:"))
#     if num >10:
#         print("You entered:",num)
#         break
#     else:
#         print("Please enter a number greater than 10.")

# Write a program to calculate the factorial of a number using a for loop

# num = int(input("Enter a Number to calculate factorial:"))
# factorial = 1
# for i in range(1,num +1):
#     factorial *=i
# print("The Factorial of", num, "is", factorial)








# a=[1,23,45,34,54]
# a.append(67)
# print(a)

# take a input from the user and append it to the list

# b=[]
# for i in range(5):
#     a=int(input("no"))
#     b.append(a)
#     print(b)



# i = 1
# while i<=5:
#     print(i)
#     i += 1

# for i in range(4):
#     print("hello world")


# a = int(input("enter a triangle :"))
# b = int(input("enter a triangle :"))
# c = int(input("enter a triangle :"))
# if a+b>c and a+c>b and b+c>a:
#     print("the triangle is valid")
# else:
#     print("the triangle is not valid") 


# a = [23,24,53,76,345]
# a[0] = 100
# print(a)


# a.insert(2,78)
# print(a)
# a.pop(3)

# print(a)
# for item in a:
#     print(item)
# print(a)

# if 23 in a:
#     print("yes 23 is present in thr list")

# len(a)
# print(len(a))

# matrix = [[1,2,3],[4,5,6],[7,8,9]]
# print(matrix[1][2])



#------------------tuple---------
# a = (1,2,3,4,5)
# print(type(a))

# element enclosed in round brackets
# element sepated by commas
# immutable 
# ordered
# heterogeneous

# a = (1,2,3,3,3)
# print(a)
# a= [1,1,2,2]
# print(a)

#--------------------Dictionary-----------------

# a = {"Name":"Krish","Age":23,"city":"delhi"}
# a["Name"] = "Gour"
# print(a)




#----------------------------Set-------------------------
# a={"a",12,12.2,12}
# print(a)


#Loops { for)}
# for i in range(6):
#     print(i)


# n = int(input("Enter a number :"))
# for i in range(0,n+1,2):
#     print(i,end=" ")




# n = 20
# for i in range(1,n,2):
#     print(i,end=" ")


# for i in range(20,-5,-2):
#     print(i,end=" ")


# for i in range(1,11):
#     print(i,end=" ")

# n = 20
# for i in range(1,n,2):
#     print(i,end=" ")

# for i in range(1,11):
#     print(i,end=" ")

# for i in range(0,11):
#     print(i,end=" ")

# n=11
# for i in range(0,n,2):
#     print("Even Number is " ,i,end=" ")
# for j in range(1,n,2):
#     print("odd Number is " ,j,end=" ")


# n=11
# for i in range(0,n):
#     if i%2==0:
#         print("Even Number is ",i)
#     else:
#         print("Odd Number is ",i)


# num = int(input("Enter a number :"))
# sum=0
# for i in range(0,num+1):
#     sum += i
# print("The sum of natural number is ",sum)

# n = int(input("Enter a Number :"))
# count = 0
# for i in range(1,n+1):
#     if(i%2==0):
#         count +=1
# print("The count of even number is ",count)
    

# a = 5
# for i in range(1,5+1):
#     for j in range(1,5+1):
#         print(i,end=" ")
#     print()
      



      # _______________________Patterns in Pyhton?

# WAP to print the star?

# n=5
# for i in range(1,n+1):
#     print("*"*i)
# n=5
# for i in range(1,n+1):
#     for j in range(1,i+1):
#         print(j,end=" ")
#     print()


# import re
# text = "Krish123 is 20 years old in 2025"
# digits=re.findall(r'\+',text)
# print(digits)

# n=5
# for i in range(n,0,-1):
#     print("*"*i)

# n=5
# num=1
# for i in range(1,n+1):
#     for j in range(1,1+i):
#         print(num,end=" ")
#         num += 1
#     print()

#now we are going to undestand the methods of list?
# a = [1,2,3,4,5,4,4,4,6,7]
# print(a[-6])
# print(a[1:4])

# a.append(8) # add items to end
# a.insert(2,9) # it will insert the item at index 2
# a.remove(3) # it will remove the item 3 from the list
# a.pop(5) #it will remove the item at index 1
# a.extend([10,11,12]) #it will add the items to end of the list
# a.clear() #it will clear the list
# a = ['banana','apple','orange']
# a.index('banana')
# a.reverse() #it will reverse the number 
# a.sort # it will run at asecding order
# a.copy() #it will copy the list
# print(a.index(4))


# Wap to print the print the sum and count of even and odd number 

# n = int(input("Enter a number :"))
# evensum=0
# evencount=1
# oddsum=0
# oddcount=1

# for i in range(1,n+1):
#     if i%2==0:
#         evensum +=i
#         evencount +=1
#     else:
#         oddsum +=i
#         oddcount +=1
# print("The sum of even number is ",evensum)
# print("The count of ecen")


# n = int(input("Enter a number :"))
# factorial = 1
# for i in range(1,n+1):
#     factorial =i*factorial
# print(factorial)


# a = 0
# b = 1
# n = int(input("Enter a number : "))
# print(a,b,end=" ")
# for i in range(2,n):
#     c = a+b
#     print(c,end=" ")
#     a =b
#     b=c
    


# n = int(input("Enter a number:"))
# count = 0
# for i in range(1,n+1):
#     if n%i==0:
#         count += 1
# if count ==2:
#       print(n,"is a prime number")
# else:
#      print(n,"is not a prime number")




# n = 6
# for i in range(6):
#     for j in range(i+1):
#         print("#",end=" ")
#     print()


# n = 7
# for i in range(7):
#     for j in range(i,n-1):
#         print("#",end=" ")  
#     print()

n=5
for i in range(n):
    for j in range(n-i-1):
        print(" ",end=" ")
    for j in range(i+1):
        print("#",end=" ")
    print()

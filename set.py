# prime = int(input("Enter a Number : "))
# if prime>1:
#     for i in range(2,prime):
#         if prime%i==0:
#             print(prime," is not a prime number")
#             break
#     else:
#         print(prime," is a prime number ")
# else:
#     print(prime," is not prime number")


# k = int(input("Enter a Number : "))
# prime = [] 
# for n in range(2,k+1):
#     if n>1:
#         for i in range(2,n):
#             if n%i==0:
#                 break
#         else:
#             prime.append(n)
# print(prime)

# n = int(input("Enter a Number"))
# a,b=0,1
# count = 0
# while count<n:
#     print(a,end=" ")
#     c=a+b
#     a,b=b,c
#     count+=1

# n = 10
# a,b=0,1
# for i in range(n+1):
#     print(a,end=" ")
#     a,b=b,a+b





# x = int(input("Enter a number :"))
# y = int(input("Enter a number :"))
# if x>y:
#     greater = x
# else:
#     greater = y
# while (True):
#     if greater%x==0 and greater%y==0:
#         lcm = greater
#         break
#     greater+=1
# print(lcm)

# x = int(input("Enter a Number :"))
# y = int(input("Enter a Number :"))
# if x>y:
#     smaller =  x
# else:
#     smaller = y
# for i in range(1,smaller+1):
#     if x%i==0 and y%i==0:
#         hcf = i
# print(hcf)


# n = int(input("Enter a number : "))
# for i in range(1,n+1):
#     if n%i==0:
#         print(i)


# n = int(input("enter a number :"))
# obj = len(str(n))
# sum = 0
# m = n
# while n>0:
#     digit = n%10
#     sum+=digit**obj
#     n = n//10
# if sum==m:
#     print(m," is a armstrong Number")
# else:
#     print(m,"is not a amrstrong number")




# n = int(input("enter a number :"))
# m=y=n
# count = 0
# sum = 0

# while n>0:
#     count+=1
#     n=n//10
# print(count)
# while y>0:
#     digit = y%10
#     sum+=digit**count
#     y = y//10
# if sum==m:
#     print(m," is a armstrong Number")
# else:
#     print(m,"is not a amrstrong number")


# n = input("enter a number :")
# m = n
# obj = len(n)
# rev = 0
# while obj>0:
#     digit = n%10
#     rev=rev*10+digit
#     n = n//10
# print(sum)

# n = input("enter a number :")
# rev = ""
# i = len(n)-1
# while i>=0:
#     rev=rev+n[i]
#     i-=1
#     print(rev)


# n = input("enter a number :")
# rev = ""
# i = len(n)-1
# for i in range(i,-1,-1):
#     rev=rev+n[i]
# print(rev)


# num = int(input("Enter a Number : "))
# sq = num+1
# i =1
# while i*i<=sq:
#     if i*i==sq:
#         print(num," is a sunny")
#         break
#     i+=1
# else:
#     print(num," is not a sunny number")

# i = 1
# while i<=5:
#     print(i)
#     i+=1

# n = int(input("enter a Number : "))
# digit = n%10
# rev = n//10
# digit_2=rev%10
# sum=digit+rev
# print(sum)
# if n%sum==0:
#     print("Harshad Number")
# else:
#     print("Not harshad number")



# n = int(input("enter a Number : "))
# sum=0
# while n>0:
#     rev=n%10
#     sum+=n
#     n=n//10
# print(n)


# n = int(input("enter a Number : "))
# digit = n%10
# rev = n//10
# digit_2=rev%10
# sum=digit+rev
# print(sum)
# if sum*sum==n:
#     print("Harshad Number")
# else:
#     print("Not harshad number")

# for _ in range(5):
#     n = 5
#     s = 'A'
#     for _ in range(n):
#         print(s,end=" ")
#         s=chr(ord(s)+1)
#     print()


# n = 5
# s = 'A'
# for _ in range(5):
#     for _ in range(n):
#         print(s,end=" ")
#         s=chr(ord(s)+1)
#     print()


# n = 5
# for i in range(1,n+1):
#     print("*"*i)

# n = 5
# for i in range(6,-1,-1):
#     print("*"*i)

# n = 5
# for i in range(1,n+1):
#     print(" "*(n-i)+"*"*i)


# n = 5
# for i in range(1,n+1):
#     print(" "*(n-i)+"*"*i+"*"*(i-1))

# n = 5
# s = 'A'
# for i in range(1,n+1):
  
#     for i in range(1,n+1):
#         print(s,end=" ")
#         s=chr(ord(s)+1)
#     print()



# n = 5
# # s = 'A'
# for i in range(1,n+1):
#     s = 'A'
#     for i in range(i):
#         print(s,end=" ")
#         s=chr(ord(s)+1)
#     print()

# n = 5
# # s = "A"
# for i in range(1,n+1):
#     s = "A"
#     print(" "*(n-i),end=" ")
#     l=[]
#     for i in range(1,i+1):
#         l.append(s)
#         s=chr(ord(s)+1)
#     print(" ".join(l))


# n = 5
# # s = "A"
# for i in range(1,n+1):
#     print(" "*(n-i),end=" ")

#     for i in range(1,i):
#         print(i,end=" ")
#     print()

# n = int(input("Enter a Number :"))
# a,b=0,1
# for i in range(n):
#     print(a,end=" ")
#     a,b=b,a+b

# n = int(input("Enter a Number :"))
# for i in range(1,n+1):
#     if n%i==0:
#     
# l = []
# for n in range(2,51):
#     if n>2:
#         for i in range(2,n):
#             if n%i==0:
#                 break
#         else:
#             l.append(n)

# print(l)

# n = 5
# for i in range(1,n+1):
#     print(" "*(n-i),end=" ")
#     for i in range(1,i+1):
#         print(i,end=" ")
#     print()


# n = 5
# # s = "A"
# for i in range(1,n+1):
#     s = "A"
#     print(" "*(i),end=" ")
#     l=[]
#     for i in range(n-i+1):
#         l.append(s)
#         s=chr(ord(s)+1)
#     print(" ".join(l))



# n = int(input("Enter a Number :"))
# tem=n
# factorial = 1
# total=0
# for i in range(1,n+1):
#     factorial*=i
# print(factorial)
# while tem>0:
#     digit = tem%10
#     total +=factorial*digit
#     tem//=10
# if total==n:
#     print("Its perterson number")
# else:
#     print("You are wrong buddy")


# n = int(input("Enter a Number : "))
# sum = 0
# i = 1
# while i<=n:
#     if i%2==0:
#         sum+=i
#         print(sum)
#     i+=1

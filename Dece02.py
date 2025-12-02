# num = [1,2,3,4,5,6,7,8,9,10]
# num1 = ["Krish","Arjun","Vijay","Ravi","Ajay"]
# num.extend(num1)
# print(num)
# sum = 0
# for i in num:
#     sum=sum+i
# print(sum)


# n = 'Krish'
# print(list(n))

# a = 'hello world'
# print(a[1])

# a = [1,2,3,4,]
# for i in a:
#     if i%2==0:
#         a.remove(i)
# print(a)

# prime number between 1 to 50

for i in range(1,51):
    count=0
    for j in range(1,i+1):
        if i%j==0:
            count=count+1
    if count==2:
        print(i)


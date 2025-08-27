# how can you concate the string 
# a = "krish"
# b = "Gour"
# result = a + b
# print(result)

# how can you find the lenth of string
# there are two types of method 1.inbuilt 2.logic
# a = "Krish"
# print(len(a))

# a = "Krish"
# count = 0
# for i in a:
#     count +=1
# print(count)

# s = "GeeksforGeeks"
# l = 0
# for char in s:
#     l += 1
# print(l)



# splinting a string

# a = "Hello World"
# b = a.split(",")
# print(b)


# a = {1,2,3,3,4}
# print(type(a))



# a = {"name":"Krish","age":38}
# print(a["name"])
# print(a["age"])

# a=[1,2,3,4,5]
# b = [x**a for i in a]
# print(b)

# numbers = [1,2,3,4,5]
# squared_numbers = [x**3 for  x in numbers] 
# print(squared_numbers) 


# a = [1,2,3,4,5,6,7,8,9,10]
# b = [i for i in a if i%2!=0]
# print(b)

a = [i for i in range(1,51) if i%a!=0 for a in range(1,51-1) if i%a==0]
print(a)
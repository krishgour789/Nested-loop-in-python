# data Structure in Pyhton ?

# A data structure is a way to store and organize data so that it can be used efficiently.
# Example:
# If you want to store names in order → use a List
# If you want to store unique items → use a Set
# If you want fast lookup by key → use a Dictionary (HashMap)

# a = [1,2,3,4,5,6,7,8,9,10]
# print(a[0])    #indexing
# print(a[-1])

# Methods of List
# a.append(90)   # append can add the values in the last
# print(a)

# a.insert(2,25)    # it can insert the value in the list [postion,value]
# print(a)

#removing Elements

# a.remove(2)  #it can remove the values
# a.pop() # it remove the last value
# a.pop(2)   # it remove with indexing

# print(a[1:4]) # it can print the indexing from start to end
# a[0] = a[3]    # it use for updating
# print(a)
# 
# 
# 
#Create a list of 5 numbers and find the maximum and minimum without using max() or min().

# a = [1,2,3,4,5]
# print(max(a))   with the help of funtion we can find the biggest value in the list
# print(min(a))  #it use to find the smallest


# Reverse a list without using built-in reverse().
# print(a[ : :-1])


# Write a program to find the second largest number in a list.
# a.sort()
# second = a(2)
# print(a)
# b = set(a)
# a.sort()
# c=b[-2]
# print(c)




# Stack (LIFO Data Structure)
# stack work on last in first out{LIFO}

# from collections import deque
# stack=[]
# stack.append(10)
# stack.append(20)
# stack.append(30)

# stack.pop()
# stack.pop(-1)

# print(stack)

# to reverse a string 
a = "Hello"
print(a[::-1])
# i = 1
# while i<=10:
#     print(i)
#     i+=1

# l = ["Krish","Kanha","Rohan","Yadav"]
# for name in l:
#     if name.startswith("K"):
#         print(f"Hello",name)



# def average():
#     a = int(input("Enter a nummber :"))
#     b = int(input("Enter a nummber :"))
#     c = int(input("Enter a nummber :"))

#     average = (a+b+c)/3
#     print(average)
    
# average()
# average()
# average()
    


# a =[1,2,3,4,15,6,7,8,9,110]
# print(sorted(a))


# i = 0
# while i<=10:
#     if i%2==0:
#         print(i)
#         i+=1


# i = 1
# n = int(input("Enter a number :"))
# while i<=n:
#     if i%3==0:
#         print(i)
#     i+=1


# print(ord("A"))
# print(chr(23435))
# print(chr(23436))
# print(chr(23433))
# print(chr(23438))

# a = "my name is krish gour"
# print(a.title())

# String Methods....
# a = "welcome to bhopal"
# print(a.title())  # it can capital the first letter
# print(a.upper())    # it capitalize all the words
# print(a.capitalize()) # it capital the  first paragraph letter
# print(a.lower())    # it small the all words



# string methods
# isdigit(), isalpha(),isalnum()

# s = "krishgour789"
# print(s.isalnum())
# print(s.isalpha())
# print(s.isdigit())




# a = "krkkish"
# print(a.count("k"))  # it can count the the letters 


# s = "Welcome to bhopal"
# print(s.replace("to","in"))
# print(s.replace("l","p"))
# print(s.replace(" ",""))


# print(s.find("W"))
# print(s.index("o"))  it cannot work in some places like set and tuples


# i = 0
# sum=0
# while i<10:
#     print(i)
#     i+=1
#     sum+=i
# print("The sum is",sum)


# i = 0
# while i<=6:
#     print(i,"is no of time of loops")
#     i+=1
# print(i,"is the final value")


# l = [10,20,30,40]
# maxelement=l[0]
# for i in l:
#     if i > maxelement:
#         maxelement=i
# print(maxelement)



# l = [10,20,30,40]
# sum = 0
# a = len(l)
# for i in l:
#     sum+=i
#     average = sum//a
# print(average)

    
    
# a = [10,30,30,5089,478873,3298]
# sum = 0
# for i in a:
#     sum+=i
# print(sum)



# l = ['abc','xyz','aba','1221']
# count = 0
# for i in l:
#     if len(i)>2 and i[0]==i[-1]:
#         count += 1
# print(count)



# l = [100,1,200,19]
# for i in range(len(l)):
#         for j in range(i+1,len(l)):
#                 if l[i]>l[j]:
#                         l[i],l[j]=l[j],l[i]
                
# print(l)




# {'red:2,yellow:1}

# a = ["Red","Yellow","Green","Red","Red"]
# d={}
# for i in a :
#     if i in d:
#         d[i] += 1
#     else:
#         d[i] = 1
#     print(d)

# a = [0,1,2,3,4,5]
# d = {}
# for i in a:
#     if i in d:
#         #  d[chr(65+i)]=i**2
#         d[i] += 1
#     else:
#         d[chr(65+i)] = i*i
# print(d)

s1 = "ans" 
s2 = "nsz"

ans1 = {}
ans2 = {}

if len(s1) != len(s2):
    print("Not an anagram")
else:
    for i in s1:
        ans1[i] = ans1.get(i,0)+1

    for i in s2:
        ans2[i] = ans2.get(i,0)+1
    
    if ans1 == ans2:
        print("anagram")
    else:
        print("NOt an anagram")
    






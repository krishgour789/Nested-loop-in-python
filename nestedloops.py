# n = 5
# for i in range(n):
#     for j in range(n):
#         print("*",end=" ")
#     print()
# * * * * * 
# * * * * * 
# * * * * * 
# * * * * * 
# * * * * * 

# n = 5
# for i in range(n):
#     for j in range(i+1):
#         print("*",end=" ")
#     print()
# * 
# * * 
# * * *
# * * * *
# * * * * *

# n = 5
# for i in range(n):
#     for j in range(n-1-i):
#         print("*",end=" ")
#     print()
# * * * * 
# * * * 
# * *
# *



# n = 5
# for i in range(n):
#     for k in range(n-i):
#         print("*",end=" ")
#     for k in range(i):
#         print(" ",end=" ")
#     for j in range(i):
#         print(" ",end=" ")
#     for j in range(n-i):
#         print("*",end=" ")
#     print()
# * * * * * * * * * * 
# * * * *     * * * * 
# * * *         * * *
# * *             * *
# *                 *

# n = 5
# for i in range(n):
#     for j in range(n-1-i):
#         print(" ",end=" ")
#     for j in range(i+1):
#         print("*",end=" ")
#     print()
#         * 
#       * * 
#     * * *
#   * * * *
# * * * * *


# Printing the Praymid with th help of direct.
# n = 5
# for i in range(n):
#     for j in range(n-1-i):
#         print(" ",end=" ")
#     for j in range(2*i+1):
#         print("*",end=" ")
#     print()

# n = 10
# for i in range(n):
#     for j in range(n-1-i):
#         print(" ",end=" ")
#     for j in range(i+1):
#         print("*",end=" ")
#     for j in range(i):
#         print("*",end=" ")
#     print()
#         * 
#       * * * 
#     * * * * *
#   * * * * * * *
# * * * * * * * * *




n = 6
for i in range(n):
    for k in range(n-i):
        print("*",end=" ")
    for k in range(i):
        print(" ",end=" ")
    for j in range(i):
        print(" ",end=" ")
    for j in range(n-i):
        print("*",end=" ")
    print()
n= 6
for i in range(n):
    for l in range(i+1):
        print("*",end=" ")
    for l in range(n-1-i):
        print(" ",end=" ")
    for m in range(n-1-i):
        print(" ",end=" ")
    for m in range(i+1):
        print("*",end=" ")
    print()

# n=5
# for i in range(n):
#     for j in range(i):
#         print(" ",end=" ")
#     for j in range(n-i):
#         print("*",end=" ")
#     print()
# * * * * * 
#   * * * * 
#     * * *
#       * *
#         *

# n = 10
# for i in range(n):
#     for j in range(i):
#         print(" ",end=" ")
#     for j in range(n-i):
#         print("*",end=" ")
#     for j in range(n-i-1):
#         print("*",end=" ")    
#     print()
    


# n = int(input("Enter a Number :"))
# for i in range(n):
#     for j in range(n-i-1):
#         print(" ",end=" ")
#     for j in range(2*i+1):
#         print(chr(65+j),end=" ")
#     print()




# # making a hollo praymid :

# n = 5
# for i in range (n):
#     for j in range(n-1-i):
#         print(" ",end=" ")
#     for j in range(2*i+1):
#         if j == 0 or j == 2*i or i == n-1:
#             print("*",end=" ")
#         else:
#             print(" ",end=" ")
#     print()




# n = 6
# for i in range(n):
#     for j in range(n-1-i):
#         print(" ",end=" ")
#     for j in range(i+1):
#         print("*",end=" ")
#     for j in range(i):
#         print("*",end=" ")
#     print()
# n=6
# for i in range(n):
#     for j in range(i+1):
#         print(" ",end=" ")
#     for j in range(n-i-2):
#         print("1",end=" ")
#     for k in range(n-i-1):
#         print("#",end=" ")
#     print()




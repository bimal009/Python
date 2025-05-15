# 1.Write a program to print multiplication table of a given number using for loop.

# num = int(input("entre a number for multipication"))

# for i in range (1,11):
#     print(f"{num}*{i}={num*i}")


# 2.Write a program to greet all the person names stored in a list ‘l’ and which start with 'S'

# l = ["Harry", "Soham", "Sachin", "Rahul"]
# l.sort()

# for name in l:
#     if name.startswith("S"):
#         print("Hello " + name)


# # 3. Attempt problem 1 using while loop.
# num = int(input("entre a number for multipication"))
# i=1
# while i <=10:
#     print( i* num)
#     i+=1


# : Write a program to print the content of a list using while loops.
# l = ["Harry", "Soham", "Sachin", "Rahul"]
# i=0
# while i<l.__len__():
#     print(l[i])
#     i+=1
    



# Write a program to find whether a given number is prime or not.
# num = int(input("entre a number to check it prime or not:"))


# if num <= 1:
#     print("Number is not prime")
# else:
#     for i in range(2, num):
#         if num % i == 0:
#             print("Number is not prime")
#             break
#     else:
#         # This else belongs to the for loop; it runs if no break occurred
#         print("Number is prime")



# Write a program to find the sum of first n natural numbers using while loop
# num = int(input("entre a number for sum"))
# sum=0
# i=1
# while i <=num:
#     sum+=i
#     i+=1
#     print(sum)


# Write a program to calculate the factorial of a given number using for loop.
# num = int(input("entre a number for sum"))
# product =1

# for i in range(1,num+1):
#     product = product*i
#     print(product)
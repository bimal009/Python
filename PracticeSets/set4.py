
# # Write a program to create a dictionary of Hindi words with values as their English
# # translation. Provide user with an option to look it up!
# dect ={
#     "namaste":"hello",
#     "kya hal": "whatsup",
#     "badiya":"i am fine"


# }

# word = input("entre the word you want to translate:")
# print(dect[word]) # prints the value if the word exists other wise throws the error
# print(dect.get(word))# prints the value if the word exists other wise throws none

# # print(dect.keys())
# # print(dect.values())

# # dect.update({"badiya":"good","hello":"kya hal"})
# # print(dect.values())
# # print(dect.items())
# # print(dect.get("namaste"))



# Write a program to input eight numbers from the user and display all the unique
# numbers (once).

# s=set()
# n1=int(input("entre a number"))
# s.add(n1)
# n2=int(input("entre a number"))
# s.add(n2)
# n3=int(input("entre a number"))
# s.add(n3)
# n4=int(input("entre a number"))
# s.add(n4)
# n5=int(input("entre a number"))
# s.add(n5)
# n6=int(input("entre a number"))
# s.add(n6)
# n7=int(input("entre a number"))
# s.add(n7)
# n8=int(input("entre a number"))
# s.add(n8)

# print(s)

# Can we have a set with 18 (int) and '18' (str) as a value in it?

# s={18,"18"}
# print(type(s) , s)
# yes


# What will be the length of following set s:
# s = set()
# s.add(20)
# s.add(20.0)
# s.add('20') 

# print(s.__len__(),s)
# 2 {'20', 20}



# Create an empty dictionary. Allow 4 friends to enter their favorite language as
# value and use key as their names. Assume that the names are unique.


# lang={}

# name1,language1 =input("entre your name and language(seperate by the space):").split()
# lang.update({name1:language1})
# name2,language2 =input("entre your name and language(seperate by the space):").split()
# lang.update({name2:language2})
# name3,language3 =input("entre your name and language(seperate by the space):").split()
# lang.update({name3:language3})
# name4,language4 =input("entre your name and language(seperate by the space):").split()
# lang.update({name4:language4})
# print(lang)


# If the names of 2 friends are same; what will happen to the program in problem
# 6?
#Dictionaries in Python cannot have duplicate keys.
# So if two friends enter the same name, the second entry will overwrite the first one.

# If languages of two friends are same; what will happen to the program in problem
# 6?
# Nothing wrong — the program works perfectly fine.

# Why? Because in a Python dictionary:

# Keys must be unique → names in your case.

# Values can be duplicated → languages can be the same


# Can you change the values inside a list which is contained in set S?

# s = {8, 7, 12, "Harry", [1,2]}

# python sets can only contain hashable (immutable) types.

# ✅ Allowed: int, str, float, tuple, etc.

# ❌ Not Allowed: list, dict, set (because they are mutable)
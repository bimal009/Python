# Write a program to print yes when the age entered by the user is greater
# than or equal to 18.


# num= int(input("entre a number:"))
# if num>=18:
#     print("yes")
# else:
#     print("no")


# Write a program to find the greatest of four numbers entered by the user
# num1=int(input("Entre your First Number:"))
# num2=int(input("Entre your Second Number:"))
# num3=int(input("Entre your third Number:"))
# num4=int(input("Entre your fourth Number:"))


# if num1 > num2 and num1 > num3 and num1 > num4:
#     print("num1 is greater")
# elif num2 > num1 and num2 > num3 and num2 > num4:
#     print("num2 is greater")
# elif num3 > num1 and num3 > num2 and num3 > num4:
#     print("num3 is greater")
# elif num4 > num1 and num4 > num2 and num4 > num3:
#     print("num4 is greater")



# Write a program to find out whether a student has passed or failed if it requires a
# total of 40% and at least 33% in each subject to pass. Assume 3 subjects and
# take marks as an input from the user.

# mark1=int(input("entre marks 1: "))
# mark2=int(input("entre marks 2: "))
# mark3=int(input("entre marks 3: "))

# total_marks = mark1 + mark2 + mark3
# percentage = (total_marks / 300) * 100


# if percentage >= 40 and mark1 >= 33 and mark2 >= 33 and mark3 >= 33:
#     print("you passed")
# else:print("you failed")



# A spam comment is defined as a text containing following keywords:
# “Make a lot of money”, “buy now”, “subscribe this”, “click this”. Write a program
# to detect these spams.

message=input("entre your message: ")

if( message == "Make a lot of money" or message == "buy now" or   "subscribe this" or message =="click this"  ):
    print("scam message diceted")
else:
    print("its safe")


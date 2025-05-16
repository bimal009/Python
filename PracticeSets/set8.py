# Write a program using functions to find greatest of three numbers
# def greatest(num1, num2, num3):
#     if num1 > num2 and num1 > num3:
#         return num1
#     elif num2 > num1 and num2 > num3:
#         return num2
#     else:
#         return num3

# result = greatest(20, 30, 40)
# print("The greatest number is:", result)


# Write a python program using function to convert Celsius to Fahrenheit.

# def conv(cel):
#     fer=(cel * (9/5) + 32)
#     return fer


# res=conv(40)
# print("the celcius is:",res)\
    
    
    # How do you prevent a python print() function to print a new line at the end.
# print("hello",end="   ")
# print("world")


# Write a python function which converts inches to cms

# def conv(inches):
#     cm= (inches*2.54)
#     print("the cm is: " ,cm)


# conv(5)

def remove_and_strip(word_list, word_to_remove):
    return [word.strip() for word in word_list if word.strip() != word_to_remove]

# Example usage
words = ["  apple", "banana ", " orange ", "grape"]
cleaned = remove_and_strip(words, "orange")
print(cleaned)

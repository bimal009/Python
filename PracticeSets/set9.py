# Write a program to read the text from a given file ‘poems.txt’ and find out
# whether it contains the word ‘twinkle’.
# with open("poems.txt", "r") as f:
#     data = f.read()

# if "twinkle" in data.lower():
#     print("The word 'twinkle' is present in the file.")
# else:
#     print("The word 'twinkle' is NOT present in the file.")


# The game() function in a program lets a user play a game and returns the score
# as an integer. You need to read a file ‘Hi-score.txt’ which is either blank or
# contains the previous Hi-score. You need to write a program to update the Hiscore whenever the game() function breaks the Hi-score.

# import random

# def game():
#     score = random.randint(1, 100)
    
#     try:
#         with open("highscore.txt", "r") as f:
#             data = f.read()
#             highscore = int(data.strip()) if data.strip() else 0
#     except FileNotFoundError:
#         highscore = 0

#     if score > highscore:
#         print(f"You win! New high score: {score}")
#         with open("highscore.txt", "w") as f:  
#             f.write(str(score))
#     else:
#         print(f"You lose! Your score: {score}, High score: {highscore}")

# game()



# Write a program to generate multiplication tables from 2 to 20 and write it to the
# different files. Place these files in a folder for a 13 – year old.
# import os
# folder_name= "tables for 13 years old"
# os.makedirs(folder_name ,exist_ok=True)


# for i in range(2,21):
#     file_path= os.path.join(folder_name,f"Tables of {i}.txt")
#     with open(file_path,"w") as f:
#         for j in range (1,11):
#             f.write(f'{i}*{j}={i*j}\n')
    
    
    
    
#     A file contains a word donkey multiple times. You need to write a program
# which replace this word with ##### by updating the same file. 
# with open("text.txt", 'r') as f:
#     data = f.read()

# updated_data = data.replace("donkey", "#####")

# with open("text.txt", 'w') as f:
#     f.write(updated_data)


# Repeat program 4 for a list of such words to be censored.

# words_to_censor =["quietly","donkey","acting","repeating"]
# with open("text.txt","r") as f:
#     data= f.read()
       
# for bad_words in words_to_censor:
#     data=data.replace(bad_words,"######")
      
# with open("text.txt","w") as f:
#     f.write(data)


# Write a program to mine a log file and find out whether it contains ‘python’.
# word="python"
# with open("log.txt","r") as f:
#     data=f.read().lower()
   
#     if word in data:
#         print("python exists")
#     else:
#         print("python doesnt exists")
   
    
# Write a program to find out the line number where python is present from ques 6

# word="python"
# line_number=1
# with open("log.txt","r") as f:
#     lines=f.readlines()
#     print(lines)

# for line in lines:
#     if word in line:
#         print(line_number)
#         line_number+=1
    
#     else:
#         print("dosnot exists")


# Write a program to make a copy of a text file “this. txt”

# with open("this.txt","r")as f:
#     data=f.read()
    
# with open("thiscopy.txt","w")as f:
#     f.write(data)
    
# print("data copied sucessfull")



# Write a program to find out whether a file is identical & matches the content of
# another file.

# def checkFiles(file1,file2):
#     with open(file1,"r") as f1:
#         data1= f1.read()

#     with open(file2,"r") as f2:
#         data2= f2.read()
#     return data1 == data2



# file1 = "this.txt"
# file2 = "thiscopy.txt"

# if checkFiles(file1,file2):
#     print(f"{file1} and {file2} are identical.")
# else:
#     print(f"{file1} and {file2} are not identical.")
    
    
    # Write a program to wipe out the content of a file using python

    
# with open("this.txt","w") as f:
#     f.write("")

# print("File content wiped out successfully!")


# Write a python program to rename a file to “renamed_by_ python.txt.

import os
file_name="this.txt"
rename_to="renamed_by_ python.txt"
os.replace(file_name,rename_to)
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

words_to_censor =["quietly","donkey","acting","repeating"]
with open("text.txt","r") as f:
    data= f.read()
       
for bad_words in words_to_censor:
    data=data.replace(bad_words,"######")
      
with open("text.txt","w") as f:
    f.write(data)
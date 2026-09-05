# a = open("file1.txt" , "r")
# data = a.read()
# print(data)
# a.close()



# f = open("wirtefile.txt" , "w")
# story = f.write("This is a story")
# f.close()


with open("file1.txt" , "rt") as f:
    data=f.read()
    if "poem" in data:
        
        print("true")
    else:
        print("None")
    print(data)

import random

def game():
    print("You are playing a game... ")
    score = random.randint(1,110)
    with open("game_score.txt" , "r") as f:
        highscore = f.read()
        if highscore !="":
            highscore = int(highscore)
        else:
            highscore = 0
    print( f" Your Score is {score}")

    with open("game_score.txt" , "w") as f:
        if (score>highscore):
            data = f.write(str(score))


game()


# wordlist = ["poem" , "is" , "it"]

# with open("file1.txt" , "r") as f:
#     content = f.read()

# for word in wordlist:
#     content = content.replace(word , "###")

# with open("file1.txt" , "w") as f :
#     f.write(content)
 

with open("file1.txt" , "r") as f:
    content = f.readlines()

line_no = 1
for line in content:
    if "python" in line:
        print(f"Python is present in line no: {line_no}")
        break
    line_no += 1
else:
    print("Python is not present")






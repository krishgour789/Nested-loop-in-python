# f = open("file.txt")
# data = f.read()
# print(data)
# f.close()

# s = "krish is good boye"
# open("file2.text", "a")
# f = open("file2.text", "a")
# f.write(s)
# f.close()

import random
def game():
    print("Welcome to the Game")
    print("You are Playing the Game :")
    score = random.randint(1,50)
    with open("hiscore.txt") as f:
        hiscore = f.read()
        if hiscore=="":
            hiscore=int(hiscore)
        else:
            hiscore=0
    print(f"your score is : ",score)
    if score > hiscore:
        with open("hiscore.txt","w") as f:
            # s = "Your Highscore is :"
            # f.write(s)
            f.write(f"Your Highscore is :{str(score)}")
            print("New Highscore")
    return score
game()

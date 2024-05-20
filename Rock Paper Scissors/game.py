import random

def disp_score():               #shows the scoreboard after every round
    print(f"---------------------------\nScoreboard\nUser: {user_score} || CPU: {comp_score}\nRounds played: {rounds}\n---------------------------\n")

arr = [0,1,2]
dict = {
    0:"rock",
    1:"paper",
    2:"scissor",
}
words = {"r":"rock", "p":"paper", "s":"scissor"}   #for remapping the letters to respective words

resp = 'y'
user_score=0; comp_score=0; rounds = 0 

while (resp=="y"):
    #do stuff here
    user = words[input("enter choice rock paper scisssor: ").lower()[0]]
    comp = dict[random.randint(0,2)]
    if (user==comp):
        print("tie")

    elif (user=="rock" and comp=="paper"):
        print("you lose") 
        comp_score+=1

    elif (user=="rock" and comp=="scissor"):
        print("you win")
        user_score+=1

    elif (user=="paper" and comp=="scissor"):
        print("you lose")
        comp_score+=1

    elif (user=="paper" and comp=="rock"):
        print("you win")
        user_score+=1

    elif (user=="scissor" and comp=="rock"):
        print("you lose")
        comp_score+=1

    elif (user=="scissor" and comp=="paper"):
        print("you win")
        user_score+=1

    disp_score()
    # if (user=="rock"):
    resp = input("do you wish to conitnue (y/n)")
    if resp.lower() != 'y':
        break
print("end")
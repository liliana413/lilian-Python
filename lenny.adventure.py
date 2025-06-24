name = input("Type your name: ")

print("welcome to lenny adventure!")

answer = input("you are in the middle of dark road. do you want to go left or right? (left/right): ").lower()
if answer =="left":
    answer = input("you encounter an abandoned bus. do you want to enter or walk around or go back? (enter/walk/back): ").lower()
    if answer=="enter":
        print("you found snake and got bitten by it and died. you lose!")

    elif answer == "walk":
        answer = input("you found a hidden path. do you want to follow it or go back to the bus? (follow/back):").lower()
        if answer == "follow":
            print("you found a hidden cave and found treasure! you win!")

        elif answer == "back":
            print ("you went back to the bus and got lost. you lose!")
        else:
            print("not a valid option. you lose!")

if answer == "right":
    answer = input("you encounter a river. do you want to smim across or wait for a bus or go back? (smim/wait/back):") . lower()
    if answer == "swim":
        print("you swim across the river and you found a crocdile and it ate you. you lose!")

    elif answer == "wait":
        print("a bus arrives,bus captain is drunk and he crashes the bus and you die. you lose!")

    elif answer == "back":
        print("you went back and found a hidden path and you followed it and found a hidden village and made new friends! you win!")
    else:
        print("not a valid option. you lose!")

        print("game over.thanks for playing,see you next time, take care " + name + "!")


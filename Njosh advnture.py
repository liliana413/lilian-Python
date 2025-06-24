name = input("type your name: ")
print("Welcome to Njosh adventure!")

answer = input("You are in a dark forest. Do you want to go left or right? (left/right): ").lower()

if answer == "left":
    answer = input("You encounter a river. Do you want to swim across or wait for a boat? (swim/wait): ").lower()
    
    if answer == "swim":
        print("You swam across the river and found treasure! You win!")
    elif answer == "wait":
        print("A boat arrives, but it's full. You lose!")
    else:
        print("Not a valid option. You lose.")


elif answer == "right":
    answer = input("You encounter a cave. Do you want to enter or walk around? (enter/walk): ").lower()
    if answer == "enter":
        print("You get eaten by a lion. You lose!")

    elif answer == "walk":
        answer = input("You find a hidden path. Do you want to follow it or go back to the cave? (follow/back): ").lower()
        if answer == "follow":
            print("You found a hidden village and made new friends! You win!")
        elif answer == "back":
            print("You went back to the cave and get lost. You lose!")
        else:
            print("Not a valid option. You lose.")

print("Game over. Thanks for playing, " + name + "!")




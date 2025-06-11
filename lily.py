import random

def number_guesser():
    number_to_guess = random.randint(1, 100)
    attempts = 0

    print("Welcome to Number Guesser!")
    print("I'm thinking of a number between 1 and 100.")

    while True:
        try:
            guess = int(input("take a guesse: "))
            attempts += 1

            if guess < number_to_guess:
                print("Too low!")
            elif guess > number_to_guess:
                print("Too high!")
            else:
                print(f"Congratulations! You guessed it in {attempts} attempts.")
                break
        except ValueError:
            print(" Please enter a valid integer.")

if __name__ == "__main__":
    number_guesser()
    
    continue_game =input("do you want to play again? (yes?no): ").strip().lower()


    
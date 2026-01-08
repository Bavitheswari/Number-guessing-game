import random

def play_game():
    secret_number = random.randint(1, 100)
    attempts = 0
    max_attempts = 5

    print("\nI have selected a number between 1 and 100.")
    print("You have 5 attempts to guess it.")

    while attempts < max_attempts:
        guess = int(input("Enter your guess: "))
        attempts += 1

        if guess > secret_number:
            print("Too high!")
        elif guess < secret_number:
            print("Too low!")
        else:
            print(f"🎉 Correct! You guessed it in {attempts} attempts.")
            return

        print(f"Remaining attempts: {max_attempts - attempts}")

    print(f"😢 Game over! The number was {secret_number}")

while True:
    play_game()
    again = input("Do you want to play again? (yes/no): ").lower()
    if again != "yes":
        print("Thanks for playing!")
        break

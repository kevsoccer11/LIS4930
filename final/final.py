import random

# Function to select, ope, and read file with a list of words


def selected_words(file_name):
    file_name = open(file_name)
    random_word = random.choice(file_name.read().split())
    file_name.close()
    return random_word

# Function to get user input on whether or not they would like to play again.


def play_again():
    play_again = input("Would you like to play another game? (Y/N) ").upper()
    if play_again == "Y":
        main()
    elif play_again == "N":
        print("Thank you for playing, goodbye.")
    while play_again != "Y" and play_again != "N":
        print("Please enter a valid answer. (Y/N)")
        print()
        play_again = input(
            "Would you like to play another game? (Y/N) ").upper()
        if play_again == "Y":
            main()
        elif play_again == "N":
            print("Thank you for playing, goodbye.")

# main


def main():

    # select a word from the list at random
    random_word = selected_words("words.txt")
    # create an empty list to store the letters that have been guessed
    guessed_letters = []
    # tract guesses made
    guesses = 0
    # heart symbol to represent lives remaining
    heart_symbol = "\u2764\ufe0f "
    # added 3 lives to the length of the word to determine lives at the beginning
    lives = len(random_word) + 3
    # get username
    user_name = input("\nHello, please enter your name: \n").upper()
    # greeting user and general information about the guessing game
    print(
        f"Welcome {user_name}, let's begin the word guessing game! Good Luck!!!\n")
    print(f"The word you are guessing has {len(random_word)} letters.\n")
    # display lives
    print("Lives: ")
    print("______")
    print(f"\n{(lives * heart_symbol)}\n")
    # create a variable to store and display guesses
    display_guesses = random_word
    for i in range(len(display_guesses)):
        # replace each letter with a '_'
        display_guesses = display_guesses[0:i] + "_" + display_guesses[i+1:]
    print(" ".join(display_guesses))

    # keep asking the player untill all letters are guessed

    while display_guesses != random_word and lives != 0:
        user_entry = input("\nPlease enter a letter: ")
        user_entry = user_entry.lower()
        # add the players guess to the list of guessed letters
        guessed_letters.extend(user_entry)
        print(f"{lives} lives remaining: ")

        # search through the letters in answer
        if user_entry in random_word:
            print("Correct!")

            for i in range(len(random_word)):
                if random_word[i] == user_entry:
                    display_guesses = display_guesses[0:i] + \
                        user_entry + display_guesses[i+1:]
        # reduce lives if entry is incorrect
        elif user_entry not in random_word:
            print("\nwrong!\n")
            lives -= 1
        # display lives
        print("Lives: ")
        print("______")
        print(f"\n{(lives * heart_symbol)}\n")
        # display letters that were already guessed
        print("Guessed letters : \n")
        print(guessed_letters)
        guesses += 1

        # join guessed letters with a space in between
        print(" ".join(display_guesses))
    # display outcome if the user ran out of lives
    if(lives == 0):
        print("You ran out of tries. Better luck next time.")
        # call function to ask user if they would like to play again
        play_again()
    # display congrats if the user guessed the word correctly
    elif(display_guesses == random_word):
        print(
            f"\nWell done {user_name}, you guessed the correct word!! {random_word.upper()}\n")
        print(
            f"It took you {guesses} tries and you had {lives} lives remaining!!")
        # call function to ask user if they would like to play again
        play_again()


main()

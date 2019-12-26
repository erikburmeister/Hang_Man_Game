import random
import csv
import string


def hang_man_0():
    print("______")
    print("|    ")
    print("|    ")
    print("|    ")
    print("|    ")
    print("|_________________")
    print("|Attempts left: 7|")


def hang_man_1():
    print("______")
    print("|    |")
    print("|     ")
    print("|     ")
    print("|     ")
    print("|_________________")
    print("|Attempts left: 6|")


def hang_man_2():
    print("______")
    print("|    |")
    print("|    O")
    print("|     ")
    print("|     ")
    print("|_________________")
    print("|Attempts left: 5|")


def hang_man_3():
    print("______")
    print("|    |")
    print("|    O")
    print("|    |")
    print("|     ")
    print("|_________________")
    print("|Attempts left: 4|")


def hang_man_4():
    print("______")
    print("|    |")
    print("|    O")
    print("|   /|")
    print("|     ")
    print("|_________________")
    print("|Attempts left: 3|")


def hang_man_5():
    print("______")
    print("|    |")
    print("|    O")
    print("|   /|\\")
    print("|     ")
    print("|_________________")
    print("|Attempts left: 2|")


def hang_man_6():
    print("______")
    print("|    |")
    print("|    O")
    print("|   /|\\")
    print("|   / ")
    print("|_________________")
    print("|Attempts left: 1|")


def hang_man_7():
    print("______")
    print("|    |")
    print("|    O")
    print("|   /|\\")
    print("|   / \\")
    print("|_________________")
    print("|    You Lose.   |")


def hang_man_win():
    print("______")
    print("|     ")
    print("|     ")
    print("|    O")
    print("|   /|\\")
    print("|___/_\\__________")
    print("|    You Won!    |")


def hang_man_art(number):
    if number == 0:
        hang_man_0()
    elif number == 1:
        hang_man_1()
    elif number == 2:
        hang_man_2()
    elif number == 3:
        hang_man_3()
    elif number == 4:
        hang_man_4()
    elif number == 5:
        hang_man_5()
    elif number == 6:
        hang_man_6()


def decorated_text(msg, deco, deco_2):
    message = msg
    decoration = deco
    decoration_2 = deco_2

    print(decoration * (len(message) + 4))
    print(decoration_2 + " " + message + " " + decoration_2)
    print(decoration * (len(message) + 4))


def instructions():
    instruction_choice = "placeholder"

    instructions_text = """Instructions:
The number of spaces represent
the amount of letters in the 
word that needs to be guessed.

Guess a letter in the alphabet.
if you guess a letter that is
in the word, a letter will
take the place of the blank.

If you guess incorrectly, a
section of the hang man will
appear. You have 7 attempts
before the hang man is
completed. Once it is complete
the game is over and you lose.

Do your best to guess the word
with the lowest amount of
guesses."""

    misunderstood = """I did not catch that.
Did you want to see the
instructions to the game?
Answer 'yes' or 'no'"""

    while not instruction_choice == "y" and not instruction_choice == "n":

        instruction_choice = input("Want to read the instructions? ").lower()

        if instruction_choice == "":
            continue

        if instruction_choice[0] == "y":
            print()
            print(instructions_text)
            print()
            break

        elif instruction_choice[0] == "n":
            print()
            break

        else:
            print()
            print(misunderstood)
            print()


def replay():
    play_again = "placeholder"

    while not play_again == "y" and not play_again == "n":

        play_again = input("Would you like to play again? ")
        print()

        if play_again == "":
            continue

        if play_again[0] == "y":
            return True

        elif play_again[0] == "n":
            return False


def choose_word_length():

    decorated_text("The Hang Man Game", "*", "*")

    instructions()

    print("""Select the difficulty of the game by 
choosing a word with more letters. 
The options are 5 letter words,
6 letter words, and 7 letter words.

Type the number of letters you want
the word to be. 

5 = EASY
6 = MEDIUM
7 = HARD
""")
    
    difficulty = ['5', '6', '7']
    
    word_length_answer = "placeholder"
    
    while not word_length_answer in difficulty:
    
        word_length_answer = input("What difficulty would you like? ")
        print()

    return int(word_length_answer)


def word_selector(number):
    word_bank = {
        5: ["above", "beast", "crawl", "ember", "freak"],
        6: ["advice", "cipher", "deluxe", "glitch", "zombie"],
        7: ["beneath", "cashier", "endgame", "monster", "strange"],
    }
    
    return word_bank[number][random.choice(range(0,len(word_bank[number])))]


def alphabet():
    alpha = list(string.ascii_lowercase)
    return alpha


def guess_checker(word, letter):
    word_to_guess = list(word)

    if letter in word_to_guess:
        print("Correct!")
    else:
        print("Wrong.")


def the_hang_man_game(number):

    alpha = alphabet()

    used_alpha = []

    letters_in_word_list = []

    word_to_guess = word_selector(number)

    list_word_to_guess = list(word_to_guess)

    space_counter = 0

    player_guess_counter = 0

    player_guess = 'placeholder'

    game_on = True

    for x in word_to_guess:
        letters_in_word_list.append("_")

    while game_on:

        if game_on:
            print("Available letters: \n" + "[ " + " ".join(alpha) + " ]")
            print()
            print("Used Letters: \n" + "[ " + " ".join(used_alpha) + " ]")

        hang_man_art(player_guess_counter)
        print()
        print(" ".join(letters_in_word_list))
        print()

        player_guess = input("Guess a letter: ").lower()

        if player_guess == "9":
            print()
            break

        guess_checker(word_to_guess, player_guess)
        print()

        for letter in list_word_to_guess:
            space_counter += 1

            if letter == player_guess:
                letters_in_word_list.pop(space_counter - 1)
                letters_in_word_list.insert((space_counter - 1), letter)

        if player_guess in set(word_to_guess):
            player_guess_counter -= 1

        space_counter = 0
        player_guess_counter += 1

        if player_guess_counter < 0:
            player_guess_counter = 0

        try:
            alpha.remove(player_guess)
        except ValueError:
            if player_guess in used_alpha:
                print("You already used the letter '" + player_guess + "'")
                print()
            else:
                print("That's not a letter...")
                print()
        else:
            used_alpha.append(player_guess)

        if player_guess_counter == 7 or (list_word_to_guess == letters_in_word_list):
            if list_word_to_guess == letters_in_word_list:
                hang_man_win()
                print()
                print("You got it! \nThe word was: " + word_to_guess)
                print()

            if player_guess_counter == 7:
                hang_man_7()
                print()
                print("Maybe next time. \nThe word was: " + word_to_guess)
                print()
                print()

            game_on = replay()
            if game_on == True:
                alpha = alphabet()
                used_alpha = []
                player_guess_counter = 0
                letters_in_word_list = []
                word_to_guess = word_selector(choose_word_length())
                list_word_to_guess = list(word_to_guess)
                for x in word_to_guess:
                    letters_in_word_list.append("_")

    decorated_text("Thanks for playing!", "*", "*")


if __name__ == "__main__":
    the_hang_man_game(choose_word_length())

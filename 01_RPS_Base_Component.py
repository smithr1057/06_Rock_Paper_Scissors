import random


# Functions

# Asks users how many round they want to play
def check_rounds():
    while True:
        response = input("How many rounds: ")

        round_error = "Please type either <enter> " \
                      "or an integer that is more than 0\n"

        # If infinite mode not chosen, check response
        # is an integer that is more than 0
        if response != "":
            try:
                response = int(response)

                # If response is to low print error and
                # restart the loop

                if response < 1:
                    print(round_error)
                    continue

            except ValueError:
                print(round_error)
                continue

        return response


# checks user answers with valid answer
def choice_checker(question, valid_list, error):
    while True:
        # Ask user for choice (and put it in lowercase)
        response = input(question).lower()

        # iterates through list and if response is an item
        # in the list (or the first letter of an item), the
        # full item name is returned

        for item in valid_list:
            if response == item[0] or response == item:
                return item

        # output error if item not in list
        print(error)
        print()


# Displays instructions
def instructions():
    print("**** How to Play ****")
    print()
    print("Enter how many rounds you would like to play.")
    print("Press <enter> for continuous mode.")
    print("You can quit at any time by typing in 'xxx'.")
    print("Choose rock, paper, scissors or r, p, s.")
    print("You can choose to see your end game summary at the end of the game.")
    print("Good luck and have fun :D")
    print()
    return ""


# Adds decorations to selected text
def statement_generator(statement, decoration):
    sides = decoration * 3

    statement = f"{sides} {statement} {sides}"
    top_bottom = decoration * len(statement)

    print(top_bottom)
    print(statement)
    print(top_bottom)

    return ""


# Main Routine

# List of valid responses
yes_no_list = ["yes", "no", "y", "n"]
rps_list = ["rock", "paper", "scissors", "xxx"]
game_summary = []

# Error
error = "Please enter either yes or no"
# Title
statement_generator("Welcome to the Rock Paper Scissors Game", "*")
print()

# Ask user if they have played before
# If 'yes', show instructions
played_before = choice_checker("Have you played the game before? "
                               , yes_no_list,
                               error)

if played_before == "no":
    instructions()

# Ask user for # of rounds then loop...
rounds_played = 0
rounds_lost = 0
rounds_drawn = 0

game_summary = []

# Ask user for # of rounds, <enter> for infinite mode
rounds = check_rounds()

end_game = "no"
while end_game == "no":

    # Start the game play loop

    # Rounds Heading
    if rounds == "":
        heading = f"*** Continuous Mode: Round" \
                  f" {rounds_played + 1} ***"
    else:
        heading = f"*** Round {rounds_played + 1}" \
                  f" of {rounds} ***"

    print(heading)
    print()
    choose_instruction = "Please choose rock, paper" \
                         ", scissors or 'xxx' to exit: "
    choose_error = "Please choose from rock / paper / " \
                   "scissors (or xxx to quit): "

    # Ask user for choice and check it's valid
    choose = choice_checker(choose_instruction, rps_list, choose_error)
    print(f"You Chose {choose}")

    # End game if exit code is typed
    if choose == "xxx":
        break

    # get computer choice
    comp_choice = random.choice(rps_list[:-1])
    print("Computer Chose", comp_choice)

    # Compare choices
    if choose == comp_choice:
        result = "Tie"
        rounds_drawn += 1

    elif choose == "rock" and comp_choice == "scissors":
        result = "Won"

    elif choose == "paper" and comp_choice == "rock":
        result = "Won"

    elif choose == "scissors" and comp_choice == "paper":
        result = "Won"

    else:
        result = "Lost"
        rounds_lost += 1

    # Quick calculations
    rounds_won = rounds_played - rounds_lost - rounds_drawn
    if result == "Lost":
        print("You lost, better luck next time")

    elif result == "Won":
        print("You won, congrats")

    else:
        print("Its a tie")

    outcome = f"Round {rounds_played + 1}: {result}"
    game_summary.append(outcome)
    print()

    # rest of loop / game

    rounds_played += 1

    # End game if requested # of rounds has been played
    if rounds_played == rounds:
        break

# Checks user has played a round
# Ask if they want to view game history
if rounds_played > 1:
    # Ask user if they want to see their game history
    # if 'yes' show game history
    show_stats = choice_checker("Would you like to see your"
                                " end game history? "
                                , yes_no_list, error)

    # Calculate stats and print them out
    if show_stats == "yes":

        rounds_won = rounds_played - rounds_lost - rounds_drawn

        # Calculate game stat
        percent_win = rounds_won / rounds_played * 100
        percent_lose = rounds_lost / rounds_played * 100
        percent_tie = rounds_drawn / rounds_played * 100

        # Displays game history
        print()
        print("***** Game History *****")
        for game in game_summary:
            print(game)

        print()

        # displays game stats with % values to the nearest whole number
        print(" ***** Game Statistics *****")
        print(f"Win: {rounds_won}, {percent_win:.0f}% \nLoss: {rounds_lost}, "
              f"{percent_lose:.0f}% \nTie: {rounds_drawn}, {percent_tie:.0f}%")

    print()
    print("Thanks for playing rock paper scissors :D")

# If user hasn't played a round comment
# Don't give them the option of game history
elif rounds_played < 1:
    print("Maybe play the game next time :)")

import random


# Functions
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


# Main Routine

# List of valid responses
yes_no_list = ["yes", "no"]
rps_list = ["rock", "paper", "scissors", "xxx"]

# Ask user if they have played before
# If 'yes', show instructions


# Ask user for # of rounds then loop...
rounds_played = 0


# Ask user for # of rounds, <enter> for infinite mode
rounds = check_rounds()

end_game = "no"
while end_game == "no":

    # Start the game play loop

    # Rounds Heading
    if rounds == "":
        heading = f"Continuous Mode: Round" \
                  f" {rounds_played + 1}"
    else:
        heading = f"Round {rounds_played + 1}" \
                  f" of {rounds}"

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
        result = "Its a draw"

    elif choose == "rock" and comp_choice == "scissors":
        result = "Congrats you won"

    elif choose == "paper" and comp_choice == "rock":
        result = "Congrats you won"

    elif choose == "scissors" and comp_choice == "paper":
        result = "Congrats you won"

    else:
        result = "You lost better luck next time)"

    print(f"{result}")

    # rest of loop / game

    rounds_played += 1

    # End game if requested # of rounds has been played
    if rounds_played == rounds:
        break


# Ask user if they want to see their game history
# if 'yes' show game history

# Show game statistics

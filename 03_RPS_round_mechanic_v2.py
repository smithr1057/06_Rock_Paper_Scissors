# Main routine more efficient than v1


# Functions
def check_rounds():

    while True:
        response = input("How many rounds: ")

        round_error = "Please type either <enter> " \
                      "or an integer that is more than 0"
        if response != "":
            try:
                response = int(response)

                if response < 1:
                    print(round_error)
                    continue

            except ValueError:
                print(round_error)
                continue

        return response


# Main routine


rounds_played = 0
choose_instruction = "Please choose rock (r), paper" \
                     "(p), scissors (s)"

# Ask user for # of rounds, <enter> for infinite mode
rounds = check_rounds()

end_game = "no"
while end_game == "no":

    # Rounds Heading
    print()
    if rounds == "":
        heading = f"Continuous Mode: Round" \
                  f" {rounds_played + 1}"
    else:
        heading = f"Round {rounds_played + 1}" \
                  f" of {rounds}"

    print(heading)
    choose = input(f"{choose_instruction} or "
                   f"'xxx' to end: ")

    # End game if exit code is typed
    if choose == "xxx":
        break

    # rest of loop / game
    print(f"You chose {choose}")

    rounds_played += 1

    # End game if requested # of rounds has been played
    if rounds_played == rounds:
        break

print("Thank you for playing")

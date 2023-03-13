rps_list = ["rock", "paper", "scissors"]
comp_index = 0
for item in rps_list:
    user_index = 0
    for item in rps_list:
        user_choice = rps_list[user_index]
        comp_choice = rps_list[comp_index]
        user_index += 1

        # Compare options
        if user_choice == comp_choice:
            result = "Draw"

        elif user_choice == "rock" and comp_choice == "paper":
            result = "The Computer Won"

        elif user_choice == "paper" and comp_choice == "scissors":
            result = "The Computer Won"

        elif user_choice == "scissors" and comp_choice == "rock":
            result = "The Computer Won"

        else:
            result = "Congrats you Won"

print(f"You chose {user_choice}")
print(f"The computer chose {comp_choice}")
print(f"Result {result}")

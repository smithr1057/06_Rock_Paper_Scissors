# Functions go here
def choice_checker(question):

    error = "Please choose from rock / paper / scissors (or xxx to quit)"

    while True:
        response = input(question).lower()
        print()

        if response == "rock" or response == "r":
            return "rock"

        if response == "paper" or response == "p":
            return "paper"

        elif response == "scissors" or response == "s":
            return "scissors"

        elif response == "xxx":
            return response

        else:
            print("*** Error please enter either rock, paper or scissors ***")
            print()


# Main routine goes here


# Loop for testing purposes
user_choice = ""
while user_choice != "xxx":

    # Ask user for choice and check it's valid
    user_choice = choice_checker("Choose rock / paper / scissors (r/p/s):  ")

    # Print out choice for comparison purposes
    print(f"You chose {user_choice}")

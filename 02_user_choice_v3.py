# version  - uses a list for checking the response


# Functions go here
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

# Main routine goes here


# Lists for checking responses
rps_list = ["rock", "paper", "scissors", "xxx"]


# Loop for testing purposes
user_choice = ""
while user_choice != "xxx":

    # Ask user for choice and check it's valid
    user_choice = choice_checker("Choose rock / paper / "
                                 "scissors (r/p/s): ", rps_list,
                                 "***Error*** please choose "
                                 "from rock / paper "
                                 "/ scissors (or xxx to quit)")

    # Print out choice for comparison purposes
    print(f"You chose {user_choice}")
    print()

game_summary = []

# Rounds won will be calculated (total - draw - lost)
rounds_played = 5
rounds_lost = 0
rounds_drawn = 0

for item in range(0, 5):
    result = input("Choose result: ")

    outcome = f"Round {item}: {result}"

    if result == "lost":
        rounds_lost += 1

    elif result == "tie":
        rounds_drawn += 1

    game_summary.append(outcome)

rounds_won = rounds_played - rounds_lost - rounds_drawn

# Calculate game stat
percent_win = rounds_won / rounds_played * 100
percent_lose = rounds_lost / rounds_played * 100
percent_tie = rounds_drawn / rounds_played * 100

# end game statement

print()
print("***** Game History *****")
for game in game_summary:
    print(game)

print()

# displays game stats with % values to the nearest whole number
print(" ***** Game Statistics *****")
print(f"Win: {rounds_won}, {percent_win:.0f}% \nLoss: {rounds_lost}, "
      f"{percent_lose:.0f}% \nTie: {rounds_drawn}, {percent_tie:.0f}%")


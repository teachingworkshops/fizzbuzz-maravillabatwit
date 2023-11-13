# Initialize the turn variable to start with Player 1
turn = 1

# Start the game count at 1
number = 1

# Main game loop
while True:
    # Check if the current number is divisible by 15 (both 3 and 5)
    if number % 15 == 0:
        # Prompt the current player to say 'fizzbuzz' or 'stop'
        player_input = input(f"Player {turn}, say 'fizzbuzz' or 'stop':- ")
        # End the game if player chooses to stop
        if player_input.lower() == 'stop':
            break
        # Check for incorrect input
        elif player_input.lower() != 'fizzbuzz':
            print(f"Player {turn} made a mistake! The correct answer was 'fizzbuzz'.")
            break

    # Check if the current number is divisible by 5 only
    elif number % 5 == 0:
        # Prompt the current player to say 'buzz' or 'stop'
        player_input = input(f"Player {turn}, say 'buzz' or 'stop': ")
        # End the game if player chooses to stop
        if player_input.lower() == 'stop':
            break
        # Check for incorrect input
        elif player_input.lower() != 'buzz':
            print(f"Player {turn} made a mistake! The correct answer was 'buzz'.")
            break

    # Check if the current number is divisible by 3 only
    elif number % 3 == 0:
        # Prompt the current player to say 'fizz' or 'stop'
        player_input = input(f"Player {turn}, say 'fizz' or 'stop': ")
        # End the game if player chooses to stop
        if player_input.lower() == 'stop':
            break
        # Check for incorrect input
        elif player_input.lower() != 'fizz':
            print(f"Player {turn} made a mistake! The correct answer was 'fizz'.")
            break

    # For numbers not divisible by 3 or 5
    else:
        # Prompt the current player to say the number or 'stop'
        player_input = input(f"Player {turn}, say the number or 'stop': ")
        # End the game if player chooses to stop
        if player_input.lower() == 'stop':
            break
        try:
            # Check if the entered number matches the current count
            if int(player_input) != number:
                print(f"Player {turn} made a mistake! The correct answer was {number}.")
                break
        except ValueError:
            # Handle non-numeric input
            print("Invalid input. Please enter a number or 'stop' to end.")
            continue

    # Increment the number for the next turn
    number += 1
    # Alternate turns between Player 1 and Player 2
    turn = 3 - turn

# Message displayed when the game ends
print("Game ended. Thanks for playing!")

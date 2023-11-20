def calculate_response(number):
    if number < 1:
        return str(number)
    elif number % 15 == 0:
        return 'fizzbuzz'
    elif number % 3 == 0:
        return 'fizz'
    elif number % 5 == 0:
        return 'buzz'
    else:
        return str(number)


def play_game():
    # Initialize the turn variable to start with Player 1
    turn = 1

    # Start the game count at 1
    number = 1

    # Main game loop
    while True:
        correct_answer = calculate_response(number)
        player_input = input(f"Player {turn}, say '{correct_answer}' or 'stop': ")

        if player_input.lower() == 'stop':
            break
        elif player_input.lower() != correct_answer:
            print(f"Player {turn} made a mistake! The correct answer was '{correct_answer}'.")
            break

        number += 1
        turn = 3 - turn

    print("Game Ends. Thanks for playing!")

if __name__ == "__main__":
    play_game()

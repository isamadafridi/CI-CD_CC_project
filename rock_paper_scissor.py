import random

# Game constants
GAME_WORDS = ['rock', 'paper', 'scissor']


def determine_winner(user_choice, comp_choice):
    """
    Determine the winner of a rock-paper-scissors game.
    
    Args:
        user_choice (str): Player's choice
        comp_choice (str): Computer's choice
    
    Returns:
        str: 'draw', 'player', or 'computer'
    """
    if user_choice == comp_choice:
        return 'draw'
    elif (user_choice == 'rock' and comp_choice == 'scissor') or \
         (user_choice == 'paper' and comp_choice == 'rock') or \
         (user_choice == 'scissor' and comp_choice == 'paper'):
        return 'player'
    else:
        return 'computer'


def is_valid_choice(choice):
    """
    Validate if the choice is valid.
    
    Args:
        choice (str): User's input choice
    
    Returns:
        bool: True if valid, False otherwise
    """
    return choice in GAME_WORDS


def get_computer_choice():
    """
    Get a random choice for the computer.
    
    Returns:
        str: Computer's random choice
    """
    return random.choice(GAME_WORDS)


def main():
    """Main game loop."""
    print('----------Welcome to Luck Game--------------')
    
    player_score = 0
    computer_score = 0

    while True:
        comp_choice = get_computer_choice()
        # print(f'Computer Choice: "{comp_choice}"')

        print('Choose Any: "Rock, Paper, Scissor"')
        user_choice = str(input('Enter your choice, or For Exit write "quit or q": ').lower())
        
        if user_choice == 'quit' or user_choice == 'q':
            print('Thanks for playing')
            break

        if not is_valid_choice(user_choice):
            print('⚠️ Invalid Input, try again')
            continue

        result = determine_winner(user_choice, comp_choice)
        
        if result == 'draw':
            print("It's Draw 😒")
        elif result == 'player':
            print('You Win🏆')
            player_score += 1
        else:
            print('You lose😔, \nTry next time')
            computer_score += 1
        
        print(f'Your Score: {player_score}')
        print(f'Bot Score: {computer_score}\n')

    print(f'Your Score: {player_score}, Bot Score: {computer_score}')


if __name__ == '__main__':
    main()



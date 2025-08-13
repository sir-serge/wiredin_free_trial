import random

hands = ['rock', 'scissors', 'paper']
results = {'win': 'win', 'lose': 'lose', 'draw': 'draw try again'}


def start_message():
    print('Start \'rock-paper-scissors\'')


def is_hand(string):
    if string.isdigit():
        number = int(string)
        if number >= 0 and number <= 2:
            return True
        else:
            return False
    else:
        return False


def get_player():
    print('Input your hand')
    input_message = ''
    index = 0
    for hand in hands:
        input_message += str(index) + ':' + hand
        if index < 2:
            input_message += ', '
        index += 1
    return input(input_message)


def get_computer():
    return random.randint(0, 2)


def get_hand_name(hand_number):
    return hands[hand_number]


def view_hand(your_hand, computer_hand):
    print('My hand is ' + get_hand_name(your_hand))
    print('Rival\'s hand is ' + get_hand_name(computer_hand))


def get_result(hand_diff):
    if hand_diff == 0:
        return 'draw'
    elif hand_diff == -1 or hand_diff == 2:
        return 'win'
    else:
        return 'lose'


def view_result(result):
    print(results[result])
"""
function live to displaye lives of players 
"""
def live(you_live,cpu_live):
    print (f'Lives You:{you_live} / Rival:{cpu_live}' )            
def play():
    # Set starting lives for both the player and the computer
    you_live = 3
    cpu_live = 3

    # Main game loop: runs until either you or the CPU has 0 
    while you_live > 0 and cpu_live > 0:
        # Show current lives before each round
        live(you_live, cpu_live)
        your_hand = get_player()
        while not is_hand(your_hand):  
            your_hand = get_player()
        your_hand = int(your_hand)
        computer_hand = get_computer()
        hand_diff = your_hand - computer_hand

        view_hand(your_hand, computer_hand)

        # Determine result of this round (win, lose, or draw)
        result = get_result(hand_diff)
        view_result(result)

        # Adjust lives based on result
        if result == 'win':
            cpu_live -= 1  # Opponent loses a life
        elif result == 'lose':
            you_live -= 1  # Player loses a life

    # This loop runs when someone has lost all lives
    while cpu_live == 0 or you_live == 0:
        # Ask if the player wants to replay the game
        replay_choice = input('Replay? (Y or N): ')
        if replay_choice.lower() == 'y':
            # Restart the game from scratch
            play()
        else:
            # Exit the game loop
            print('Thank you for playing!')
            break


start_message()
play()
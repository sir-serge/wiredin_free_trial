import random  # Import the random module for computer's hand selection

hands = ['rock', 'scissors', 'paper']  
results = {'win': 'You win!',
           'lose': 'You lose!',
           'draw': 'try again it\'s a draw!'}  # Result messages

def start_message():
    print('Start \'rock-paper-scissors\'')  


def get_player():
    print('Input your hand')  
    input_message = ''        # Initialize the input message string
    index = 0   
    for hand in hands:        # Build the input message with hand options
        input_message += str(index) + ':' + hand  
        if index < 2:         
            input_message += ', '
        index += 1  
    return input(input_message)   # Return the user's input as a string


def is_hands(inputedString):
    # Check if the input is a digit and within the valid range
    if inputedString.isdigit():
        number = int(inputedString)
        if number >= 0 and number <= 2:
            return True
        else:
            return False
    # Return False if input is not a digit
    return False


def get_computer():
    return random.randint(0, 2)  # Randomly select computer's hand (0, 1, or 2)


def get_hand_name(index):
    return hands[index]  # Get the hand name from index


def Print_hand_names(your_hand, computer_hand):
    # Print both player's and computer's hand choices
    print('Your hand: ' + get_hand_name(your_hand))
    print('Computer hand: ' + get_hand_name(computer_hand))


def get_result(hand_difference):
    # Determine the result based on hand difference
    if hand_difference == 0:
        return 'draw'
    elif hand_difference == 1:
        return 'lose'
    else:
        return 'win'


def get_hand_difference(your_hand, computer_hand):
    # Calculate the difference using modulo for game logic
    return (your_hand - computer_hand) % 3


def result_message(result):
    print(results[result])  # Print the result message


def main():
    player = get_player()  # Get player's input as a string
    
    # Validate input until a correct value is entered
    while not is_hands(player):
        print('Input error, try again')
        player = get_player()
    
    player_hand = int(player)  # Convert input to integer
    computer_hand = get_computer()  # Get computer's hand
    
    Print_hand_names(player_hand, computer_hand)  # Show both hands
    
    hand_difference = get_hand_difference(player_hand, computer_hand)  # Calculate difference
    result = get_result(hand_difference)  # Determine result
    
    result_message(result)  # Show result message

start_message()  # Print start message
main()
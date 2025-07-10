import random

# List of possible coin sides
results = {
    "win": "You win!",
    "lose": "You lose!"
}
def start_betFlip():
    print('Start \'bet flip\'')  # Print the start message

def Your_bet():
    print('Input your bet \"0 for head and 1 for Tail')  # Prompt user for input
    return input('Input your bet: ')  

def is_coorect_input(inputedbet):
    # Check if the input is a digit and within the valid range
    if inputedbet.isdigit():
        number = int(inputedbet)
        if number == 0 or number == 1:
            return True
        else:
            return False
    # Return False if input is not a digit
    return False

def coin_flip():
    return random.randint(0, 1)  # Randomly select coin side (0 for head, 1 for tail)

def get_side_name(index):
    if index == 0:
        return 'head'
    else:
        return 'tail'  # Get the bet name based on index (0 for head, 1 for tail)
    
def view_side(your_bet, coin_side):
    # Print both player's and computer's bet choices
    print('my  bet is : ' + get_side_name(your_bet))
    print('Coin side is: ' + get_side_name(coin_side))


def get_result(your_bet, coin_side):
    # Determine the result based on bet and coin side
    if your_bet == coin_side:
        return 'win'
    else:
        return 'lose'

def view_result(result):
    print(results[result])

def main():
    bet = Your_bet()  # Get bet's bet
    while not is_coorect_input(bet):  # Validate bet's bet
        print('Input error, try again and put in a number that is either  0 or 1')
        bet = Your_bet()
    
    fling_coin = coin_flip()  # Get computer's coin side
    view_side(int(bet),  fling_coin)  # Print both bets
    result = get_result(int(bet),  fling_coin)  # Get the result
    view_result(result)  # Print the result message


start_betFlip()  # Start the game
main()  # Start the game

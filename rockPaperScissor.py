import random

# print('Start \'rock-paper-scissors\' game')
# print('Input your hand choice')
# your_hand = int(input('0:rock, 1:scissors, 2:paper'))
# computer_hand = random.randint(0, 2)


#exercise 1


# if your_hand == 0:
#     if computer_hand == 0:
#         print('Draw')
#     elif computer_hand == 1:
#         print('Win')
#     elif computer_hand == 2:
#         print('Lose')
# elif your_hand == 1:
#     if computer_hand == 0:
#         print('Lose')
#     elif computer_hand == 1:
#         print('Draw')
#     elif computer_hand == 2:
#         print('Win')
# elif your_hand == 2:
#     if computer_hand == 0:
#         print('Win')
#     elif computer_hand == 1:
#         print('Lose')
#     elif computer_hand == 2:
#         print('Draw')

#exercise 2

# differnece = your_hand - computer_hand
# if differnece == 0:
#     print('Draw')
# elif differnece <0:
#     print('Win')
# elif differnece > 0:
#     print('Lose')

#exercise 3\

#funtionalzing 

def start_game():
    print('Start \'rock-paper-scissors\' game')

# get_player() function
def get_player():
    print('Input your hand choice')
    your_hand = int(input('0:rock, 1:scissors, 2:paper'))
    return your_hand


#get_computer() function
def get_computer():
    computer_hand = random.randint(0, 2)
    return computer_hand

#result function
def result(hand_diff):
    if hand_diff == 0:
        print('Draw')
    elif hand_diff < 0:
        print('Win')
    elif hand_diff > 0:
        print('Lose')


#exercise 4 
#getting hand names funtion and viewing them

# get_hand_name function
def get_hand_name(hand_numebr):
    if hand_numebr == 0:
        return 'rock'
    elif hand_numebr == 1:
        return 'scissors'
    elif hand_numebr == 2:
        return 'paper'
##view_hands function
def view_hands(your_hand, computer_hand):
    print('Your hand is: ', get_hand_name(your_hand))
    print('Computer hand is: ', get_hand_name(computer_hand))


start_game()
your_hand = get_player()
computer_hand = get_computer()
hand_diff = your_hand - computer_hand
result(hand_diff)
view_hands(your_hand, computer_hand)
get_hand_name(hand_diff)
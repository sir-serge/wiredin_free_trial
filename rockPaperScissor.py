# import random

# # print('Start \'rock-paper-scissors\' game')
# # print('Input your hand choice')
# # your_hand = int(input('0:rock, 1:scissors, 2:paper'))
# # computer_hand = random.randint(0, 2)


# #exercise 1


# # if your_hand == 0:
# #     if computer_hand == 0:
# #         print('Draw')
# #     elif computer_hand == 1:
# #         print('Win')
# #     elif computer_hand == 2:
# #         print('Lose')
# # elif your_hand == 1:
# #     if computer_hand == 0:
# #         print('Lose')
# #     elif computer_hand == 1:
# #         print('Draw')
# #     elif computer_hand == 2:
# #         print('Win')
# # elif your_hand == 2:
# #     if computer_hand == 0:
# #         print('Win')
# #     elif computer_hand == 1:
# #         print('Lose')
# #     elif computer_hand == 2:
# #         print('Draw')

# #exercise 2

# # differnece = your_hand - computer_hand
# # if differnece == 0:
# #     print('Draw')
# # elif differnece <0:
# #     print('Win')
# # elif differnece > 0:
# #     print('Lose')

# #exercise 3\

# #funtionalzing 

# def start_game():
#     print('Start \'rock-paper-scissors\' game')

# # get_player() function
# def get_player():
#     print('Input your hand choice')
#     your_hand = int(input('0:rock, 1:scissors, 2:paper'))
#     return your_hand


# #get_computer() function
# def get_computer():
#     computer_hand = random.randint(0, 2)
#     return computer_hand

# #result function
# def result(hand_diff):
#     if hand_diff == 0:
#         print('Draw')
#     elif hand_diff < 0:
#         print('Win')
#     elif hand_diff > 0:
#         print('Lose')


# #exercise 4 
# #getting hand names funtion and viewing them

# # get_hand_name function
# def get_hand_name(hand_numebr):
#     if hand_numebr == 0:
#         return 'rock'
#     elif hand_numebr == 1:
#         return 'scissors'
#     elif hand_numebr == 2:
#         return 'paper'
# ##view_hands function
# def view_hands(your_hand, computer_hand):
#     print('Your hand is: ', get_hand_name(your_hand))
#     print('Computer hand is: ', get_hand_name(computer_hand))


# start_game()
# your_hand = get_player()
# computer_hand = get_computer()
# hand_diff = your_hand - computer_hand
# result(hand_diff)
# view_hands(your_hand, computer_hand)
# get_hand_name(hand_diff)


#execrise 7 
# Refactored rock-paper-scissors game with functions and improved structure wher the fountion will repeat its self when it is draw
import random

hands = ['rock', 'scissors', 'paper']


def start_message():
    print('Start \'rock-paper-scissors\'')


def get_player(computer_hand):
    print('Input your hand')  # Prompt the user to input their hand
    input_message = ''        # Initialize an empty string for the input prompt message
    index = 0                 # Start index at 0 for hand options
    for hand in hands:        # Loop through each hand option in the hands list
        input_message += str(index) + ':' + hand  # Add the index and hand name to the input message
        if index < 2:         # If not the last hand, add a comma and space
            input_message += ', '
        index += 1            # Increment the index for the next hand
    inputed=int(input(input_message))    # Display the input message and get the user's choice as an integer
    if(inputed == computer_hand):
        print('You can\'t choose the same hand as the computer! try again.')
        return get_player(computer_hand)
    
    return inputed            # Return the user's selected hand


def get_computer():
    return random.randint(0, 2)


def get_hand_name(hand_number):
    return hands[hand_number]


def view_hand(your_hand, computer_hand):
    print('My hand is ' + get_hand_name(your_hand))
    print('Rival\'s hand is ' + get_hand_name(computer_hand))


def view_result(hand_diff):
    if hand_diff == 0:
        print('draw')
    elif hand_diff == -1 or hand_diff == 2:
        print('win')
    else:
        print('lose')


start_message()
computer_hand = get_computer()
your_hand = get_player(computer_hand)
hand_diff = your_hand - computer_hand

view_hand(your_hand, computer_hand)
view_result(hand_diff)
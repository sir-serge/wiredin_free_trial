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

##########################################################################################

#exercise 2

# differnece = your_hand - computer_hand
# if differnece == 0:
#     print('Draw')
# elif differnece <0:
#     print('Win')
# elif differnece > 0:
#     print('Lose')

##################################################################################
#exercise 3\

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
#     elif hand_diff==-1 or hand_diff == 2:
#         print('lose')
#     elif hand_diff==1 or hand_diff == -2:
#         print('win')

# start_game()
# your_hand = get_player()
# computer_hand = get_computer()
# hand_diff = your_hand - computer_hand
# result(hand_diff)


##########################################################################################
#exercise 4 
#getting hand names funtion and viewing them

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
#     elif hand_diff==-1 or hand_diff == 2:
#         print('lose')
#     elif hand_diff==1 or hand_diff == -2:
#         print('win')
# get_hand_name function
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

##########################################################################################

# exercise 5
# import random

# hands = ['rock', 'scissors', 'paper']


# def start_message():
#     print('Start \'rock-paper-scissors\'')

# #Get player's hand function
# def get_player():
#     print('Input your hand')
#     input_message = ''
#     index = 0
#     for hand in hands:
#         input_message += str(index) + ':' + hand
#         if index < 2:
#             input_message += ', '
#         index += 1
#     return int(input(input_message))

## Get computer's hand function
# def get_computer():
#     return random.randint(0, 2)

# #Get the result based on the difference between hands
# def get_hand_name(hand_number):
#     return hands[hand_number]

## View the hands of both player and computer
# def view_hand(your_hand, computer_hand):
#     print('My hand is ' + get_hand_name(your_hand))
#     print('Rival\'s hand is ' + get_hand_name(computer_hand))

## View the result based on the difference between hands
# def result(hand_diff):
#     if hand_diff == 0:
#         print('Draw')
#     elif hand_diff==-1 or hand_diff == 2:
#         print('lose')
#     elif hand_diff==1 or hand_diff == -2:
#         print('win')


# start_message()

# your_hand = get_player()
# computer_hand = get_computer()
# hand_diff = your_hand - computer_hand

# view_hand(your_hand, computer_hand)
# view_result(hand_diff)

############################################################################



# #exercise 6

# import random

# # Dictionary for user-friendly result display
# results = {'win': 'you win', 'lose': 'you lose', 'draw': 'draw try again'}

# # Start game
# def start_game():
#     print("Start 'rock-paper-scissors' game")

# # Get player's hand
# def get_player():
#     print('Input your hand choice')
#     your_hand = int(input('0:rock, 1:scissors, 2:paper: '))
#     return your_hand

# # Get computer's hand
# def get_computer():
#     computer_hand = random.randint(0, 2)
#     return computer_hand

# # Map hand difference to game result key
# def get_result(hand_diff):
#     result_mapping = {
#         0: 'draw',
#         1: 'lose',
#         2: 'win'
#     }
#     print('hand_diff:', hand_diff)  # Debugging line to check hand_diff
#     return result_mapping.get(hand_diff, 'draw')

# # Get hand name
# def get_hand_name(hand_number):
#     if hand_number == 0:
#         return 'rock'
#     elif hand_number == 1:
#         return 'scissors'
#     elif hand_number == 2:
#         return 'paper'

# # Display hand names
# def view_hands(your_hand, computer_hand):
#     print('Your hand is:', get_hand_name(your_hand))
#     print('Computer hand is:', get_hand_name(computer_hand))

# # Run the game
# start_game()
# your_hand = get_player()
# computer_hand = get_computer()
# hand_diff = (your_hand - computer_hand)%3

# result_key = get_result(hand_diff)
# print(results[result_key])
# view_hands(your_hand, computer_hand)


#####################################################################################################
#execrise 7 
#Refactored rock-paper-scissors game with functions and improved structure wher the fountion will repeat its self when it is draw


hands = ['rock', 'scissors', 'paper']


def start_message():
    print('Start \'rock-paper-scissors\'')


def get_player(computer_hand):
    print('Input your hand')  
    input_message = ''        
    index = 0                 
    for hand in hands:        
        input_message += str(index) + ':' + hand  
        if index < 2:         
            input_message += ', '
        index += 1            
    inputed=int(input(input_message))    
    if(inputed == computer_hand):
        print('You can\'t choose the same hand as the computer! try again.')
        return get_player(computer_hand)
    
    return inputed            


def get_computer():
    return random.randint(0, 2)


def get_hand_name(hand_number):
    return hands[hand_number]


def view_hand(your_hand, computer_hand):
    print('My hand is ' + get_hand_name(your_hand))
    print('computer\'s hand is ' + get_hand_name(computer_hand))


def result(hand_diff):
    if hand_diff == 0:
        print('Draw')
    elif hand_diff==1:
        print('lose')
    elif hand_diff==2:
        print('win')


start_message()
computer_hand = get_computer()
your_hand = get_player(computer_hand)
hand_diff = (your_hand - computer_hand)%3

view_hand(your_hand, computer_hand)
result(hand_diff)

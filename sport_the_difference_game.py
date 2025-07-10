import random
level=1
data=[ ["o","0" ], ["l","1"], ["u","v"]]
def start_sport_the_difference_game():
    print('Start \'sport the difference\'')  # Print the start message

def view_question():
    random_data=random.randint(0, 2) 
    print(f"{data[random_data]}") 
def section_message():
    print(f"level:{level}")


def play():
    start_sport_the_difference_game()  # Start the game
    view_question()  # Show the question
    section_message()  # Print the section message
    choice = input('(e.g. A1)')
    print('Debug:choice = ' + choice)

play()
import random
level=1
data=[ ["o","0" ], ["l","1"], ["u","v"]]
def start_sport_the_difference_game():
    print('Start \'sport the difference\'')  # Print the start message

def view_question():
    random_data=random.randint(0, 2) 
    random_cell=random.randint(0, 8)  # Randomly select a data item and cell
    print(f"{data[random_data]}") 
    for i in range(3):
        print(f"{i+1} |", end=' ')
        for j in range(3):
            if (i * 3 + j) == random_cell:
                print(f"{data[random_data][1]}", end=' ')
            else:
                print(f"{data[random_data][0]}", end=' ') # Print the first part of the question and we use end=' ' to avoid new line
        print()  # Print the question with the random data

def change_input_number(input_str):
    str_data = { 'A':0, 'B':1, 'C':2 }
    split_input = list(input_str)
    column=str_data[ split_input[0]]
    print(f"Debug: column = {column}")
    row=int(split_input[1])-1
    print(f"Debug: row = {row}")
    cell_number=row * 3 + column
    print(f"Debug: cell_number = {cell_number}")
    return cell_number




def section_message():
    print(f"level:{level}")


def play():
    start_sport_the_difference_game()  # Start the game
    view_question()  # Show the question
    section_message()  # Print the section message
    choice = input('(e.g. A1)')
    print('Debug:choice = ' + choice)
    change_input_number(choice)  # Change the input number
play()
import random
level=1
cols=5
rows=4
letters=[chr(ord('A') + i) for i in range(cols)]  # Generate letters A, B, C
data=[ ["o","0" ], ["l","1"], ["u","v"]]
def start_sport_the_difference_game():
    print('Start \'sport the difference\'')  # Print the start message

def view_question(row,col):
    random_data=random.randint(0, 2) 
    mistake_number=random.randint(0, row * col - 1)  # Randomly select a data item and cell
    print(f"mistake number{mistake_number}")
    print(f"{data[random_data]}") 
    for i in range(row):
        print(f"{i+1} |", end=' ')
        for j in range(col):
            if (i * 3 + j) == mistake_number:
                print(f"{data[random_data][1]}", end=' ')
            else:
                print(f"{data[random_data][0]}", end=' ') # Print the first part of the question and we use end=' ' to avoid new line
        print()  
    return mistake_number  # Return the mistake number for later use

def change_input_number(input_str):
    str_data = { letters[i]: i for i in range(len(letters)) }  # Create a mapping of letters to indices
    split_input = list(input_str)
    column=str_data[ split_input[0]]
    row=int(split_input[1])-1
    cell_number=row * 3 + column
    return cell_number

def is_correct_number(mistake_number, input_number ):
    if mistake_number == input_number:
        print('they are the same!')
        return True
    else:
        print('they are different!')
        return False
    

def view_result(is_correct):
    if is_correct:
        print('correct!')
    else:
        print('incorrect!')

def change_string(number):
    columns_map=[ 'A', 'B', 'C']
    row = number // 3 + 1
    column = number % 3
    return f"{columns_map[column]}{row}"  # Convert the number to a string format like 'A1', 'B2', etc.


def section_message():
    print(f"level:{level}")


def play():
    start_sport_the_difference_game()  # Start the game
    mistake_number=view_question(rows,cols)  # Get the mistake number from the question
    section_message()  # Print the section message
    choice = input('(e.g. A1)')
    print('Debug:choice = ' + choice)
    input_numebr=change_input_number(choice)  # Change the input number
    value_check=is_correct_number(mistake_number,input_numebr)  # Check if the input is correct
    view_result(value_check)  # Show the result of the check
    print(f"the answer is {change_string(mistake_number)}")  # Show the correct answer
play()
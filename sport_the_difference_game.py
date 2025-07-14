import random
level=1
cols=5
rows=4
letters=[chr(ord('A') + i) for i in range(cols)]  # Generate letters A, B, C
data=[ ["o","0" ], ["l","1"], ["u","v"]]
def start_sport_the_difference_game():
    print('Start \'sport the difference\'')  # Print the start message

def view_question(row, col):
    random_data = random.randint(0, 2)
    mistake_number = random.randint(0, row * col - 1)
    COLUMN_HEADERS = "".join(letters)  # No spaces between letters
    print(f"[{data[random_data]}]")  # Print the data row before the grid (optional, remove if not needed)
    print(f"/|{COLUMN_HEADERS}")      # No space after /|, no spaces between letters
    print("-" * (col + 2))            # Print dashes: 2 for /| and one for each column
    for i in range(row):
        print(f"{i+1}|", end='')      # No space after | for compact look
        for j in range(col):
            if (i * col + j) == mistake_number:
                print(f"{data[random_data][1]}", end='')  # Print the "mistake" character
            else:
                print(f"{data[random_data][0]}", end='')  # Print the normal character
        print()
    return mistake_number  # Return the mistake number for later use

def change_input_number(input_str):
    str_data = { letters[i]: i for i in range(len(letters)) }  # Create a mapping of letters to indices
    split_input = list(input_str)
    column=str_data[ split_input[0]]
    row=int(split_input[1])-1
    cell_number=row * cols + column
    return cell_number

def is_correct_number(mistake_number, input_number ):
    if mistake_number == input_number:
        return True
    else:
        return False
    

def view_result(is_correct):
    if is_correct:
        print('correct!')
    else:
        print('incorrect!')

def change_string(number):
    columns_map=letters
    row = number // cols + 1
    column = number % cols
    return f"{columns_map[column]}{row}"  # Convert the number to a string format like 'A1', 'B2', etc.


def section_message():
    print(f"level:{level}")


def play():
    start_sport_the_difference_game()  # Start the game
    section_message()  # Print the section message (level)
    mistake_number = view_question(rows, cols)  # Show the grid and get the mistake number
    print(f"Debug: mistake_number = {mistake_number}")  # Debug: print mistake number
    choice = input('(e.g. A1) ')  # Prompt for input
    print('Debug: choice = ' + choice)  # Debug: print choice
    input_number = change_input_number(choice)  # Convert input to cell number
    print(f"Debug: input_number = {input_number}")  # Debug: print input number
    value_check = is_correct_number(mistake_number, input_number)  # Check if correct
    view_result(value_check)  # Show result
    print(f"the answer is {change_string(mistake_number)}")  # Show correct answer

play()
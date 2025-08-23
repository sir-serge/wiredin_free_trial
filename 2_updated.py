import random
import math

def start_message():
    print('Input cell number (e.g. A1) of the different character.')
    
    
def section_message(level):
    # Show current level before each round
    print('level: ' + str(level))
    
    
def view_question(data, number_data, row, col):
    # Randomly pick a pair of characters (e.g., ['c','2'])
    choice_data = random.randint(0, 2)
    # Pick the position of the different character
    mistake_number = random.randint(0, (col * row) - 1)
    question = data[choice_data]
    print(question)
    # Print column headers
    i = 0
    j = 0
    question_str1 = '/|'
    question_str2 = '--'
    while i < col:
        question_str1 += number_data[i]
        question_str2 += '-'
        i += 1
    print(question_str1)
    print(question_str2)
    # Print the grid of characters
    i = 0
    while i < row:
        question_str = str(i + 1) + '|'
        while j < col:
            if (i * col + j) == mistake_number:
                question_str += question[1]
            else:
                question_str += question[0]
            j += 1
        print(question_str)
        i += 1
        j = 0
    return mistake_number
    
    
def change_input_number(input_str, col):
    # Convert user input (e.g., "A1") into a grid index
    str_data = {
    'A': 0,
    'B': 1,
    'C': 2,
    'D': 3,
    'E': 4,
    'F': 5,
    'G': 6,
    'H': 7,
    'I': 8,
    'J': 9
}

    input_str_split = list(input_str)
    col_number = str_data[input_str_split[0]]
    row_number = int(input_str_split[1]) - 1
    input_number = row_number * col + col_number
    return input_number
    
    
def is_correct_number(mistake_number, input_number):
    return mistake_number == input_number
    
    
def view_result(is_correct, mistake_number):
    if is_correct:
        print('Correct!')
    else:
        print('Wrong')
        
        
def change_string(number):
    # Convert grid index back into a cell label (e.g., 0 → "A1")
    col_number = number % col
    row_number = math.floor(number / col) + 1
    string = number_data[col_number] + str(row_number)
    return string
    
    
def Level(string, level, row, col):
    # Adjust difficulty based on whether the player was correct
    if string == True:
      if level<13:  
        level += 1  
        # Increase grid size (rows first, then columns)
        if row < col:
            row += 1
        else:
            col += 1
    elif string == False:  
        if level < 3 or row-2<3 or col-2<3:
            level -= 1  
            row = 3
            col = 3            
        else:
            level -= 2
            row -= 1
            col -= 1
    return level, row, col
    
    
def play():
    col = 3
    row=3
    level = 1
    number_data = ['A','B','C','D','E','F','G','H','I','j']
    data = [['c', '2'], ['l', '1'], ['u', 'v']]
    while True:
        section_message(level)  
        mistake_number = view_question(data, number_data, row, col)
        choice = input('(e.g. A1)').upper()
        input_number = change_input_number(choice, col)
        is_correct = is_correct_number(mistake_number, input_number)
        view_result(is_correct, mistake_number)
        level, row, col = Level(is_correct, level, row, col)
        if level <= 0:
            level = 1
        if level ==13:
            print('all level passed "congrats"')
            
            
            
start_message()
play()

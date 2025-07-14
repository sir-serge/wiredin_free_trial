array = [
    ['January', 'February', 'March', 'April'],
    ['May', 'June','July', 'August'],
    ['September', 'October', 'November', 'December']
    ]
for row in array:  # Loop through each sublist (each group of months)
    for column in row:  # Loop through each month in the current sublist
        print(column)  # Print the current month

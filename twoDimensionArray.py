import numpy as np
friends = np.array(['Tom', 'Jane', 'Brian', 'Carol', 'Jack'])
for i, friend in enumerate(friends):
    print(f'{i+1}: {friend}')
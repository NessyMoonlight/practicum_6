cell = input('Введите координаты ячейки: ')
letter = cell[0]
number = cell[1]

if letter in 'aceg' and number in '1357':
    print('черный')
elif letter in 'bdfh' and number in '2468':
    print('черный')
else:
    print('белый')
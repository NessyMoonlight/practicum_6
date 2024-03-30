move = input()

start = move.split('-')[0]
end = move.split('-')[1]

gorisontal_dist = abs(ord(start[0]) - ord(end[0]))
vertical_dist = abs(int(start[1]) - int(end[1]))

if ((gorisontal_dist == 2 and vertical_dist == 1) or
        (gorisontal_dist == 1 and vertical_dist == 2)):
    print("Верно")
else:
    print("Ошибка")
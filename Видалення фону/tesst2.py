x1 = int(input(''))
y1 = int(input(''))
x2 = int(input(''))
y2 = int(input(''))
x = int(input(''))
y = int(input(''))

if x < x1:
    if y >= y2:
        print('NW')
    elif y <= y1:
        print('SW')
    else:
        print('W')
elif x > x2:
    if y >= y2:
        print('NE')
    elif y <= y1:
        print('SE')
    else:
        print('E')
else:
    if y > y2:
        print('N')
    elif y < y1:
        print('S')
    else:
        print('Good!')

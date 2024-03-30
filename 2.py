a, b = map(int,input().split('x'))
c, d, e = map(int, input().split('x'))

if a*b >= c*d or a*b >= d*e or a*b >= c*e:
    print('да')
else:
    print('нет')
x1 = int(input())
y1 = int(input())
x2 = int(input())
y2 = int(input())

k = (y1 - y2) / (x1 - x2)
b = y1 - k * x1

print('y = ' + str(k) + 'x' + ' + ' + str(b))

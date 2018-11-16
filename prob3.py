import math
minutes = int(input('Enter minutes: '))
x = math.sin(minutes / 60 * 2 * math.pi)
y = math.cos(minutes / 60 * 2 * math.pi)
print('Minute hand is at (x,y): {:0.2f}, {:0.2f}'.format(x, y))
from turtle import *
from turtle_5 import draw_star

speed(-1)
color('blue')

for i in range(100):
    import random
    x = random.randint(-300, 300)
    y = random.randint(-300, 300)
    length = random.randint(3, 10)
    draw_star(x, y, length)
mainloop()

# random.randint(a, b)
# Return a random integer N such that a <= N <= b.

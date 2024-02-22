import turtle

def koch_curve(t, order, size):
    if order == 0:
        t.forward(size)
           
    else:
        for angle in [60, -120, 60, 0]:
            koch_curve(t, order - 1, size / 3)
            t.left(angle)

def snowflake(t, order, size):
    for _ in range(6):
        koch_curve(t, order, size)
        t.right(60)

def draw_koch_curve(order, size=200):
    window = turtle.Screen()
    window.bgcolor('white')

    t = turtle.Turtle()
    t.speed(0)
    t.penup()
    t.goto(-size / 2, size / 2)
    t.pendown()

    snowflake(t, order, size)

    window.mainloop()

def main():
    order = int(input('Enter the integer to determine the recursion depth: '))
    draw_koch_curve(order)

main()


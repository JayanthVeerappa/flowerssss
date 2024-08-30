import turtle as trtl


painter = trtl.Turtle()
screen = trtl.Screen()
screen.setup(width=800, height=600) 

def sunflower():
    painter.speed(20)
    painter.color("black", "orange")
    painter.begin_fill()
    
    for _ in range(50):
        painter.forward(300)
        painter.left(170)
    
    painter.end_fill()

def lily():
    def draw_petal(painter, radius):
        heading = painter.heading()
        painter.circle(radius, 60)
        painter.left(120)
        painter.circle(radius, 60)
        painter.setheading(heading)

    my_radius = 80
    my_petals = 10

    for _ in range(my_petals):
        draw_petal(painter, my_radius)
        painter.left(360 / my_petals)
    
def rose():
    painter.penup()
    painter.left(90)
    painter.fd(200)
    painter.pendown()
    painter.right(90)
    
    # Flower base
    painter.fillcolor("red")
    painter.begin_fill()
    painter.circle(10, 180)
    painter.circle(25, 110)
    painter.left(50)
    painter.circle(60, 45)
    painter.circle(20, 170)
    painter.right(24)
    painter.fd(30)
    painter.left(10)
    painter.circle(30, 110)
    painter.fd(20)
    painter.left(40)
    painter.circle(90, 70)
    painter.circle(30, 150)
    painter.right(30)
    painter.fd(15)
    painter.circle(80, 90)
    painter.left(15)
    painter.fd(45)
    painter.right(165)
    painter.fd(20)
    painter.left(155)
    painter.circle(150, 80)
    painter.left(50)
    painter.circle(150, 90)
    painter.end_fill()
    
   
def tulip():
    painter.penup()
    painter.left(90)
    painter.fd(200)
    painter.pendown()
    painter.right(90)
    
    # Flower base
    painter.fillcolor("purple")
    painter.begin_fill()
    painter.circle(10, 180)
    painter.circle(25, 110)
    painter.left(50)
    painter.circle(60, 45)
    painter.circle(20, 170)
    painter.right(24)
    painter.fd(30)
    painter.left(10)
    painter.circle(30, 110)
    painter.fd(20)
    painter.left(40)
    painter.circle(90, 70)
    painter.circle(30, 150)
    painter.right(30)
    painter.fd(15)
    painter.circle(80, 90)
    painter.left(15)
    painter.fd(45)
    painter.right(165)
    painter.fd(20)
    painter.left(155)
    painter.circle(150, 80)
    painter.left(50)
    painter.circle(150, 90)
    painter.end_fill()
    
    


flowerChoice = input("What flower do you want? And how many of them do you want?")


numberof = 0

for word in flowerChoice.split():
    if word.isdigit():
        numberof = int(word)  
        if word.lower() == 'lily' or 'lilys':
            for i in range(numberof):
                lily()
                painter.penup()
                painter.goto(float(screen.window_width()) * ((i + 1) / numberof), 0)
                painter.pendown()
                painter.setheading(0)
        if word.lower() == 'sunflower' or 'sunflowers':
            for i in range(numberof):
                sunflower()
                painter.penup()
                painter.goto(float(screen.window_width()) * ((i + 1) / numberof), 0)
                painter.pendown()
                painter.setheading(0)
        if word.lower() == 'rose' or 'roses':
            for i in range(numberof):
                rose()
                painter.penup()
                painter.goto(float(screen.window_width()) * ((i + 1) / numberof), 0)
                painter.pendown()
                painter.setheading(0)
        if word.lower() == 'tulip' or 'tulips':
            for i in range(numberof):
                tulip()
                painter.penup()
                painter.goto(float(screen.window_width()) * ((i + 1) / numberof), 0)
                painter.pendown()
                painter.setheading(0)


trtl.done()

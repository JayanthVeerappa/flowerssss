import turtle as trtl
painter = trtl.Turtle()
screen = trtl.screensize()
print ("FLOWERS: 1:ROSE 2:TULIP 3:LILY 4:SUNFLOWER 5:MARIGOLDS")
flowerChoice = int(input("What flower do you want? (Input number) "))
numberof = int(input("How many"))
Potentialflowers = {1:'rose', 2:'tulip', 3:'lily', 4:'sunflower', 5:'Marigolds'}



def sunflower():
    painter.speed(20)
    painter.color("black", "orange")
    painter.begin_fill()
    
    for i in range(50):
        painter.forward(300)
        painter.left(170)
    
    painter.end_fill()
if flowerChoice == 4:
    for i in range (1,numberof):
        sunflower()
        painter.goto()

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
if flowerChoice == 3:
    for i in range(numberof):
        lily()
        painter.penup()
        painter.goto(float(screen[0])*((i+1)/numberof),0)
        painter.pendown()

def rose():
    # Set initial position
    painter.penup ()
    painter.left (90)
    painter.fd (200)
    painter.pendown ()
    painter.right (90)
    
    # flower base
    painter.fillcolor ("red")
    painter.begin_fill ()
    painter.circle (10,180)
    painter.circle (25,110)
    painter.left (50)
    painter.circle (60,45)
    painter.circle (20,170)
    painter.right (24)
    painter.fd (30)
    painter.left (10)
    painter.circle (30,110)
    painter.fd (20)
    painter.left (40)
    painter.circle (90,70)
    painter.circle (30,150)
    painter.right (30)
    painter.fd (15)
    painter.circle (80,90)
    painter.left (15)
    painter.fd (45)
    painter.right (165)
    painter.fd (20)
    painter.left (155)
    painter.circle (150,80)
    painter.left (50)
    painter.circle (150,90)
    painter.end_fill ()
    
    # Petal 1
    painter.left (150)
    painter.circle (-90,70)
    painter.left (20)
    painter.circle (75,105)
    painter.setheading (60)
    painter.circle (80,98)
    painter.circle (-90,40)
    
    # Petal 2
    painter.left (180)
    painter.circle (90,40)
    painter.circle (-80,98)
    painter.setheading (-83)
    
    # Leaves 1
    painter.fd (30)
    painter.left (90)
    painter.fd (25)
    painter.left (45)
    painter.fillcolor ("green")
    painter.begin_fill ()
    painter.circle (-80,90)
    painter.right (90)
    painter.circle (-80,90)
    painter.end_fill ()
    painter.right (135)
    painter.fd (60)
    painter.left (180)
    painter.fd (85)
    painter.left (90)
    painter.fd (80)
    
    # Leaves 2
    painter.right (90)
    painter.right (45)
    painter.fillcolor ("green")
    painter.begin_fill ()
    painter.circle (80,90)
    painter.left (90)
    painter.circle (80,90)
    painter.end_fill ()
    painter.left (135)
    painter.fd (60)
    painter.left (180)
    painter.fd (60)
    painter.right (90)
    painter.circle (200,60)
if flowerChoice == 1:
    for i in range(numberof):
        rose()
        painter.penup()
        painter.goto(float(screen[0])*((i+1)/numberof),0)
        painter.pendown()

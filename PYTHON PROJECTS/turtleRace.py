import turtle
import time
import random

WIDTH, HEIGHT = 700, 600
COLORS = ['red', 'green', 'blue', 'orange', 'yellow', 'black', 'blue', 'orange', 'yellow', 'black', 'purple', 'pink', 'brown', 'cyan']
    

def get_number_of_racers():
    racers = 0
    while True:
        racers = input("Enter the numbers of racers (2 - 10): ")
        if racers.isdigit():
            racers = int(racers)
        else:
            print("Input is not numeric... Try Again!")
            continue
        # The above if else is to convert the racers to 
        # intergers.

        if 2 <= racers <= 10:
            return racers
        else:
            print("Number not in range 2 - 10. Try again! ")


def create_turtles(colors):
    turtles = []
    spacingx = WIDTH // (len(colors) +  1)

    
    for i, color in enumerate(colors):
        racer = turtle.Turtle()
        racer = turtle.Turtle()
        racer.color(color)
        racer.shape('turtle')
        racer.left(90)
        racer.penup()
        # set position
        racer.setpos(-WIDTH // 2 + (i + 1) * spacingx , -HEIGHT // 2  + 20 )
        racer.pendown()   
        turtles.append(racer)

    return turtles

def race(colors):
    turtles = create_turtles(colors)
    
    while True:
        for racer in turtles:
            distance = random.randrange(1, 20)
            racer.forward(distance)

            x, y = racer.pos()
            if y >= HEIGHT // 2 - 10:
                return colors[turtles.index(racer)]



def init_turtle():
    screen = turtle.Screen()
    screen.setup(WIDTH, HEIGHT)
    screen.title('Turtle Racing!')

racers = get_number_of_racers()
init_turtle()

random.shuffle(COLORS)
colors = COLORS[:racers]
winner = race(colors)
print(f"The winner turtle is color with -> {winner}")
time.sleep(5)
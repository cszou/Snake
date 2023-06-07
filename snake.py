import random
from turtle import *

# global variables for screen setup
WIDTH = 500
HEIGHT = 500


# distance check
def checkDis(p1, p2):
    x1, y1 = p1
    x2, y2 = p2
    return ((x1 - x2) ** 2 + (y1 - y2) ** 2) ** 0.5 < 1


# Apple class extends Turtle
class Apple(Turtle):
    def __init__(self):
        super().__init__('circle')
        self.color('red')
        self.shapesize(0.5)
        self.up()
        self.setposition(random.randint(-19, 19) * 12.5, random.randint(-19, 19) * 12.5)

    # move to new position
    def newPos(self):
        self.goto(random.randint(-19, 19) * 12.5, random.randint(-19, 19) * 12.5)


# Snake class extends Turtle
class Snake(Turtle):
    def __init__(self):
        super().__init__('square')
        self.shapesize(0.5)
        self.color('green')
        self.up()
        self.stamp()
        self.segments = [(0, 0)]  # store snake segments, first one is the tail and last one is the head
        # drawing initial snake with 5 segments
        for i in range(4):
            self.forward(12.5)
            self.stamp()
            self.segments.append(self.pos())

    # change snake moving direction
    def goUp(self):
        if self.heading() % 180 != 0:
            pass
        else:
            self.setheading(90)

    def goDown(self):
        if self.heading() % 180 != 0:
            pass
        else:
            self.setheading(-90)

    def goLeft(self):
        if self.heading() % 180 == 0:
            pass
        else:
            self.setheading(180)

    def goRight(self):
        if self.heading() % 180 == 0:
            pass
        else:
            self.setheading(0)


class Game:
    # game initialize setup
    def __init__(self):
        self.score = 0
        self.inv = 250
        self.screen = Screen()
        self.screenSetup()
        self.mySnake = Snake()
        self.myApple = Apple()

    # screen setup
    def screenSetup(self):
        self.screen.setup(WIDTH, HEIGHT)
        self.screen.title("Snake Game - Score: " + str(self.score))
        self.screen.bgcolor('cyan')
        self.screen.tracer(0)

    # snake moving control
    def move(self):
        if not checkDis(self.mySnake.pos(), self.myApple.pos()):
            self.mySnake.clearstamps(1)
            self.mySnake.segments.pop(0)
        else:
            self.score += 1
            self.screen.title("Snake Game - Score: " + str(self.score))
            if self.score % 5 == 0 and self.inv > 50:
                self.inv -= 50
            self.myApple.newPos()
        self.mySnake.forward(12.5)
        self.mySnake.stamp()
        self.mySnake.segments.append(self.mySnake.pos())
        self.screen.update()
        self.screen.ontimer(self.move, self.inv)
        # restart game when collision with wall or snake itself.
        if abs(self.mySnake.xcor()) > 250 or abs(self.mySnake.ycor()) > 250:
            self.reset()
            self.play()
        for seg in self.mySnake.segments[1::]:
            if checkDis(self.mySnake.segments[0], seg):
                self.reset()
                self.play()

    # game play control
    def play(self):
        if self.mySnake.pos() == self.myApple.pos():
            self.myApple.newPos()
        self.move()
        self.screen.onkey(self.mySnake.goUp, 'Up')
        self.screen.onkey(self.mySnake.goDown, 'Down')
        self.screen.onkey(self.mySnake.goRight, 'Right')
        self.screen.onkey(self.mySnake.goLeft, 'Left')
        self.screen.listen()

    # reset and restart game after game over
    def reset(self):
        self.screen.clear()
        self.score = 0
        self.inv = 250
        self.screen = Screen()
        self.screenSetup()
        self.mySnake = Snake()
        self.myApple = Apple()


myGame = Game()
myGame.play()
mainloop()

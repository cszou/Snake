import random
from turtle import *

WIDTH = 500
HEIGHT = 500
INV = 500

screen = Screen()
screen.setup(WIDTH, HEIGHT)
screen.title("Game")
screen.bgcolor('cyan')
screen.tracer(0)


class Apple:
    def __init__(self):
        self.apple = Turtle(shape='circle')
        self.apple.color('red')
        self.apple.shapesize(0.5)
        self.apple.up()
        self.apple.setposition(random.randint(-19, 19) * 12.5, random.randint(-19, 19) * 12.5)

    def newPos(self):
        self.apple.goto(random.randint(-19, 19) * 12.5, random.randint(-19, 19) * 12.5)


class Snake:
    def __init__(self):
        self.snake = Turtle(shape='square')
        self.snake.shapesize(0.5)
        self.snake.color('green')
        self.snake.up()
        self.snake.stamp()
        self.segments = [(0, 0)]
        for i in range(4):
            self.snake.forward(12.5)
            self.snake.stamp()
            self.segments.append(self.snake.pos())

    def goUp(self):
        direction = self.snake.heading()
        if direction == 90 or direction == 270:
            pass
        elif direction == 0:
            self.snake.left(90)
        elif direction == 180:
            self.snake.right(90)

    def goDown(self):
        direction = self.snake.heading()
        if direction == 90 or direction == 270:
            pass
        elif direction == 180:
            self.snake.left(90)
        elif direction == 0:
            self.snake.right(90)

    def goLeft(self):
        direction = self.snake.heading()
        if direction == 180 or direction == 0:
            pass
        elif direction == 90:
            self.snake.left(90)
        elif direction == 270:
            self.snake.right(90)

    def goRight(self):
        direction = self.snake.heading()
        if direction == 0 or direction == 180:
            pass
        elif direction == 270:
            self.snake.left(90)
        elif direction == 90:
            self.snake.right(90)


def checkDis(p1, p2):
    x1, y1 = p1
    x2, y2 = p2
    return ((x1-x2)**2+(y1-y2)**2)**0.5 < 1


class Game:
    def __init__(self):
        self.mySnake = Snake()
        self.myApple = Apple()
        self.score = 0
        self.inv = 250
        self.screen = Screen()
        self.screenSetup()

    def screenSetup(self):
        self.screen.setup(WIDTH, HEIGHT)
        self.screen.title("Snake Game - Score: " + str(self.score))
        self.screen.bgcolor('cyan')
        self.screen.tracer(0)

    def move(self):
        if not checkDis(self.mySnake.snake.pos(), self.myApple.apple.pos()):
            self.mySnake.snake.clearstamps(1)
            self.mySnake.segments.pop(0)
        else:
            self.score += 1
            self.screen.title("Snake Game - Score: " + str(self.score))
            if self.score % 5 == 0 and self.inv > 50:
                self.inv -= 50
            self.myApple.newPos()
        self.mySnake.snake.forward(12.5)
        self.mySnake.snake.stamp()
        self.mySnake.segments.append(self.mySnake.snake.pos())
        if self.mySnake.snake.xcor() > 250:
            self.mySnake.snake.setx(self.mySnake.snake.xcor() - 500)
        elif self.mySnake.snake.xcor() < -250:
            self.mySnake.snake.setx(self.mySnake.snake.xcor() + 500)
        if self.mySnake.snake.ycor() > 250:
            self.mySnake.snake.sety(self.mySnake.snake.ycor() - 500)
        elif self.mySnake.snake.ycor() < -250:
            self.mySnake.snake.sety(self.mySnake.snake.ycor() + 500)
        screen.update()
        screen.ontimer(self.move, self.inv)
        for seg in self.mySnake.segments[1::]:
            if checkDis(self.mySnake.segments[0], seg):
                bye()

    def play(self):
        if self.mySnake.snake.pos() == self.myApple.apple.pos():
            self.myApple.newPos()
        self.move()
        self.screen.onkey(self.mySnake.goUp, 'Up')
        self.screen.onkey(self.mySnake.goDown, 'Down')
        self.screen.onkey(self.mySnake.goRight, 'Right')
        self.screen.onkey(self.mySnake.goLeft, 'Left')
        self.screen.listen()


myGame = Game()
myGame.play()
mainloop()

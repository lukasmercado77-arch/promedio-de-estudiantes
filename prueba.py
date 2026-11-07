import pygame

pygame.mixer.init()
pygame.mixer.music.load("musica.mp3")
pygame.mixer.music.set_volume(0.5)
pygame.mixer.music.play(-1)


import math
import turtle

screen = turtle.Screen()
screen.bgcolor("black")

pen = turtle.Turtle()
pen.hideturtle()
pen.penup()
pen.color("#ffb6c1")

for scale in range(11, 17):
    for i in range(120):
        t = i * math.tau / 120
        x = 16 * math.sin(t) ** 3
        y = (13 * math.cos(t) - 5 * math.cos (2 * t)
              - 2 * math.cos(3 * t)- math.cos(4 * t))
        pen.goto(x * scale, y * scale)
        pen.write("I Love You", align="center", font=("Arial", 8, "bold"))
nombre = turtle.Turtle()
nombre.hideturtle()
nombre.penup()
nombre.color("#ffb6c1")
nombre.goto(0, 20)

nombre.write("Daniela", align="center",
             font=("Arial", 12, "bold"))

turtle.done()

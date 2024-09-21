from turtle import *
from math import *

speed(0)
bgcolor("black")
goto(0,-40)

# Dibujo de la flor
for i in range(16):
    for j in range(18):
        color('#FFA216'), rt(90)
        circle(150-j*6, 90), lt(90)
        circle(150-j*6, 90), rt(180)
    circle(40,24)

# Estampado circular con phi
color('black')
shape('circle')
shapesize(0.5)
fillcolor('#8B4513')
golden_ang = 137.508
phi = golden_ang*(pi/180)

for i in range(140):
    r = 4*sqrt(i)
    theta = i*phi
    x = r*cos(theta)
    y = r*sin(theta)
    penup(), goto(x, y)
    setheading(i*golden_ang)
    pendown(), stamp()

# Función para dibujar un punto
def point(x, y):
    penup(), goto(x, y), pendown()
    color('black'), fillcolor('#FFA216')
    begin_fill(), circle(4), end_fill()

# Función para dibujar la letra "A" en el centro
def draw_A():
    penup()
    goto(0, -40)  # Ajustar la posición de la "A" más abajo
    color("#FFA216")  # Cambiar al color de los pétalos
    write("A", align="center", font=("Arial", 60, "bold"))  # Tamaño y estilo de la "A"

# Escribir mensaje encima de la flor
penup()
goto(0, 250)  # Ajustar la posición del mensaje
color("white")
write("Feliz día. Te amo mucho mire reina, te envío esta flor desde la distancia <3", align="center", font=("Arial", 24, "bold"))

# Dibujar la "A" en el centro
draw_A()

hideturtle()
done()

# pip install PythonTurtle

# importa la biblioteca turtle que proporciona una forma de dibuja gráficos en una ventana
import turtle

ventana = turtle.Screen()
ventana.bgcolor("black")
tortuga = turtle.Turtle()
tortuga.speed(0.6)
tortuga.color('red')
numero_estrella = 75

for i in range(numero_estrella*5):
    tortuga.forward(i*3)
    tortuga.right(145)
     
ventana.exitonclick()
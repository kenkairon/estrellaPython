# Importa la biblioteca 'turtle', que proporciona una forma de dibujar gráficos en una ventana.
import turtle

# Crea una ventana para dibujar, que tiene un fondo negro.
ventana = turtle.Screen()
ventana.bgcolor("black")

# Crea una estrella, que es el objeto que se mueve para dibujar en la ventana.
estrella = turtle.Turtle()

# Ajusta la velocidad de la estrella. El valor '10' está en la velocidad máxima.
estrella.speed(10)

# Establece el color de la estrella a rojo.
estrella.color('blue')

# Define el número total de estrellas que se van a dibujar, que en este caso es 75.
numero_estrella = 45

# Un bucle 'for' que se ejecuta 'numero_estrella * 5' veces, o sea, 375 veces.
for i in range(numero_estrella*5):
    # Mueve la estrella hacia adelante por una distancia que aumenta con cada iteración. La distancia es 'i * 3'.
    estrella.forward(i*3)
    
    # Gira la estrella 145 grados a la derecha después de cada movimiento.
    estrella.right(145)

# Mantiene la ventana abierta hasta que se haga clic en ella.
ventana.exitonclick()




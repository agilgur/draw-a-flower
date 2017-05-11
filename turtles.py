#Opens a window and draws a flower
import turtle

window= turtle.Screen()
window.bgcolor("Turquoise")
alice=turtle.Turtle()
alice.shape("arrow")
alice.speed("fastest")
alice.color("Navy", "yellow")
    

def draw_rhombus(name):
    for i in range (2):
        alice.forward(90)
        alice.right(50)
        alice.forward(90)
        alice.right(130)
    

def draw_flower():
       
    for j in range(36):
      #  alice.begin_fill()
        draw_rhombus(alice)
      #  alice.end_fill()
        alice.right(10)
    for i in range(36):
        alice.circle(60)
        alice.right(10)

    alice.right(90)    
    alice.forward(300)

    alice.left(90)
    alice.circle(190,55)
    alice.left(125)
    alice.circle(190,55)

    alice.right(115)
    alice.circle(190,55)
    alice.left(125)
    alice.circle(190,55)


    window.exitonclick()

draw_flower()





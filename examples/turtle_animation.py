import tkinter as tk
import turtle, math

# Generate 'y = 0.1*x**3 − 0.8*x**2 − 1.5*x + 5.4'
scale = 10
xs = [x/scale for x in range(-4*scale, 10*scale)]
ys = [0.1*x**3 - 0.8*x**2 - 1.5*x + 5.4 for x in xs]
yd = [0.3*x**2 - 1.6*x - 1.5 for x in xs]

# Prepare 'screen' and 'actor'
root = tk.Tk()
canvas = tk.Canvas(root, width=500, height=500)
canvas.pack()
screen = turtle.TurtleScreen(canvas)
actor = turtle.RawTurtle(screen, 'turtle')
actor.radians() # Use radian unit for angle and rotation

# Draw the function
zoom = 20
actor.penup()
actor.setpos(zoom*xs[0], zoom*ys[0]) # Put at the initial point
actor.pendown()
for (x, y, slope) in zip(xs, ys, yd):
    actor.setpos(zoom*x, zoom*y)
    actor.setheading(math.atan2(slope, 1))
screen.mainloop()
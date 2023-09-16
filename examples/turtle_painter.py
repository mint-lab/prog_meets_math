# This example is not working in Spyder directly (F5 or Run)
# Please type '!python turtle_painter.py' on IPython console in your Spyder.
import turtle

class TurtlePainter(turtle.RawTurtle):
    def __init__(self, canvas):
        super().__init__(canvas)
        self.pen_pallate = ['black', 'red', 'green', 'blue', 'cyan', 'magenta', 'yellow']
        self.pen_color = 0
        self.pen_width = 3
        self.pen_delta = 1
        self.step_move = 10
        self.step_turn = 10

        # Initialize the turtle
        self.shape('turtle')
        self.pencolor(self.pen_pallate[self.pen_color])
        self.pensize(self.pen_width)

        # Register event handlers
        canvas.onkeypress(self.shift_pen_color, 'c')
        canvas.onkeypress(lambda: self.forward(self.step_move), 'Up')
        canvas.onkeypress(lambda: self.backward(self.step_move), 'Down')
        canvas.onkeypress(lambda: self.left(self.step_turn), 'Left')
        canvas.onkeypress(lambda: self.right(self.step_turn), 'Right')
        canvas.onkeypress(lambda: self.clear(), 'Escape')
        canvas.onkeypress(lambda: self.pen(pendown=not self.isdown()), ' ')
        canvas.onkeypress(lambda: self.change_pen_width(+self.pen_delta), 'm')
        canvas.onkeypress(lambda: self.change_pen_width(-self.pen_delta), 'n')
        canvas.listen()

    def shift_pen_color(self):
        self.pen_color = (self.pen_color + 1) % len(self.pen_pallate)
        self.pencolor(self.pen_pallate[self.pen_color])

    def change_pen_width(self, delta):
        self.pen_width = max(self.pen_width + delta, 1)
        self.pensize(self.pen_width)

if __name__ == '__main__':
    canvas = turtle.Screen()
    painter = TurtlePainter(canvas)
    # You can add another turtles by additional instantiation.
    # another = turtle.Turtle()
    # another.penup()
    # another.goto(100, 100)
    canvas.mainloop()
import turtle
import colorsys

# set up screen
screen = turtle.Screen()
screen.bgcolor("black")
screen.title("Animated Birthday Flower")

# create turtle
pen = turtle.Turtle()
pen.speed(0)   # fastest
pen.width(2)
pen.hideturtle()

# color setting
hue = 0.0

# Flower drawing function
def draw_flower():
    global hue
    pen.clear()
    pen.penup()
    pen.goto(0, 0)
    pen.pendown()
    pen.setheading(0)

    petals = 36
    petal_length = 100
    petal_angle = 360 / petals
    for i in range(petals):
        color = colorsys.hsv_to_rgb((hue + i * 0.03) % 1.0, 1, 1)
        pen.pencolor(color)
        pen.circle(petal_length, 60)
        pen.left(120)
        pen.circle(petal_length, 60)
        pen.left(120)
        pen.left(petal_angle)
    hue = (hue + 0.01) % 1.0

# Animation loop
def animate():
    draw_flower()
    screen.update()
    screen.ontimer(animate, 50)  # redraw every 50ms

# start animation
screen.tracer(0)  # Turn off automatic animation
animate()

# keep window open
screen.mainloop()

# --- Sample class code (commented out) ---
# class Flower:
#     def __init__(self, color, size):
#         self.color = color
#         self.size = size
#
#     def bloom(self):
#         print(f"The {self.color} flower blooms with a size of {self.size} cm.")
#     def wilt(self):
#         print(f"The {self.color} flower wilts and shrinks to {self.size - 5} cm.")
#     def change_color(self, new_color):
#         print(f"The flower changes color from {self.color} to {new_color}.")
#         self.color = new_color
#     def grow(self, additional_size):
#         self.size += additional_size
#         print(f"The flower grows to a new size of {self.size} cm.")
#
# # Example usage
# rose = Flower("red", 10)
# rose.bloom()
# rose.grow(5)
# rose.change_color("blue")
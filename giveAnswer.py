import turtle
import random

screen = turtle.Screen()
screen.setup(700, 700)

a = random.randint(0, 12)
b = random.randint(0, 12)

correct_answer = a * b
# Prevent duplicate options if b is 0
wrong_answer1 = correct_answer - b if b != 0 else correct_answer + 5
wrong_answer2 = correct_answer + b if b != 0 else correct_answer + 10

# 1. Shuffle the options together first
options = [correct_answer, wrong_answer1, wrong_answer2]
random.shuffle(options)

# Write the Question
question = turtle.Turtle()
question.hideturtle()
question.penup()
question.color('black')
question.goto(0, 275)
question.write(f"What is the product of {a} and {b}", align="center", font=("Arial", 40, "bold"))

# Create a dedicated turtle to print feedback on screen
feedback = turtle.Turtle()
feedback.hideturtle()
feedback.penup()
feedback.goto(0, -150)  # Placed below the boxes


# 2. Function to check the answer
def check_answer(chosen_val):
    feedback.clear()  # Clear previous text
    if chosen_val == correct_answer:
        feedback.color("green")
        feedback.write("Correct! 🎉", align="center", font=("Arial", 30, "bold"))
    else:
        feedback.color("red")
        feedback.write("Wrong! Try again.", align="center", font=("Arial", 30, "bold"))


# Coordinates for Left, Middle, and Right boxes
positions = [-300, 0, 300]

# 3. Create boxes and numbers in a loop
for i in range(3):
    x_pos = positions[i]
    val = options[i]

    # Create the clickable square box turtle
    box = turtle.Turtle()
    box.shape("square")
    box.shapesize(stretch_wid=2, stretch_len=5)
    box.penup()
    box.goto(x_pos, 0)

    # Bind click event using a lambda to pass the specific value of this box
    box.onclick(lambda x, y, chosen=val: check_answer(chosen))

    # Write the text number inside the box
    text_pen = turtle.Turtle()
    text_pen.hideturtle()
    text_pen.penup()
    text_pen.color("white")
    text_pen.goto(x_pos, -12)  # Centered vertically inside the box
    text_pen.write(str(val), align="center", font=("Arial", 20, "bold"))

# Keeps the window alive so you can click multiple times
screen.mainloop()

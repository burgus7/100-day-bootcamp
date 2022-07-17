import pandas
import turtle as t

screen = t.Screen()
screen.title("U.S. State Game")
image = "blank_states_img.gif"
screen.addshape(image)
t.shape(image)
cursor = t.Turtle()
cursor.penup()
cursor.hideturtle()
score = t.Turtle()
score.penup()
score.hideturtle()

data = pandas.read_csv("50_states.csv")
all_states = data.state.to_list()
print(all_states)
counter = 0
guessed_states = []

def update_score(new_score):
    score.goto(-320, -300)
    score.color("white")
    score.begin_fill()
    score.goto(-320, -260)
    score.goto(-100, -260)
    score.goto(-100, -300)
    score.goto(-320, -300)
    score.end_fill()
    score.color("black")
    score.write(f"Score: {new_score}", align="left", font=("Courier", 24, "normal"))

def note(text):
    score.goto(320, -300)
    score.color("white")
    score.begin_fill()
    score.goto(320, -260)
    score.goto(10, -260)
    score.goto(10, -300)
    score.goto(320, -300)
    score.end_fill()
    score.color("black")
    score.write(f"{text}", align="right", font=("Courier", 24, "normal"))


cursor.goto(0, 260)
cursor.write("US States Game", align="center", font=("Courier", 24, "normal"))

update_score(0)

while counter <= 50:
    state = t.textinput(title="US States Game", prompt="Enter a State")
    f_state = state.strip().title()
    if f_state == "Exit":
        break
    if f_state in all_states:
        guessed_states.append(f_state)
        state_row = data[data["state"] == f_state]
        cursor.goto(int(state_row["x"]), int(state_row["y"]))
        cursor.write(f_state, align="center")
        counter += 1
        update_score(counter)
        note("Correct!")
    else:
        note("Wrong Answer")

#states to learn

states_to_learn = []
for state in all_states:
    if state not in guessed_states:
        states_to_learn.append(state)
missing = pandas.DataFrame(states_to_learn)
missing.to_csv("states_to_learn.csv")


t.mainloop()
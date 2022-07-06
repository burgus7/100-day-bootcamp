from tkinter import *
# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20
CHECK = "✔"
reps = 0
timer = None

# ---------------------------- TIMER RESET ------------------------------- # 
def reset():
    window.after_cancel(timer)
    global reps
    reps = 0
    canvas.itemconfig(time_num, text="00:00")
    timer_text.config(text="Timer", fg=GREEN)
    checks.config(text="")


# ---------------------------- TIMER MECHANISM ------------------------------- # 
def start_timer():
    global reps
    reps += 1

    if reps % 8 == 0:
        count_down(LONG_BREAK_MIN * 60)
        timer_text.config(text="Break", fg=PINK)
        checks.config(text=CHECK * int(reps/2))
    elif reps % 2 == 1:
        count_down(WORK_MIN * 60)
        timer_text.config(text="Work", fg=GREEN)
    elif reps % 2 == 0:
        count_down(SHORT_BREAK_MIN * 60)
        timer_text.config(text="Break", fg=PINK)
        checks.config(text=CHECK * int(reps/2))


# ---------------------------- COUNTDOWN MECHANISM ------------------------------- # 
def count_down(count):
    mins = int(count / 60)
    secs = count % 60
    if mins < 10:
        mins = "0" + str(mins)
    else:
        mins = str(mins)

    if secs < 10:
        secs = "0" + str(secs)
    else:
        secs = str(secs)

    new_time = f"{mins}:{secs}"
    canvas.itemconfig(time_num, text=new_time)
    if count > 0:
        global timer
        timer = window.after(1000, count_down, count - 1)
    else:
        start_timer()




# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Pomodoro")
window.config(padx=100, pady=50, bg=YELLOW)

# TODO 1: Add tomato image using canvas widget
canvas = Canvas(width=200, height=224, bg=YELLOW, highlightthickness=0)
tomato_img = PhotoImage(file="tomato.png")
canvas.create_image(100, 112, image=tomato_img)
time_num = canvas.create_text(103, 130, text="00:00",
                   fill='white',
                   font=(FONT_NAME, 35, 'bold'))
canvas.grid(column=2, row=2)

# TODO 2: Add text and buttons
timer_text = Label(text="Timer", font=(FONT_NAME, 35, 'bold'), fg=GREEN, bg=YELLOW)
timer_text.grid(column=2, row=1)

start_btn = Button(text="Start", command=start_timer, highlightthickness=0)
start_btn.grid(column=1, row=3)

reset_btn = Button(text="Reset", command=reset, highlightthickness=0)
reset_btn.grid(column=3, row=3)

checks = Label(text="",
               fg=GREEN, bg=YELLOW,
               font=(FONT_NAME, 25))
checks.grid(column=2, row=4)

window.mainloop()

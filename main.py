from tkinter import *
import math

PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
FONT_NAME = "Courier"
WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20
reps = 0
timer = None

# TIMER RESET


def reset_timer():
    global reps
    window.after_cancel(timer)
    title_lbl.config(text="Title", fg="white")
    canvas.itemconfig(timer_text, text="00:00")
    check_marks.config(text="")
    reps = 0


# TIMER MECHANISM


def start_timer():
    global reps
    reps += 1
    work_sec = WORK_MIN * 60
    short_break_sec = SHORT_BREAK_MIN * 60
    long_break_sec = LONG_BREAK_MIN * 60
    if reps == 8:
        count_down(long_break_sec)
        title_lbl.config(text="Break", fg="gold")
    elif reps == 2 or reps == 4 or reps == 6:
        count_down(short_break_sec)
        title_lbl.config(text="Break", fg=GREEN)
    else:
        count_down(work_sec)
        title_lbl.config(text="Working", fg=RED)


# COUNTDOWN MECHANISM


def count_down(count):
    global timer
    timer_min = math.floor(count / 60)
    timer_sec = count % 60
    if timer_sec < 10:
        timer_sec = f"0{timer_sec}"

    canvas.itemconfig(timer_text, text=f"{timer_min}:{timer_sec}")
    if count > 0:
        timer = window.after(1000, count_down, count - 1)
    else:
        start_timer()
        if reps % 2 == 0:
            check_marks.config(text="✓" * round(reps * .5))


# UI SETUP
window = Tk()
window.title("Pomodoro")
window.config(padx=70, pady=70, bg=PINK)

# Backround image and timer
canvas = Canvas(width=210, height=226, bg=PINK, highlightthickness=0)
tomato_img = PhotoImage(file="tomato.png")
canvas.create_image(105, 113, image=tomato_img)
timer_text = canvas.create_text(103, 130, text="00:00", fill=GREEN, font=("Courier", 35, "bold"))
canvas.grid(column=1, row=1)

# Label "Timer" on top
title_lbl = Label(text="Timer", fg="white", font=("Courier", 40, "bold"), padx=5, bg=PINK)
title_lbl.grid(column=1, row=0)

# Buttons Start and Reset
start_button = Button(text="Start", highlightbackground=PINK, activeforeground=GREEN, command=start_timer)
start_button.grid(column=0, row=2)
reset_button = Button(text="Reset", highlightbackground=PINK, activeforeground=RED, command=reset_timer)
reset_button.grid(column=2, row=2)

# Check mark Label
check_marks = Label(fg="gold", font=("Courier", 35, "bold"), bg=PINK)
check_marks.grid(column=1, row=3)


window.mainloop()

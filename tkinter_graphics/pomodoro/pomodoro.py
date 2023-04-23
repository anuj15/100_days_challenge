import math
from tkinter import *

reps = 0
timer_c = None


def start_timer():
    global reps
    reps += 1
    work = 1 * 3
    short_break = 2 * 3
    long_break = 3 * 3

    if reps % 2 != 0:
        count_down(work)
        timer.config(text="Work", fg="green")
    elif reps == 8:
        count_down(long_break)
        timer.config(text="Long Break", fg="pink")
    else:
        count_down(short_break)
        timer.config(text="Short Break", fg="red")


def count_down(counter):
    global timer_c
    count_min = math.floor(counter / 60)
    count_sec = counter % 60
    text = f"{count_min}:{count_sec}"
    if count_min < 10:
        text = f"0{count_min}:{count_sec}"
    if count_sec < 10:
        text = f"{count_min}:0{count_sec}"
    canvas.itemconfig(timer_text, text=text)
    if counter >= 0:
        timer_c = window.after(1000, count_down, counter - 1)
    else:
        start_timer()
        marks = ""
        work_sessions = math.floor(counter / 2)
        for i in range(work_sessions):
            marks += "✔"
        check.config(text=marks, fg="green", bg="yellow", font=("arial", 16, "bold"))


def reset_timer():
    window.after_cancel(timer_c)


window = Tk()
window.title("POMODORO")
window.config(padx=100, pady=50, bg="yellow")

canvas = Canvas()
canvas.config(width=200, height=224, bg="yellow", highlightthickness=0)
img = PhotoImage(file="tomato.png")
canvas.create_image(100, 112, image=img)
timer_text = canvas.create_text(100, 130, text="00:00", fill="white", font=("arial", 12, "bold"))
canvas.grid(row=1, column=1)

timer = Label()
timer.config(text="Timer", fg="green", font=("arial", 24, "bold"), bg="yellow")
timer.grid(row=0, column=1)

start = Button()
start.config(text="Start", command=start_timer)
start.grid(row=2, column=0)

reset = Button()
reset.config(text="Reset", command=reset_timer)
reset.grid(row=2, column=2)

check = Label()
check.config(text="", fg="green", bg="yellow", font=("arial", 16, "bold"))
check.grid(row=3, column=1)

window.mainloop()

if __name__ == '__main__':
    print("Start")

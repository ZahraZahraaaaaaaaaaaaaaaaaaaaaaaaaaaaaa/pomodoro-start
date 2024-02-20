import math
from tkinter import *


PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 1
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20
reps = 0
timer = None
# ---------------------------- TIMER RESET ------------------------------- #

def reset_time():
    window.after_cancel(timer)
    timer_text.config(text="Timer")
    canvas.itemconfig(set_timing, text="00:00")


# ---------------------------- TIMER MECHANISM ------------------------------- #
def start_timer():

    global reps

    reps += 1

    work_sec = WORK_MIN * 60
    short_break_sec = SHORT_BREAK_MIN * 60
    long_break_Sec = LONG_BREAK_MIN * 60

    if reps % 8 ==0:
        cout_down(long_break_Sec)
        timer_text.config(text="Break", fg=RED)

    elif reps % 2 ==0:
        cout_down(short_break_sec)
        timer_text.config(text="Break", fg=PINK)
    else:
        cout_down(work_sec)
        timer_text.config(text="Work", fg=GREEN)



# ---------------------------- COUNTDOWN MECHANISM ------------------------------- #
def cout_down(count):

    count_min = math.floor(count / 60)
    count_sec = count % 60
    if count_sec < 10:
        count_sec = f"0{count_sec}"

    canvas.itemconfig(set_timing, text=f"{count_min}:{count_sec}")
    if count > 0:
        global timer
        timer = window.after(1000, cout_down, count - 1)
    else:
        start_timer()
        mark = ""
        for i in range(math.floor(reps/2)):
            mark += "🗸"
        check_mark.config(text=mark)




# ---------------------------- UI SETUP ------------------------------- #

window = Tk()
window.title("Pomodoro")
window.config(padx=100, pady=50, bg=YELLOW)


tomato_img = PhotoImage(file="tomato.png")
canvas = Canvas(width=200, height=224, bg=YELLOW, highlightthickness=0)
canvas.create_image(100, 112,image=tomato_img)
set_timing = canvas.create_text(100, 112, text="00:00", fill="white", font=(FONT_NAME, 15, "bold"))
canvas.grid(column=1, row=1)

timer_text = Label(text="Timer", bg=YELLOW, fg=GREEN, font=(FONT_NAME, 50))
timer_text.grid(column=1, row=0)

start_button = Button(text="Start", command=start_timer)
start_button.grid(column=0 , row=3)

reset_button = Button(text="Reset", command=reset_time)
reset_button.grid(column=3 , row=3)

check_mark = Button(fg=GREEN)



window.mainloop()
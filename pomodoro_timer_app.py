"""
This script creates a pomodoro time productivity app using tkinter
"""

import tkinter
import math

# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20
reps = 0
timer = None

# ---------------------------- TIMER RESET ------------------------------- #

def reset_timer():
    global reps
    window.after_cancel(timer)
    title.config(text="Timer")
    canvas.itemconfig(timer_text, text="00:00")
    check_marks.config(text="")
    reps = 0

# ---------------------------- TIMER MECHANISM ------------------------------- #
def start_timer():
    global reps
    mark = ""
    reps += 1
    if reps % 2 == 1:
        count_down(WORK_MIN * 60)
        title.config(text="WORK", font=(FONT_NAME, 35, "bold"), bg=YELLOW, fg=GREEN)
    elif reps % 2 == 0 and reps < 8:
        count_down(SHORT_BREAK_MIN * 60)
        title.config(text="BREAK", font=(FONT_NAME, 35, "bold"), bg=YELLOW, fg=PINK)
        checks = int(reps / 2)
        for num in range(checks):
            mark += "✓"
        check_marks.config(text=mark)
        bring_to_front()
    else:
        count_down(LONG_BREAK_MIN * 60)
        title.config(text="BREAK", font=(FONT_NAME, 35, "bold"), bg=YELLOW, fg=RED)
        check_marks.config(text="")
        bring_to_front()
        reps = 0

# ---------------------------- BRING TO FRONT------------------------------- #
def bring_to_front():
    window.attributes('-topmost', True)
    window.after_idle(window.attributes, '-topmost', False)
# ---------------------------- COUNTDOWN MECHANISM ------------------------------- # 

def count_down(count):
    count_min = math.floor(count/60)
    count_sec = count % 60
    if count_sec < 10:
        count_sec = "0"+str(count_sec)
    canvas.itemconfig(timer_text,text=f"{count_min}:{count_sec}")
    if count > 0:
        global timer
        timer = window.after(1000,count_down,count-1)
    if count == 0:
        start_timer()

# ---------------------------- UI SETUP -----------

#Create main window
window = tkinter.Tk()
window.title("Pomodoro")
window.config(padx=100,pady=50,bg=YELLOW)

#Title label
title = tkinter.Label(text="Timer",font=(FONT_NAME,35,"bold"),bg=YELLOW,fg=GREEN)
title.grid(row=1,column=2)

#Start button
start = tkinter.Button(text="Start",highlightthickness=0,command=start_timer)
start.grid(row=6,column=1)

#Rest button
reset = tkinter.Button(text="Reset",highlightthickness=0,command=reset_timer)
reset.grid(row=6,column=3)

#Check marks to track progress
check_marks = tkinter.Label(text="",fg=GREEN,bg=YELLOW,font=(20))
check_marks.grid(row=6,column=2)

#Canvas image object
canvas = tkinter.Canvas(width=200,height=224,bg=YELLOW,highlightthickness=0)
tomato_img = tkinter.PhotoImage(file="tomato.png")
canvas.create_image(100,112,image=tomato_img)
timer_text = canvas.create_text(100,130,text="00:00",fill="white",font=(FONT_NAME,35,"bold"))
canvas.grid(row=4,column=2)

#Main Loop
window.mainloop()
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


rep = 0
global marks
marks = ''
timer = None

# ---------------------------- TIMER RESET ------------------------------- #
def reset_timer():
    screen.after_cancel(timer)
    # timer_text.config(100, 130, text='00:00', fill='white', font=(FONT_NAME, 35, "bold"))
    canvas.itemconfig(timer_text, text=f"00:00")
    timer_label.config(text='Timer', fg=GREEN, font=(FONT_NAME, 50), bg=YELLOW)
    checkmark.config(text='', fg=GREEN, bg=YELLOW)
    global rep
    rep = 0



# ---------------------------- TIMER MECHANISM ------------------------------- #
work_list = [1, 3, 5, 7]
short_break_list = [2,4,6]



def start_timer():
    global rep
    global marks
    #global timer_label
    rep += 1


    if rep % 2 == 0:
        marks = f"{marks} " + str('✓')
        print(marks)
        checkmark.config(text=marks)

    if rep in work_list:
        # timer_label = tkinter.Label(text='WORK', fg=GREEN, font=(FONT_NAME, 50), bg=YELLOW)
        # timer_label.grid(row=1, column=1)
        timer_label.config(text='WORK', fg = GREEN)
        count_down(WORK_MIN)# * 60)

    elif rep in short_break_list:
        # timer_label = tkinter.Label(text='BREAK', fg=PINK, font=(FONT_NAME, 50), bg=YELLOW)
        # timer_label.grid(row=1, column=1)
        timer_label.config(text='BREAK', fg=PINK)
        count_down(SHORT_BREAK_MIN)# * 60)
    else:
        # timer_label = tkinter.Label(text='LONG BREAK', fg=RED, font=(FONT_NAME, 50), bg=YELLOW)
        # timer_label.grid(row=1, column=1)
        timer_label.config(text='LONG BREAK', fg=RED)
        count_down(LONG_BREAK_MIN)# * 60)
    #rep += 1
    #screen.after(11,start_timer)


# ---------------------------- COUNTDOWN MECHANISM ------------------------------- #
def count_down(count):

    count_min = math.floor(count / 60)
    count_sec = count % 60
    if count_sec == 0:
        count_sec = '00'
    elif count_sec < 10:
        count_sec = '0' + str(count_sec)

    canvas.itemconfig(timer_text, text=f"{count_min}:{count_sec}")
    if count > 0:
        global timer
        timer = screen.after(1000,count_down, count - 1)
    else:
        start_timer()
# ---------------------------- UI SETUP ------------------------------- #

screen = tkinter.Tk()
screen.title("Pomodoro Timer")
screen.config(padx=100, pady = 50, bg = YELLOW)

canvas = tkinter.Canvas(width=200, height=224, bg=YELLOW, highlightthickness=0)
tomato_img = tkinter.PhotoImage(file='tomato.png')
canvas.create_image(100,112, image=tomato_img)

timer_text = canvas.create_text(100,130, text='00:00', fill = 'white', font=(FONT_NAME, 35, "bold"))
canvas.grid(row=2, column=1)

# animation to test 'while in parallel':
def animation(anim_counter):
    # anim_counter = anim_counter % 6
    animation_list = ['/','-','\\','|']
    anim = tkinter.Label(text=animation_list[anim_counter], bg=YELLOW)
    #anim.itemconfig(timer_text, text=f"{animation[anim_counter]}")
    anim.grid(row = 0, column=2)
    print(anim_counter)
    screen.after(1000,animation, (anim_counter + 1) % 4 )

animation(0)


## Buttons:
# start_label = tkinter.Label(text='Start')
# start_label.grid(row=5, column = 0)
# reset_label = tkinter.Label(text='Reset')
# reset_label.grid(row=5, column =2)

start_button = tkinter.Button(text='Start', command = start_timer, highlightthickness=0)
start_button.grid(row= 5,column = 0)
reset_button = tkinter.Button(text='Reset',command = reset_timer,  highlightthickness=0)
reset_button.grid(row= 5,column = 2)


checkmark = tkinter.Label(text='', fg=GREEN, bg=YELLOW)
checkmark.grid(column=1, row=6)


# Main title inside app:
# global timer_label
timer_label = tkinter.Label(text='Timer', fg = GREEN, font=(FONT_NAME,50), bg=YELLOW)
timer_label.grid(row=1, column = 1)




screen.mainloop()


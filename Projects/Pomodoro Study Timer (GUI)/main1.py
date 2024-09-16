from tkinter import *
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_sec = 0.2 *60
SHORT_BREAK_sec = 0.05*60
LONG_BREAK_sec = 0.1*60
#pow(2,3)=8
#anything/anything=float
#2*3=6
#2*3.0=6.0
#20*0.1=2.0 not 2
#1%60=1
#1.0%60=1.0
after=None

def countdown(count):
    global after
    min=int(count/60)
    sec=int(count%60)
    if sec<10:
        sec=f"0{sec}"
    canvas.itemconfig(timer, text=f"{min}:{sec}")
    if count>0:
        after=window.after(1000,countdown,count-1)
    else:
        startt()

window=Tk()
window.title("pomodoro")
window.config(padx=100,pady=50,bg=YELLOW)

canvas=Canvas(width=200,height=223,bg=YELLOW,highlightthickness=0)
image=PhotoImage(file="tomato.png")
canvas.create_image(99.5,111,image=image)
canvas.grid(row=1,column=1)

label=Label(text="Timer",font=(FONT_NAME,46,"italic"),bg=YELLOW,fg=GREEN) #"italic" position doesnt have to be there
label.grid(row=0,column=1) #if u put nothing here, row is not 0. row is 2(probably). see previuos grid row

timer=canvas.create_text(100,130,text="00:00",fill="white",font=(FONT_NAME,30,"bold"))#not a label, maybe bc of bg. create_text gives u only text. so u dont have to set bg

rep=0
tick=Label(bg=YELLOW,fg=GREEN)
tick.grid(row=2,column=1)
def startt():
    global after
    global rep
    rep+=1
    if rep%2!=0:
        label.config(text="Work")
        countdown(WORK_sec)
    elif rep%8==0:
        label.config(text="Break")
        countdown(LONG_BREAK_sec)
    else:
        label.config(text="Break")
        countdown(SHORT_BREAK_sec)
    if rep%2==0:
        tick["text"]+="✔"

def resett():
    global after
    global rep
    window.after_cancel(after)
    canvas.itemconfig(timer,text="00:00")
    label["text"]="Timer"
    tick["text"]=""
    rep=0

start=Button(text="start",command=startt)
reset=Button(text="reset",command=resett,highlightthickness=0)
start.grid(row=2,column=0)
reset.grid(row=2,column=2)






window.mainloop()
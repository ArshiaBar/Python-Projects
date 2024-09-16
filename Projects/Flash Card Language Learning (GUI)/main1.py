from tkinter import *
import shutil
import pandas
import random

BACKGROUND_COLOR = "#B1DDC6"

def flip():
    global keyy
    canvas.itemconfig(ground,image=card_back)
    canvas.itemconfig(lang_text,text="English")
    canvas.itemconfig(word,text=diction[keyy])

def yes_imple():
    global keyy
    diction.pop(keyy)
    dictt={"French":list(diction.keys()),"English":list(diction.values())}
    df=pandas.DataFrame(dictt)
    df.to_csv("data/learn.csv")

    canvas.itemconfig(ground, image=card_front)
    canvas.itemconfig(lang_text,text="French")
    keyy = random.choice(list(diction.keys()))
    canvas.itemconfig(word, text=keyy)
    window.after(3000,flip)

def no_imple():
    global keyy
    canvas.itemconfig(ground, image=card_front)
    canvas.itemconfig(lang_text, text="French")
    keyy = random.choice(list(diction.keys()))
    canvas.itemconfig(word,text=keyy)
    window.after(3000, flip)

#with open("data/french_words.csv") as f:
#    with open("data/learn.csv",'w') as ff:
#        ff.write(f.read())

#shutil.copyfile("data/french_words.csv","data/learn.csv")

try:
    dataframe = pandas.read_csv("data/learn.csv")
except FileNotFoundError:
    dataframe=pandas.read_csv("data/french_words.csv")
#diction=dataframe.to_dict(orient='records') #list
#print(diction)

diction={value.French:value.English for (key,value) in dataframe.iterrows()}

window=Tk()
window.title("learn french words")
window.config(bg=BACKGROUND_COLOR,padx=50,pady=50)

canvas=Canvas(width=800,height=526,highlightthickness=0,bg=BACKGROUND_COLOR)
canvas.grid(columnspan=2)
card_front=PhotoImage(file="images/card_front.png")
card_back=PhotoImage(file="images/card_back.png")
ground = canvas.create_image(400, 263)
lang_text=canvas.create_text(400,100,text="French",font=("Arial",24)) #fill="black"

right=PhotoImage(file="images/right.png")
wrong=PhotoImage(file="images/wrong.png")

yes=Button(image=right,command=yes_imple)
no=Button(image=wrong,command=no_imple)
yes.grid(column=1,row=1)
no.grid(row=1)

canvas.itemconfig(ground, image=card_front)

keyy=random.choice(list(diction.keys()))
word=canvas.create_text(400,263,text=keyy)

window.after(3000,flip)

window.mainloop()


#original_data = pandas.read_csv("data/french_words.csv")
#to_learn = original_data.to_dict(orient="records")
#data = pandas.DataFrame(to_learn)
#data.to_csv("data/words_to_learn.csv", index=False)

#list.remove(current_card)
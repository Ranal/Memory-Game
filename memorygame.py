from tkinter import *
from tkinter import font
from random import randint, shuffle

raam = Tk()
raam.title("Memory Game")
tahvel = Canvas(raam, width=600, height=600, background="dim gray")
tahvel.grid()

s_font = font.Font(family="Helvetica", size=40)
tahvel.create_text(125,25, text="Memory Game", fill="white", font=s_font, anchor=NW)


a = PhotoImage(file="a.gif") #1
b = PhotoImage(file="b.gif") #2
c = PhotoImage(file="c.gif") #3
d = PhotoImage(file="d.gif") #4
e = PhotoImage(file="e.gif") #5
f = PhotoImage(file="f.gif") #6
g = PhotoImage(file="g.gif") #7
h = PhotoImage(file="h.gif") #8
bg = PhotoImage(file="bg.gif") #bg

pic_list = [a,a,b,b,c,c,d,d,e,e,f,f,g,g,h,h]
bg_list = [bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg]
shuffle(pic_list)

print(pic_list)
print("--------")


def callback(event):
    canvas = event.widget
    x = canvas.canvasx(event.x)
    y = canvas.canvasy(event.y)
    print(x)
    print(y)
    a = canvas.find_closest(x,y)
    print(a)
    return a

    
k = 0
id_tabel = []
for i in range(4):
    id_rida = []
    for j in range(4):
        x = 135 + (j*110)
        y = 150 + (i*110)
        pildi_id = tahvel.create_image(x, y, image=pic_list[k])
        tahvel.tag_bind(pildi_id, "<1>", callback)
        id_rida.append(pildi_id)
        k += 1
    id_tabel.append(id_rida)
print(id_tabel)



raam.mainloop()


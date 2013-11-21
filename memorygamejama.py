from tkinter import *
from tkinter import font

def vaheta_pilt(event):
    # global deklaratsioon võimaldab muuta funktsioonist väljaspool
    # defineeritud muutujat
    global näidatav_pilt

    # vahetan pildi viite
    if näidatav_pilt == suletud:
        näidatav_pilt = avatud
    else:
        näidatav_pilt = suletud

    # ... ja uuendan selle viite põhjal tahvlil oleva pildi sisu
    tahvel.itemconfigure(img, image=näidatav_pilt)

raam = Tk()
raam.title("Memory Game")
tahvel = Canvas(raam, width=600, height=600, background="dim gray")
tahvel.grid()

s_font = font.Font(family="Helvetica", size=32)
tahvel.create_text(170,25, text="Memory Game", fill="white", font=s_font, anchor=NW)

suletud = PhotoImage(file="bg.gif")
avatud = PhotoImage(file="a.gif")
näidatav_pilt = suletud

img = tahvel.create_image(135, 150,image = näidatav_pilt,)
tahvel.tag_bind(img, '<1>', vaheta_pilt)

a = PhotoImage(file="a.gif") #1
b = PhotoImage(file="b.gif") #2
c = PhotoImage(file="c.gif") #3
d = PhotoImage(file="d.gif") #4
e = PhotoImage(file="e.gif") #5
f = PhotoImage(file="f.gif") #6
g = PhotoImage(file="g.gif") #7
h = PhotoImage(file="h.gif") #8
##
##img = tahvel.create_image(135, 150, image=a)
img = tahvel.create_image(245, 150, image=b)
img = tahvel.create_image(355, 150, image=c)
img = tahvel.create_image(465, 150, image=d)
 
img = tahvel.create_image(135, 260, image=e)
img = tahvel.create_image(245, 260, image=f)
img = tahvel.create_image(355, 260, image=g)
img = tahvel.create_image(465, 260, image=h)
 
img = tahvel.create_image(135, 370, image=h)
img = tahvel.create_image(245, 370, image=g)
img = tahvel.create_image(355, 370, image=f)
img = tahvel.create_image(465, 370, image=e)
 
img = tahvel.create_image(135, 480, image=d)
img = tahvel.create_image(245, 480, image=c)
img = tahvel.create_image(355, 480, image=b)
img = tahvel.create_image(465, 480, image=a)


raam.mainloop()



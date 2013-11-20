from tkinter import *
from tkinter import font

raam = Tk()
raam.title("Memory Game")
tahvel = Canvas(raam, width=600, height=600, background="dim gray")
tahvel.grid()

s_font = font.Font(family="Helvetica", size=40)
tahvel.create_text(170,25, text="Memory Game", fill="white", font=s_font, anchor=NW)


a = PhotoImage(file="a.gif") #1
b = PhotoImage(file="b.gif") #2
c = PhotoImage(file="c.gif") #3
d = PhotoImage(file="d.gif") #4
e = PhotoImage(file="e.gif") #5
f = PhotoImage(file="f.gif") #6
g = PhotoImage(file="g.gif") #7
h = PhotoImage(file="h.gif") #8
bg = PhotoImage(file="bg.gif") #bg

def click(event):
    pildi_id = tahvel.find_withtag(CURRENT)[0]
    for i in range(4):
        for j in range(4):
            if pildi_id == id_tabel[i][j]:
                print("klik kläk")

id_tabel = []
for i in range(4):
    id_rida = []
    for j in range(4):
        x = 135 + (j*110)
        y = 150 + (i*110)
        pildi_id = tahvel.create_image(x, y, image=bg)

        tahvel.tag_bind(pildi_id, "<1>", click)
        id_rida.append(pildi_id)
    id_tabel.append(id_rida)

print(id_tabel)


raam.mainloop()





#------------------------------------------------------
##img = tahvel.create_image(135, 150, image=a)
##img = tahvel.create_image(245, 150, image=b)
##img = tahvel.create_image(355, 150, image=c)
##img = tahvel.create_image(465, 150, image=d)
##
##img = tahvel.create_image(135, 260, image=e)
##img = tahvel.create_image(245, 260, image=f)
##img = tahvel.create_image(355, 260, image=g)
##img = tahvel.create_image(465, 260, image=h)
##
##img = tahvel.create_image(135, 370, image=h)
##img = tahvel.create_image(245, 370, image=g)
##img = tahvel.create_image(355, 370, image=f)
##img = tahvel.create_image(465, 370, image=e)
##
##img = tahvel.create_image(135, 480, image=d)
##img = tahvel.create_image(245, 480, image=c)
##img = tahvel.create_image(355, 480, image=b)
##img = tahvel.create_image(465, 480, image=a)

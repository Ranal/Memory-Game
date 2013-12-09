#!/usr/bin/python
from tkinter import *
from time import *
import random
root=Tk()
b=[]
col=[]
c=['red','blue','green','yellow','orange']
w=4
h=5
t=w*h
for z in range(w*h):
	col.append(z)
random.shuffle(col)
for z in range(w*h):
	col[z]=c[col[z]%5]
clk=0
def maker(a):
	def com():
		global p
		global clk
		clk+=1
		b[a].config(bg=col[a])
		if clk%2==1:
			global one
			one=col[a]
			p=a
			b[a].config(state='disabled')
		else:
			global two
			two=col[a]
			if one==two:
				b[a].config(state='disabled')
			else:
				root.update_idletasks()
				sleep(.2)
				b[a].config(state='normal', bg='SystemButtonFace')
				b[p].config(state='normal', bg='SystemButtonFace')

	return com
for a in range(t):
	b.append(Button(root, text='    ', command=maker(a)))
	b[a].grid(row=a%h, column=a%w)
mainloop()

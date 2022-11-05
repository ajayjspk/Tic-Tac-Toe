from tkinter import *
from tkinter import messagebox
a=Tk()
v=('Arial',20)

n=0
#funtion print x or o
def rname(b):
	global n	
	if b['text']==' ' and n%2==0:
		b['text']='X'
		b['bg']="#Ef55dc"
		n+=1
	elif b['text']==' ' and n%2!=0:
		b['text']='O'
		b['bg']="#62a7c8"
		n+=1
	elif b['text']!=' ':
		l4=Label(a,text='already entered',font=v).grid(column=2,row=5)
		messagebox.showerror(" ","already entered")
# check rows value 	

def crow(b1,b2,b3,b4,b5,b6,b7,b8,b9):
	if b1['text']=='X' and b2['text']=='X' and b3['text']=='X':
		l5=Label(a,text='X palyer is won',font=v).grid(column=2,row=5)
		messagebox.showerror("game over ","X palyer is won")
		mc=messagebox.askquestion('restart',"restart the game")
		print(mc)
		exit()
	elif b4['text']=='X' and b5['text']=='X' and b6['text']=='X':
		l6=Label(a,text='X palyer is won',font=v).grid(column=2,row=5)
		messagebox.showerror("game over ","X palyer is won")
		exit()
	elif b7['text']=='X' and b8['text']=='X' and b9['text']=='X':
		l7=Label(a,text='X palyer is won',font=v).grid(column=2,row=5)
		messagebox.showerror("game over ","X palyer is won")
		exit()


def crow1(b1,b2,b3,b4,b5,b6,b7,b8,b9):
	if b1['text']=='O' and b2['text']=='O' and b3['text']=='O':
		ll5=Label(a,text='O palyer is won',font=v).grid(column=2,row=5)
		messagebox.showerror("game over ","O palyer is won")
		exit()

	elif b4['text']=='O' and b5['text']=='O' and b6['text']=='O':
		ll6=Label(a,text='O palyer is won',font=v).grid(column=2,row=5)
		messagebox.showerror("game over ","O palyer is won")
		exit()

	elif b7['text']=='O' and b8['text']=='O' and b9['text']=='O':
		ll7=Label(a,text='O palyer is won',font=v).grid(column=2,row=5)
		messagebox.showerror("game over ","O palyer is won")
		exit()

#check column			
def ccolumn(b1,b2,b3,b4,b5,b6,b7,b8,b9):
	if b1['text']=='X' and b4['text']=='X' and b7['text']=='X':
		l1=Label(a,text='X palyer is won',font=v).grid(column=2,row=5)
		messagebox.showerror("game over ","X palyer is won")
		exit()

	elif b2['text']=='X' and b5['text']=='X' and b8['text']=='X':
		l2=Label(a,text='X palyer is won',font=v).grid(column=2,row=5)
		messagebox.showerror("game over ","X palyer is won")
		exit()

	elif b3['text']=='X' and b6['text']=='X' and b9['text']=='X':
		l3=Label(a,text='X palyer is won',font=v).grid(column=2,row=5)
		messagebox.showerror("game over ","X palyer is won")
		exit()
def ccolumn1(b1,b2,b3,b4,b5,b6,b7,b8,b9):
	if b1['text']=='O' and b4['text']=='O' and b7['text']=='O':
		l1=Label(a,text='O palyer is won',font=v).grid(column=2,row=5)
		messagebox.showerror("game over ","O palyer is won")
		exit()

	elif b2['text']=='O' and b5['text']=='O' and b8['text']=='O':
		l2=Label(a,text='O palyer is won',font=v).grid(column=2,row=5)
		messagebox.showerror("game over ","O palyer is won")
		exit()

	elif b3['text']=='O' and b6['text']=='O' and b9['text']=='O':
		l3=Label(a,text='O palyer is won',font=v).grid(column=2,row=5)
		messagebox.showerror("game over ","O palyer is won")
		exit()

#check daigonal
def diag(b1,b3,b5,b7,b9):
	if b1['text']=='X' and b5['text']=='X' and b9['text']=='X':
		l1=Label(a,text='X palyer is won',font=v).grid(column=2,row=5)
		messagebox.showerror("game over ","X palyer is won")
		exit()
	elif b3['text']=='X' and b5['text']=='X' and b7['text']=='X':
		l2=Label(a,text='X palyer is won',font=v).grid(column=2,row=5)
		messagebox.showerror("game over ","X palyer is won")
		exit()

def diag1(b1,b3,b5,b7,b9):
	if b1['text']=='O' and b5['text']=='O' and b9['text']=='O':
		l1=Label(a,text='O palyer is won',font=v).grid(column=2,row=5)
		messagebox.showerror("game over ","O palyer is won")
		exit()

	
	elif b3['text']=='O' and b5['text']=='O' and b7['text']=='O':
		l2=Label(a,text='O palyer is won',font=v).grid(column=2,row=5)
		messagebox.showerror("game over ","O palyer is won")
		exit()

#main command func
def clickb(b):
	global b1,b2,b3,b4,b5,b6,b7,b8,b9
	#tgame(b)
	rname(b)
	crow(b1,b2,b3,b4,b5,b6,b7,b8,b9)
	crow1(b1,b2,b3,b4,b5,b6,b7,b8,b9)
	ccolumn(b1,b2,b3,b4,b5,b6,b7,b8,b9)
	ccolumn1(b1,b2,b3,b4,b5,b6,b7,b8,b9)
	diag(b1,b3,b5,b7,b9)
	diag1(b1,b3,b5,b7,b9)
new=0
#buttons
b1=Button(a,text=' ',padx=110,pady=100,command=lambda:clickb(b1))
b1.grid(column=1,row=1)

b2=Button(a,text=' ',padx=110,pady=100,command=lambda:clickb(b2))
b2.grid(column=2,row=1)

b3=Button(a,text=' ',padx=110,pady=100,command=lambda:clickb(b3))
b3.grid(column=3,row=1)

b4=Button(a,text=' ',padx=110,pady=100,command=lambda:clickb(b4))
b4.grid(column=1,row=2)

b5=Button(a,text=' ',padx=110,pady=100,command=lambda:clickb(b5))
b5.grid(column=2,row=2)

b6=Button(a,text=' ',padx=110,pady=100,command=lambda:clickb(b6))
b6.grid(column=3,row=2)

b7=Button(a,text=' ',padx=110,pady=100,command=lambda:clickb(b7))
b7.grid(column=1,row=3)

b8=Button(a,text=' ',padx=110,pady=100,command=lambda:clickb(b8))
b8.grid(column=2,row=3)
b9=Button(a,text=' ',padx=110,pady=100,command=lambda:clickb(b9))
b9.grid(column=3,row=3)

a.mainloop()
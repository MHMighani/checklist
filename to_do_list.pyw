import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
import pickle
global color1
global money
money = 0
color1='white'
#-------------------classes and functions---------------------------------------------
class check:
	def __init__(self,win,text,row,col,value,color=color1):
		self.var=tk.IntVar()
		self.var.set(value)
		self.text=text
		self.row=row
		self.col=col
		self.value=value
		self.color=color
		self.ch=tk.Checkbutton(win,text=self.text,variable=self.var,background=self.color)
		self.ch.grid(row=row,column=col,sticky=tk.W)

	def delete(self):
		self.ch.destroy()	

	def dic_return(self):
		dic={'text':self.text,'row':self.row,'col':self.col,'value':self.var.get(),'color':self.color}
		return dic


class button:
	def __init__(self,win,text,row,col,command):
		self.bot=ttk.Button(win,text=text,command=command)
		self.bot.grid(row=row,column=col,padx=5,pady=5)


class entery:
	def __init__(self,win,text,row,col):
		self.var=tk.StringVar()		
		self.enter=ttk.Entry(win,text=text,textvariable=self.var)
		self.enter.grid(row=row,column=col,sticky=tk.W,padx=5,pady=5)
		self.enter.focus()

def test_command(event=None):
	global row,col
	print(row)
	file=open('c:/users/hermes/desktop/list.pickle','ab')
	if(en1.enter.get()==''):
		messagebox.showinfo('attention','یه چیزی وارد کن پسر')
		return
	ch1=check(tab1,en1.enter.get(),row,col,0)
	list_of_objects.append(ch1)
	pickle.dump(ch1.dic_return(),file)
	file.close()
	en1.enter.delete(0,'end')
	row+=1

def delete(event=None):
	file=open('list.pickle','wb')
	list2=[]
	global list_of_objects
	for i in list_of_objects:
		if(i.var.get()==1):
			i.delete()
		else:
			list2.append(i)
	list_of_objects=list2[:]

	
			
	file.close()

def dosomething():
	file=open('c:/users/hermes/desktop/list.pickle','wb')
	for i in list_of_objects:
		print(i.dic_return())
		pickle.dump(i.dic_return(),file)
	file.close()	
	file = open('c:/users/hermes/desktop/spends.pickle','wb')	
	for i in list_of_spends:
		print(i)
		pickle.dump(i,file)
	file.close()	
	win.destroy()

def color_change(color):
	win.configure(background=color)
	for i in list_of_objects:
		i.ch.configure(background=color)

def spend_recorder():
	global money,row2,col2
	aa=ttk.Label(tab2,text="price %s"%(en2.enter.get()))
	bb=ttk.Label(tab2,text="date  %s"%(en3.enter.get()))
	money+=int(en2.enter.get())
	cc=ttk.Label(tab2,text="total spend        %d"%money)
	aa.grid(row=row2,column=0,sticky=tk.W)
	bb.grid(row=row2,column=1,sticky=tk.W)
	cc.grid(row=row2+1,column=0,sticky=tk.W)
	list_of_spends.append({'price':en2.enter.get(),'date':en3.enter.get()})
	row2+=1

#-------------------------------main------------------------------------

win=tk.Tk()
win.title('my dashboard')
#--------------------------------tabs------------------------------------
tabcontrol = ttk.Notebook(win)
tab1 = ttk.Frame(tabcontrol)
tabcontrol.add(tab1,text="to do list")
tabcontrol.pack(expand=1,fill="both")
tab2=ttk.Frame(tabcontrol)
tabcontrol.add(tab2,text="expenses")
tabcontrol.pack(expand=1,fill="both")

#-------------------------------to do list main part---------------------
list_of_objects=[]
file=open('c:/users/hermes/desktop/list.pickle','ab')
file.close()
file=open('list.pickle','rb')

row=0
col=0

while(True):
	try:
		aa=pickle.load(file)
		print(aa)
		row+=1
		list_of_objects.append(check(tab1,aa['text'],row,col,aa['value']))

	except Exception as inst:
		print((inst))
		break	
row+=1
win.protocol('WM_DELETE_WINDOW',dosomething)
color_change(color1)

file.close()
en1=entery(tab1,'enter',0,0)
bot1=button(tab1,'create task',0,1,test_command)	
bot2=button(tab1,'delete task',0,2,delete)
file.close()
win.bind('<Delete>',delete)
win.bind('<Return>',test_command)

#------------------------------spend and income part------------------------
list_of_spends=[]
row2=1
col2=0
en2=entery(tab2,'مبلغ هزینه شده',0,0)
en3=entery(tab2,'شرح',0,1)
en3.enter.insert(0,'/03/97')
bot3=button(tab2,'submit',0,2,spend_recorder)

file1=open('c:/users/hermes/desktop/spends.pickle','ab')
file1.close()
file1=open('c:/users/hermes/desktop/spends.pickle','rb')
while(True):
	try:
		aa=pickle.load(file1)
		print(aa)
		list_of_spends.append(aa)
		cc=ttk.Label(tab2,text="price %s"%(aa['price']))
		dd=ttk.Label(tab2,text="date  %s"%(aa['date']))
		cc.grid(row=row2,column=0,sticky=tk.W)
		dd.grid(row=row2,column=1,sticky=tk.W)
		row2+=1

	except:
		break
file1.close()			
#
win.mainloop()


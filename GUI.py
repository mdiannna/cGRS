# coding: latin-1
from Tkinter import *
import time

def centerWindow(self):
		w = 800
		h = 400

		sw = self.winfo_screenwidth()
		sh = self.winfo_screenheight()

		x = (sw - w)/2
		y = (sh - h)/2
		self.geometry('%dx%d+%d+%d' % (w, h, x, y))


t = Tk()
t.title("CGRS - Customizable Gesture Recognition System")

centerWindow(t)

p = PhotoImage(file="bg.png")
p['width'] = t.winfo_screenwidth()+199
p['height'] = t.winfo_screenheight()+1990


l = Label(t, image=p)
l.pack(fill=BOTH, expand=YES)
l.place(x=0, y=-50, width=t.winfo_screenwidth(), height=t.winfo_screenheight(), anchor="nw")


label_name = Label(t, text="Înregistrarea gestului", background="#F44336",
	font=("Helvetica", 26), fg="white", pady=58, padx=230)
label_name.grid(row=0, sticky=W+E+N+S, columnspan=14)


label_gest_name = Label(t, text="Nume:", background="white", fg="#F44336", 
	font=("Helvetica", 14), pady=30)
label_gest_name.grid(row=1, column=6, sticky=W)

entry_gest_name = Entry(t, font=("Helvetica", 14), fg="#212121")
entry_gest_name.grid(row=1, column=7, sticky=W)


label_status = Label(t, text="Scrieți denumirea gestului și tastați OK",
	font=("Helvetica", 14), background="white", fg="#727272", pady=20)
label_status.grid(row=3, columnspan=14, sticky=N+W+E)


def in_progress():
	label_status.configure(text="Înregistrare în proces...  Nu mișcați mîna pe durata înregistrarii")
	label_status.configure(fg="#727272")
	label_status.update_idletasks()

def done(gest_name):
	label_status.configure(text="Gestul " + gest_name + " a fost înregistrat cu succes! ")
	label_status.configure(fg="#D32F2F")
	label_status.update_idletasks()

def callback():
	in_progress()
	gest_name = entry_gest_name.get()	
	print "Numele gestului:" + gest_name
	time.sleep(3)
	done(gest_name)	
	# !!!!!!!!11 Nu uita sa faci uncomment
	# trainGest(gest_name)


btn_ok = Button(t, text="OK", font=("Helvetica", 14), command=callback, 
	background="#F44336",fg="white", activebackground="#F44336", activeforeground="#212121")
btn_ok.grid(row=1, column=8, sticky=W)




t.mainloop()



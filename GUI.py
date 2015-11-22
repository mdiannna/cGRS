 # coding: latin-1
import Tkinter as tk
from Tkinter import *
import time

TITLE_FONT = ("Helvetica", 18, "bold")

class SampleApp(tk.Tk):
    def __init__(self, *args, **kwargs):
        tk.Tk.__init__(self,  *args, **kwargs)
        self.title("CGRS - Customizable Gesture Recognition System")
        self.resizable(width=FALSE, height=FALSE)

        def centerWindow(self):
            w = 800
            h = 500

            sw = self.winfo_screenwidth()
            sh = self.winfo_screenheight()

            x = (sw - w)/2
            y = (sh - h)/2-100
            self.geometry('%dx%d+%d+%d' % (w, h, x, y))

        centerWindow(self)
        # the container is where we'll stack a bunch of frames
        # on top of each other, then the one we want visible
        # will be raised above the others
        container = tk.Frame(self, background="white")
        container.pack(side="top", fill="both", expand=True)
        container.grid_rowconfigure(0, weight=1)
        container.grid_columnconfigure(0, weight=1)


        self.frames = {}
        for F in (AddGest, RecogGest, PageTwo):
            frame = F(container, self)
            self.frames[F] = frame
            # put all of the pages in the same location;
            # the one on the top of the stacking order
            # will be the one that is visible.
            frame.grid(row=0, column=0, sticky="nsew", pady=(0, 20))

        self.show_frame(RecogGest)

    def show_frame(self, c):
        '''Show a frame for the given class'''
        frame = self.frames[c]
        frame.tkraise()


class AddGest(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent, bg="white")
        self.controller = controller
       
        p = PhotoImage(file="bg.png")
        p['width'] = self.winfo_screenwidth()+199
        p['height'] = self.winfo_screenheight()+1990


        l = Label(self, image=p, background="white")
        l.pack(fill=BOTH, expand=YES)
        l.place(x=0, y=-50, width=self.winfo_screenwidth(), height=self.winfo_screenheight(), anchor="nw")


        label_name = Label(self, text="Înregistrarea gestului", background="#F44336",
            font=("Helvetica", 26), fg="white", pady=58, padx=250)
        label_name.grid(row=0, sticky=W+E+N+S, columnspan=14)


        label_gest_name = Label(self, text="Nume:", background="white", fg="#F44336", 
            font=("Helvetica", 14), pady=30)
        label_gest_name.grid(row=1, column=6, sticky=E)

        entry_gest_name = Entry(self, font=("Helvetica", 14), fg="#212121", background="white")
        entry_gest_name.grid(row=1, column=7, sticky=W+E)


        label_status = Label(self, text="Scrieți denumirea gestului și tastați OK",
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
            gest_name = entry_gest_name.get()   
            print "Numele gestului:" + gest_name
            if gest_name:
                in_progress()
                time.sleep(3)
                done(gest_name) 
                # !!!!!!!!11 Nu uita sa faci uncomment
                # trainGest(gest_name)
            else:
                label_status.configure(text="Eroare. Scrieți mai întîi denumirea gestului.")
                label_status.configure(fg="#D32F2F")
                label_status.update_idletasks() 


        btn_ok = Button(self, text="OK", font=("Helvetica", 14), command=callback, 
            background="#F44336",fg="white", activebackground="#D32F2F", activeforeground="white")
        btn_ok.grid(row=1, column=8, sticky=W)

        btn_recog = Button(self, text="Recunoașterea gesturilor", font=("Helvetica", 14),
            background="#F44336",fg="white", activebackground="#D32F2F", activeforeground="white",
            command=lambda: controller.show_frame(RecogGest))
        btn_recog.grid(row=4, column=7, sticky=W+E)


class RecogGest(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller
        

        p = PhotoImage(file="bg.png")
        p['width'] = self.winfo_screenwidth()-100
        p['height'] = self.winfo_screenheight()+1990


        l = Label(self, image=p, background="white")
        l.pack(fill=BOTH, expand=YES)
        l.place(x=0, y=-50, width=self.winfo_screenwidth(), height=self.winfo_screenheight(), anchor="nw")


        label_name = Label(self, text="Recunoașterea gesturilor", background="#F44336",
            font=("Helvetica", 26), fg="white", pady=58, padx=210)
        # label_name['padx'] = self['width'] - label_name['width']
        # print label_name.config(padx=(400-label_name['width'])/2)
        # print self.winfo_width

        label_name.grid(row=0, sticky=W+E, columnspan=12)

        recog_box = Listbox(self)
        # recog_box.insert("Diana")
        recog_box.grid(rowspan=4, column=0, columnspan=12, pady=20, padx=30, sticky=W+E)

        def start_recognition():
            gest_name = "Diana "
            print "Start Recognition" 
            recog_box.insert(0, "Gestul:      ---   " + gest_name + "   ---   " + "  recunoscut la ora: " + str(time.strftime('%X')))
            recog_box.update_idletasks()

            # !!!!!!!!11 Nu uita sa faci uncomment
            # recogGest(gest_name)
        def stop_recognition():
            print "Stop Recognition" 
            recog_box.insert(0, "Stop")
            recog_box.update_idletasks()
            # !!!!!!!!11 Nu uita sa faci uncomment
            # recogGest(gest_name)

        btn_start = Button(self, text="Start", font=("Helvetica", 14), command=start_recognition, 
            background="#F44336",fg="white", activebackground="#D32F2F", activeforeground="white")
        btn_start.grid(row=5, column=5, sticky=W+E)

        btn_stop = Button(self, text="Stop", font=("Helvetica", 14), command=stop_recognition, 
            background="#F44336",fg="white", activebackground="#D32F2F", activeforeground="white")
        btn_stop.grid(row=5, column=6, sticky=W+E)


        btn_recog = Button(self, text="Înregistrarea gesturilor", font=("Helvetica", 14),
            background="#F44336",fg="white", activebackground="#D32F2F", activeforeground="white",
            command=lambda: controller.show_frame(AddGest))
        btn_recog.grid(row=6, column=3, rowspan=4, columnspan=6, sticky=W+E)


class PageTwo(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller
        label = tk.Label(self, text="This is page 2", font=TITLE_FONT)
        label.pack(side="top", fill="x", pady=10)
        button = tk.Button(self, text="Go to the start page",
                           command=lambda: controller.show_frame(StartPage))
        button.pack()


if __name__ == "__main__":
    app = SampleApp()

    app.mainloop()
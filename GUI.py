 # coding: latin-1
import Tkinter as tk
from Tkinter import *
import time
import threading
import atexit
from grsNN import recogGest, trainGest
from grslib import *

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
       
        # p = PhotoImage(file="bg.png")
        # p['width'] = self.winfo_screenwidth()+199
        # p['height'] = self.winfo_screenheight()+1990


        l = Label(self, background="white")
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

       
        def in_progress(gest_name):
            label_status.configure(text="Înregistrare în proces...  Nu mişcaţi mîna pe durata înregistrarii")
            label_status.configure(fg="#727272")
            label_status.update_idletasks()
            trainGest(gest_name)



        def done(gest_name):
            label_status.configure(text="Gestul " + gest_name + " a fost înregistrat cu succes! ")
            label_status.configure(fg="#D32F2F")
            label_status.update_idletasks()


        def callback():
            global stopFlag
            global exitFlag
            stopFlag = 1
            exitFlag = 1
            gest_name = entry_gest_name.get()   
            print "Numele gestului:" + gest_name
            if gest_name:
                in_progress(gest_name)
                # time.sleep(3)
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

        def changeFrame():
            stopFlag = 1
            exitFlag = 1
            controller.show_frame(RecogGest)

        btn_recog = Button(self, text="Recunoașterea gesturilor", font=("Helvetica", 14),
            background="#F44336",fg="white", activebackground="#D32F2F", activeforeground="white",
            command=changeFrame)
        btn_recog.grid(row=4, column=7, sticky=W+E)


exitFlag = 0
stopFlag = 1
Diana = "Diaa=naa"


class myThread (threading.Thread):
    def __init__(self, threadID, name, counter):
        threading.Thread.__init__(self)
        self.threadID = threadID
        self.name = name
        self.counter = counter
    def run(self):
        global Diana
        Diana = recogGest()
        print "Starting " + self.name + Diana
        recognition(self.name, self.counter, 5)
        
        print "Exiting " + self.name

def recognition(threadName, delay, counter):
    global Diana
    while not exitFlag:
        if exitFlag:
            threadName.exit()
        Diana = recogGest()
        # box.insert(0, Diana)
        time.sleep(0.5)
        print "%s: %s" % (threadName, time.ctime(time.time()))
        counter -= 1


class RecogGest(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller
        

        # p = PhotoImage(file="bg.png")
        # p['width'] = self.winfo_screenwidth()-100
        # p['height'] = self.winfo_screenheight()+1990


        l = Label(self, background="white")
        l.pack(fill=BOTH, expand=YES)
        l.place(x=0, y=-50, width=self.winfo_screenwidth(), height=self.winfo_screenheight(), anchor="nw")


        label_name = Label(self, text="Recunoașterea gesturilor", background="#F44336",
            font=("Helvetica", 26), fg="white", pady=58, padx=210)
        # label_name['padx'] = self['width'] - label_name['width']
        # print label_name.config(padx=(400-label_name['width'])/2)
        # print self.winfo_width

        label_name.grid(row=0, sticky=W+E, columnspan=12)
    

        self.recog_box = Listbox(self)
        recog_box = self.recog_box

        # self.recog_box.after(5, updateGUI(self))
        # recog_box.insert("Diana")
        self.recog_box.grid(rowspan=4, column=0, columnspan=12, pady=20, padx=30, sticky=W+E)
        self.listenID = self.after(1000, self.run)

        

        def start_recognition(): 
            global exitFlag
            global stopFlag
            stopFlag = 0
            # AddGest.helloFromOtherClass()
            gest_name = str(Diana)

            print "Start Recognition"  + str(Diana)
            recog_box.insert(0, "Gestul:      ---   " + gest_name + "   ---   " + "  recunoscut la ora: " + str(time.strftime('%X')))
            recog_box.update_idletasks()
             # # Create new threads
            exitFlag = 0
            thread1 = myThread(1, "Thread-1", 7)
            thread1.start()
            
            

            # !!!!!!!!11 Nu uita sa faci uncomment
            # recogGest(gest_name)
        def stop_recognition():
            global exitFlag
            global stopFlag
            stopFlag = 1
            exitFlag = 1
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

        def changeFrame():
            global stopFlag
            global exitFlag
            stopFlag = 1
            exitFlag = 1
            controller.show_frame(AddGest)

        btn_recog = Button(self, text="Înregistrarea gesturilor", font=("Helvetica", 14),
            background="#F44336",fg="white", activebackground="#D32F2F", activeforeground="white",
            command=changeFrame)
        btn_recog.grid(row=6, column=3, rowspan=4, columnspan=6, sticky=W+E)

        

    def run(self):
        if stopFlag == 0:
            self.recog_box.insert(0, "Gestul:      ---   " + str(Diana) + "   ---   " + "  recunoscut la ora: " + str(time.strftime('%X')))
            self.recog_box.update_idletasks()
        self.listenID = self.after(1000, self.run)

    def quit(self):
        self.root.destroy()
        exitFlag = 1


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
    command = sys.argv[2]
    com_port = sys.argv[1]
    try:
        server = sys.argv[3]
    except:
        server = "ws://localhost:5000/echo"

    init_GRS(com_port, server)
    init_server(server)

    app = SampleApp()

    def onExit():
                exitFlag = 0
                print "exited"
                app.destroy()
                stop_server_conn()
                stop_serial_conn()

    app.protocol('WM_DELETE_WINDOW', onExit) 

    app.mainloop()

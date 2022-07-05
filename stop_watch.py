from tkinter import *

root = Tk()
root.title('Stopwatch')
root.config(bg='black')
width, height = 500, 200
screen_width = root.winfo_screenwidth()
screen_height = root.winfo_screenheight()
x = (screen_width / 2) - (width / 2)
y = (screen_height / 2) - (height / 2)
root.geometry('%dx%d+%d+%d' % (width, height, x, y))
millisec = sec = min_ = 00

def Start():
    global time, timer, millisec, sec, min_
    millisec += 1
    if millisec == 100:
        millisec, sec = 0, sec + 1
    if sec == 60:
        sec, min_ = 0, min_ + 1
    timer.config(text=f'{min_}:{sec}:{millisec}')
    time = timer.after(200, Start)

def Stop():
    global time
    timer.after_cancel(time)

def Reset():
    global millisec, sec, min_
    millisec = sec = min_ == 00
    timer.config(text=f'{min_}:{sec}:{millisec}')
    timer.after_cancel(time)

def Exit():
    root.destroy()

Top = Frame(root, width=400, bg="green2")
Top.pack(side=TOP)
Bottom = Frame (root, width=400, bg="black")
Bottom.pack(side=BOTTOM)
Title = Label (Top, text="StopWatch", font=("arial 24 bold"), fg="gold", bg="black")


Title.pack()
timer = Label (Top, font=("times new roman", 45), fg="white", bg="black")
timer.pack(fill=X, expand=NO, pady=10)
timer.config(text=f' {min_}: {sec}: {millisec}')
Startt = Button(Bottom, text='START', font=("arial 20 bold"), fg="purple4", width=6, command=Start)


Startt.pack(side=LEFT, padx=2, pady=5)
Stopp = Button (Bottom, text='STOP', font=("arial 20 bold"),  fg="purple4", width=6, command=Stop)


Stopp.pack(side=LEFT, padx=2, pady=5)
Resett = Button (Bottom, text='RESET', font=("arial 20 bold"),  fg="purple4", width=6, command=Reset)


Resett.pack(side=LEFT, padx=2, pady=5)
Exitt = Button (Bottom, text='CLOSE', font=("arial 20 bold"),  fg="purple4", width=6, command=Exit)


Exitt.pack(side=LEFT, padx=2, pady=5)
root.mainloop()
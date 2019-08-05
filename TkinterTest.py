from tkinter import *  # from main import Run
from macro import Run
import subprocess as sub
import threading

def sendOut(*args):
    res = (resVar.get().split(' x '))
    time = int(e.get())
    res1 = int(res[0])
    res2 = int(res[1])

    print(type(res1))
    print(res1)
    print(res2)
    def callback():
        Run(time, res1, res2 )
        o.insert(0, "asdasd")
    t = threading.Thread(target=callback)
    t.start()

def change_dropdown(*args):
    print(resVar.get())

# def changeOutput():



root = Tk()
root.title("Tk dropdown example")

# Add a grid
dropFrame = Frame(root)
dropFrame.grid(column=0, row=0, sticky='nsew')
dropFrame.columnconfigure(0, weight=1)
dropFrame.rowconfigure(0, weight=1)
# dropFrame.pack(pady = 100, padx = 100)

entryFrame = Frame(root)
entryFrame.grid(column=0, row=1, sticky='nsew')
entryFrame.columnconfigure(0, weight=1)
entryFrame.rowconfigure(0, weight=1)

buttonFrame = Frame(root)
buttonFrame.grid(column=0, row=2, sticky='nsew')
buttonFrame.columnconfigure(0, weight=1)
buttonFrame.rowconfigure(0, weight=1)

# outputFrame = Frame(root)
# outputFrame.grid(column=0, row=3, sticky='nsew')
# outputFrame.columnconfigure(0, weight=1)
# outputFrame.rowconfigure(0, weight=1)


# Create a Tkinter variable
resVar = StringVar(root)
timeVar = StringVar(root)

# Dictionary with options
choices = {'1920 x 1080', '1280 x 720', '640 x 360'}
resVar.set('1920 x 1080')  # set the default option


Label(entryFrame, text="Number of runs:").grid(row=0, column=0, sticky='w')
e = Entry(entryFrame)
e.delete(0, END)
e.insert(0, "1")
e.grid(row=0, column=1)
e.config(width=16)

# Label(outputFrame, text="Output").grid(sticky='w')
# o = Entry(outputFrame, width=30)
# o.delete(0, END)
# o.grid(row=1, column=0,rowspan=3)

popupMenu = OptionMenu(dropFrame, resVar, *choices)
popupMenu.config(width=9)
Label(dropFrame, text="Resolution:").grid(row=0, column=0, sticky='w')
popupMenu.grid(row=0, column=1, sticky='e')
b = Button(buttonFrame, text="OK", command=sendOut, width=13)
Label(buttonFrame, text="Click to start: ").grid(row=0, column=0, sticky='w')
b.grid(row=0, column=1, sticky='nwes')



# link function to change dropdown
resVar.trace('w', change_dropdown)


root.mainloop()

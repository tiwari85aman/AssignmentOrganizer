import tkinter as tk
import fileHandler as fh
import systemScan as sc


root = tk.Tk()
root.geometry("270x300")


#Directory Choice Desktop/Custom...

v = tk.IntVar()
v.set(0)  # initializing the choice, i.e. Python

choices = [
    ("Desktop",1),
    ("Custom",2),
]

def ShowChoice():
    fh.setChoice(v.get())

tk.Label(root, 
         text="""Select Directory (Organize):""",
         justify = tk.LEFT,
         padx = 10).pack()

for val, choice in enumerate(choices):
    tk.Radiobutton(root,
                  text=choice[0],
                  padx = 10, 
                  variable=v, 
                  command=ShowChoice,
                  value=val).pack()


frame= tk.Frame(root, width=150, height = 350)
frame.place(relx=.5, rely=.5, anchor="c")

frame.pack_propagate(0)

everything = tk.Button(frame,
                   text="Organize in same location (Undo allowed)",
                   command=lambda : fh.organiseDesktop(everything,everythingInDocument,byDate,undoButton),
                   padx=20,
                    width=29
                   )

everything.grid(row=1, column=1)

everythingInDocument = tk.Button(frame,
                   text="Organize in Documents",
                   command=lambda : fh.organiseDesktopInDocuments(everything,everythingInDocument,byDate,undoButton),
                   padx=20,
                    width=29
                   )

everythingInDocument.grid(row=2, column=1)

byDate = tk.Button(frame,
                   text="Organize By Date (Undo allowed)",
                   command=lambda : fh.organiseDesktopByDate(everything,byDate,undoButton),
                   padx=20,
                    width=29
                   )
byDate.grid(row=3, column=1)

undoButton = tk.Button(frame,
                   text="Undo Changes",
                   command=lambda : fh.undoChanges(undoButton,everything,everythingInDocument,byDate),
                   padx=20,
                    width=29,
                   )
undoButton.grid(row=4, column=1)
undoButton.config(state="disabled")


systemScanButton = tk.Button(frame,
                   text="System Scan",
                   command=lambda : sc.walkThroughSystem(),
                   padx=20,
                    width=29,
                   )
systemScanButton.grid(row=5, column=1)

quit = tk.Button(frame,
                   text="QUIT",
                   fg="red",
                   command=quit,
                   padx=20,
                 width=29)
quit.grid(row=6, column=1)



root.mainloop()

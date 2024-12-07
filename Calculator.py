from tkinter import * #tk graphical user interface


def click(event): # geting value
    global scvalue
    text = event.widget.cget("text")

    if text == "=": # calculation logic
        if scvalue.get().isdigit(): # for digits
            value = int(scvalue.get())
        elif scvalue.get() == "%": # for percentage
            scvalue.set(scvalue.get() / 100)
        else:
            value = eval(scvalue.get()) # for aggrigation
        scvalue.set(value)
        screen.update()
    elif text == "AC": # for clear screen
        scvalue.set("")
        screen.update()
    else:
        scvalue.set(scvalue.get() + text)
        screen.update()


root = Tk()

# make window
root.geometry("440x570")
root.title("BLACKLION Calculator")
root.iconbitmap(r"C:\Users\DELL\Downloads\icon1.ico") 
root.update()
window_width = root.winfo_width()
window_height = root.winfo_height()
screen_width = root.winfo_screenwidth()
screen_height = root.winfo_screenheight()

window_x = int((screen_width / 2) - (window_width / 2))
window_y = int((screen_height / 2) - (window_height / 2))

root.geometry(f"{window_width}x{window_height}+{window_x}+{window_y}")

# make screen
scvalue = StringVar()
scvalue.set("")
screen = Entry(root, textvariable=scvalue, font="lucida 40 bold")
screen.pack(fill=X, ipadx=8, pady=10, padx=10)

# set buttons
button = [
    ["(", ")", "%", "AC"],
    ["9", "8", "7", "/"],
    ["6", "5", "4", "*"],
    ["3", "2", "1", "-"],
    ["0", ".", "=", "+"],
]

for i in button:
    f = Frame(root, background="Grey", width=50, height=60)
    b = Button(f, text=i[0], width=5, height=2, font="lucida 20 bold")
    b.pack(side=LEFT, padx=6, pady=4)
    b.bind("<Button>", click)
    b = Button(f, text=i[1], width=5, height=2, font="lucida 20 bold")
    b.pack(side=LEFT, padx=6, pady=4)
    b.bind("<Button>", click)
    b = Button(f, text=i[2], width=5, height=2, font="lucida 20 bold")
    b.pack(side=LEFT, padx=6, pady=4)
    b.bind("<Button>", click)
    b = Button(f, text=i[3], width=5, height=2, font="lucida 20 bold")
    b.pack(side=LEFT, padx=6, pady=4)
    b.bind("<Button>", click)
    f.pack()

root.mainloop()
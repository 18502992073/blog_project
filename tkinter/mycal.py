import tkinter
class Window(tkinter.Tk):
    def __init__(self):
        root = tkinter.Tk()

        entry1 = tkinter.Entry()
        entry1.pack()

        label1 = tkinter.Label(root, text="+")
        label1.pack()

        entry2 = tkinter.Entry()
        entry2.pack()


def calculate():
    try:
        num1 = entry1.get()
        num2 = entry2.get()
        res = int(num1) + int(num2)
        label2.config(text=res)
    except:
        label2.config(text="输入有误")

button = tkinter.Button(root, text="=", command=calculate)
button.pack()

label2 = tkinter.Label(root)
label2.pack()

root.mainloop()

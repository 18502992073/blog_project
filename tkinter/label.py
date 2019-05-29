import tkinter

root = tkinter.Tk()
label = tkinter.Label(root, text="这是文字",
                      bg='red', width=24,
                      height=3, font=('黑体', 30))
label.pack()
img = tkinter.PhotoImage(file="0.jpg")
label2 = tkinter.Label(
    root, image=img)

root.mainloop()



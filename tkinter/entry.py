import tkinter

root = tkinter.Tk()
entry = tkinter.Entry(root)
entry.pack()


def on_button():
    s = entry.get()  # 获取entry的字符串
    print(s)
btn = tkinter.Button(root, text="取entry的值", command=on_button)
btn.pack()
root.mainloop()

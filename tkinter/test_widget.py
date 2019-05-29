# widget 小部件，小控件
import tkinter
root = tkinter.Tk()

label = tkinter.Label(root, text="我是label")
label.pack()

btn = tkinter.Button(root, text="我是button")
btn.pack()

checkbox = tkinter.Checkbutton(root, text="看书")
checkbox.pack()

entry = tkinter.Entry(root, text='请输入用户名')
entry.pack()

root.mainloop()
print("程序退出")

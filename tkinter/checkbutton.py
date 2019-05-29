import tkinter
root = tkinter.Tk()
# 创建一个布尔型变量
btn1_value = tkinter.BooleanVar(root, value=False)


def oncheckbtn1():
    print("读书状态：", btn1_value.get())
    if btn1_value.get():
        cbtn2.deselect()
    else:
        cbtn2.select()
cbtn1 = tkinter.Checkbutton(
    root, text="读书", command=oncheckbtn1, variable=btn1_value)
cbtn2 = tkinter.Checkbutton(root, text="看电影")
cbtn1.pack()
cbtn2.pack()

root.mainloop()

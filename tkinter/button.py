import tkinter

root = tkinter.Tk()
times = 0  # 按钮按下的次数


def onbtn_click():
    global times
    print("已点")
    times += 1
    s = "点我(%s)" % times
    btn.config(text=s)

btn = tkinter.Button(
    root, text="点", command=onbtn_click, width=10)
btn.pack()

root.mainloop()

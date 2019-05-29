import tkinter

root = tkinter.Tk()
label = tkinter.Label(root, text="--")
label.pack()
res = 0


def on_timer():
    # print("定时器函数已经调用!")
    global timer_id, res  # 声明timer_id 为全局变量
    timer_id = label.after(1000, on_timer)  # 让定时器重复启动
    res += 1
    label.config(text=res)


def on_start_timer():
    # print("已启动定时器")
    global timer_id
    timer_id = label.after(0, on_timer)


def on_stop_timer():
    label.after_cancel(timer_id)  # 取消定时器
    # print("定时器已取消!")
btn = tkinter.Button(root, text="启动定时器",
                     command=on_start_timer)
btn.pack()
btn2 = tkinter.Button(root, text="取消定时器",
                      command=on_stop_timer)
btn2.pack()
root.mainloop()

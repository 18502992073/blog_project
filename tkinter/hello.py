# 导入tkinter
import tkinter

# 创建顶层窗口
root = tkinter.Tk()

# 创建lable
lable = tkinter.Label(root,
                      text="hello world",
                      bg='#FF0000')
lable.pack()    # 把lable放在窗口上

# 进入主事件循环
root.mainloop()

print("程序退出")

import tkinter


def on_mouse_down(event):
    print("有鼠标键按下", event.x, event.y)


def on_mouse_release(event):
    print("有鼠标键抬起")


def on_key_down(event):
    print("有按键按下：",
          event.keysym, event.char, event.keycode)

root = tkinter.Tk()
root.bind('<Button-1>', on_mouse_down)  # 绑定左键
root.bind('<ButtonRelease>', on_mouse_release)
root.bind('<Key>', on_key_down)
root.mainloop()

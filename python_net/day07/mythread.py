from threading import Thread
from time import *


class MyThread(Thread):
    def __init__(self, target, args=(), kwargs=None):
        super().__init__()
        if kwargs is None:
            kwargs = {}
        self.target = target
        self.args = args
        self.kwargs = kwargs

    def run(self):
        self.target(*self.args, **self.kwargs)


# ***根据如下需求完成上面的MyThread类***
def player(sec, song):
    for i in range(2):
        print("playing %s:%s" % (song, ctime()))
        sleep(sec)


t = MyThread(target=player, args=(3,), kwargs={"song": "凉凉"})
t.start()
t.join()

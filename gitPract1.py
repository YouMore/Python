import math
import tkinter as tk
import time

def pyshader(func, w, h):
    scr = bytearray((0, 0, 0) * w * h)
    for y in range(h):
        for x in range(w):
            p = (w * y + x) * 3
            scr[p:p + 3] = [max(min(int(c * 255), 255), 0)
                            for c in func(x / w, y / h)]
    return bytes('P6\n%d %d\n255\n' % (w, h), 'ascii') + scr

# Ваш код здесь:
def func(x, y):
    c = int(time.time()*1000000)
    return c%(x*y +1),c%(x*y +1), c%(x*y +1)

root = tk.Tk()
img = tk.PhotoImage(data=pyshader(func, 64, 64)).zoom(2, 2)
label = tk.Label(root, image = img)
label.pack()

def newPhoto():
    new_img = tk.PhotoImage(data=pyshader(func, 64, 64)).zoom(2, 2)
    label.configure(image=new_img)
    label.image = new_img
    label.after(1,newPhoto)

newPhoto()
root.mainloop()



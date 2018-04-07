from tkinter import *
import math

def setup_image(w,h):            # faz um canvas e uma imagem que podemos pintar por cima de tamanho w por h
    master = Tk()
    canvas = Canvas(master, width = w, height = h)
    canvas.pack()
    img = PhotoImage(width = w, height = h)
    canvas.create_image((w/2),(h/2), image = img)
    return img

def paint(x,y,w,h,img):                         # pinta nos oito octantes

    img.put("#000000",(x+(w//2),y+(h//2)))
    img.put("#000000",(x+(w//2),(h//2)-y))
    img.put("#000000",((w//2)-x,y+(h//2)))
    img.put("#000000",((w//2)-x,(h//2)-y))
    img.put("#000000",(y+(w//2),x+(h//2)))
    img.put("#000000",((w//2)-y,x+(h//2)))
    img.put("#000000",((w//2)+y,(h//2)-x))
    img.put("#000000",((w//2)-y,(h//2)-x))

def tradicional(r,w,h,img):                 # pintando só quando é numero inteiro
    for x in range(h):
        for y in range(w):
            if (x ** 2 + y ** 2 == r ** 2):
                paint(x,y,w,h,img)

#def polar(r,w,h,img):

def medium_point(r,w,h,img):
    x = 0
    y = r
    d = 1 - r

    paint(x,y,w,h,img)
    
    while (y > x):
        if (d < 0):
            d = d + 2 * x + 3
            x = x + 1
        else:
            d = d + 2 * (x - y) + 5
            x = x + 1
            y = y - 1

        paint(x,y,w,h,img)

w = h = 800
img = setup_image(w,h)
medium_point(100,w,h,img)
#tradicional(100,w,h,img)

mainloop()

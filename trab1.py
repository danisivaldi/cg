from tkinter import *
import time
import math

def setup_image(w,h):            # faz um canvas e uma imagem que podemos pintar por cima de tamanho w por h
    master = Tk()
    canvas = Canvas(master, width = w, height = h, bg = "#FFFFFF")
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


def tradicional(r,w,h,img):
    x = -r
    y = 0
    
    while x <= r:
        y = int(math.sqrt(r ** 2 - x ** 2))
        paint(x,y,w,h,img)
        y = int(-1 * math.sqrt(r ** 2 - x ** 2))
        paint(x,y,w,h,img)
        x = x + 1


def polar(r,w,h,img):
    teta = 0

    while teta <= 360:
        x = int(r * math.cos(teta))
        y = int(r * math.sin(teta))
        paint(x,y,w,h,img)
        teta = teta + 1


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


inicio = time.time()

w = h = 3000
img = setup_image(w,h)

print("digite o raio: ")
r = int(input())

print("digite:\n1-algoritmo do ponto médio\n2-algorimo tradicional\n3-algoritmo usando coordenadas polares")
op = int(input())

if op == 1:
    medium_point(r,w,h,img)
elif op == 2:
    tradicional(r,w,h,img)
else:
    polar(r,w,h,img)

print("tempo de execução: " + str(time.time() - inicio))

mainloop()


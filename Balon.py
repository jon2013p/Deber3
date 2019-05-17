from tkinter import*
from tkinter import messagebox
tk=Tk()
x=0
y=0
canvas=Canvas(tk,width=450,height=300)
canvas.pack()
balon=PhotoImage(file='ball.gif')
cancha=PhotoImage(file='cancha.gif')
canvas.create_image(0,0,anchor=NW, image=cancha)
canvas.create_image(80,150,anchor=NW, image=balon)


def movetriangule(event):
    global y,x
    if event.keysym=='Up':
        canvas.move(2,0,-6)
        y=y-6
    elif event.keysym=='Down':
        canvas.move(2,0,6)
        y=y+6
    elif event.keysym=='Left':
        canvas.move(2,-6,0)
        x=x-6
    else:        
        canvas.move(2,6,0)
        x=x+6
    if x==342 or x==-84:
        messagebox.showinfo(message='GOOOOOOOOOL', title='Titulo')

    print(str(x),''+str(y))
    
canvas.bind_all('<KeyPress-Up>',movetriangule)
canvas.bind_all('<KeyPress-Down>',movetriangule)
canvas.bind_all('<KeyPress-Left>',movetriangule)
canvas.bind_all('<KeyPress-Right>',movetriangule)



tk.mainloop()


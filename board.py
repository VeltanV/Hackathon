from tkinter import *

#TODO: object orient this to class Level One, Level Two .... 
#TODO: find pictures, (GIF) to representent board
#TODO: Make labels in top of canvas to show Level, points and so on 
#TODO: Lock playing field so you cant adjust it 

height_of_canvas = 300
width_of_canvas = 600

root = Tk()
board = Canvas(root, width=width_of_canvas, height=height_of_canvas)
board.pack()

img = PhotoImage(file="fim.gif")
board.create_image(0, 0, anchor=NW, image=img)

mainloop()




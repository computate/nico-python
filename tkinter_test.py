'''
Created on Feb 20, 2022
@author: ntate

Prerequisites:

tkinter
pkcon install -y python3-tkinter

'''
import tkinter
import tkinter.dialog
import tkinter.filedialog


def set_color_black(event):
    global color
    color = "black"
def set_color_grey(event):
    global color
    color = "grey"
def set_color_lightgrey(event):
    global color
    color = "lightgrey"
def set_color_white(event):
    global color
    color = "white"
def set_color_brown(event):
    global color
    color = "brown"
def set_color_darkred(event):
    global color
    color = "darkred"
def set_color_red(event):
    global color
    color = "red"
def set_color_pink(event):
    global color
    color = "pink"
def set_color_darkorange(event):
    global color
    color = "darkorange"
def set_color_orange(event):
    global color
    color = "orange"
def set_color_yellow(event):
    global color
    color = "yellow"
def set_color_lightyellow(event):
    global color
    color = "lightyellow"
def set_color_darkgreen(event):
    global color
    color = "darkgreen"
def set_color_green(event):
    global color
    color = "green"
def set_color_lightgreen(event):
    global color
    color = "lightgreen"
def set_color_darkblue(event):
    global color
    color = "darkblue"
def set_color_blue(event):
    global color
    color = "blue"
def set_color_lightblue(event):
    global color
    color = "lightblue"
def set_color_purple(event):
    global color
    color = "purple"
def set_color_violet(event):
    global color
    color = "violet"

def clear(event):
    global draw_canvas
    draw_canvas.destroy()
    draw_canvas = tkinter.Canvas(window, width=1000, height=500, bg="white")
    draw_canvas.pack() 
    draw_canvas.bind("<Button-1>", on_click)
    draw_canvas.bind("<B1-Motion>", on_drag)

def on_click(event):
    store_position(event)
def store_position(event):
    global lastX, lastY
    lastX = event.x
    lastY = event.y
def on_drag(event):
    draw_canvas.create_line(lastX, lastY, event.x, event.y, fill = color, width = 3)
    store_position(event)

if __name__ == '__main__':
    color= "black"
    lastX, lastY = 0,0

    window = tkinter.Tk(className="tkinter test program")

    button = tkinter.Button(window, text="Quit", background="red", width=90, height=1, command=window.destroy)
    button.pack(padx=30, pady=10)

    label = tkinter.Label(window, text="Choose a color below and click on it. Then click and drag on the canvas to draw.")
    label.pack()

    color_canvas = tkinter.Canvas(window, width=1000, height=30)
    color_canvas.pack(pady=10) 

    draw_canvas = tkinter.Canvas(window, width=1000, height=500, bg="white")
    draw_canvas.pack() 

    draw_canvas.bind("<Button-1>", on_click)
    draw_canvas.bind("<B1-Motion>", on_drag)
    
    
    

    color_canvas.tag_bind(color_canvas.create_rectangle(10, 0, 40, 30, fill="black"), "<Button-1>", set_color_black)
    color_canvas.tag_bind(color_canvas.create_rectangle(50, 0, 80, 30, fill="grey"), "<Button-1>", set_color_grey)
    color_canvas.tag_bind(color_canvas.create_rectangle(90, 0, 120, 30, fill="lightgrey"), "<Button-1>", set_color_lightgrey)
    color_canvas.tag_bind(color_canvas.create_rectangle(130, 0, 160, 30, fill="white"), "<Button-1>", set_color_white)
    color_canvas.tag_bind(color_canvas.create_rectangle(180, 0, 210, 30, fill="brown"), "<Button-1>", set_color_brown)
    color_canvas.tag_bind(color_canvas.create_rectangle(230, 0, 260, 30, fill="darkred"), "<Button-1>", set_color_darkred)
    color_canvas.tag_bind(color_canvas.create_rectangle(270, 0, 300, 30, fill="red"), "<Button-1>", set_color_red)
    color_canvas.tag_bind(color_canvas.create_rectangle(310, 0, 340, 30, fill="pink"), "<Button-1>", set_color_pink)
    color_canvas.tag_bind(color_canvas.create_rectangle(360, 0, 390, 30, fill="darkorange"), "<Button-1>", set_color_darkorange)
    color_canvas.tag_bind(color_canvas.create_rectangle(400, 0, 430, 30, fill="orange"), "<Button-1>", set_color_orange)
    color_canvas.tag_bind(color_canvas.create_rectangle(450, 0, 480, 30, fill="yellow"), "<Button-1>", set_color_yellow)
    color_canvas.tag_bind(color_canvas.create_rectangle(490, 0, 520, 30, fill="lightyellow"), "<Button-1>", set_color_lightyellow)
    color_canvas.tag_bind(color_canvas.create_rectangle(540, 0, 570, 30, fill="lightgreen"), "<Button-1>", set_color_lightgreen)
    color_canvas.tag_bind(color_canvas.create_rectangle(580, 0, 610, 30, fill="green"), "<Button-1>", set_color_green)
    color_canvas.tag_bind(color_canvas.create_rectangle(620, 0, 650, 30, fill="darkgreen"), "<Button-1>", set_color_darkgreen)
    color_canvas.tag_bind(color_canvas.create_rectangle(670, 0, 700, 30, fill="lightblue"), "<Button-1>", set_color_lightblue)
    color_canvas.tag_bind(color_canvas.create_rectangle(710, 0, 740, 30, fill="blue"), "<Button-1>", set_color_blue)
    color_canvas.tag_bind(color_canvas.create_rectangle(750, 0, 780, 30, fill="darkblue"), "<Button-1>", set_color_darkblue)
    color_canvas.tag_bind(color_canvas.create_rectangle(800, 0, 830, 30, fill="purple"), "<Button-1>", set_color_purple)
    color_canvas.tag_bind(color_canvas.create_rectangle(840, 0, 870, 30, fill="violet"), "<Button-1>", set_color_violet)
    color_canvas.tag_bind(color_canvas.create_rectangle(960, 0, 990, 30, fill="red"), "<Button-1>", clear)
    color_canvas.mainloop()

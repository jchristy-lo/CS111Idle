import Tkinter as tk

class rabbit:
    def __init__(self):
        #self.size = 100
        #self.canvas = canvas
        #self.click = click
        self.image = tk.PhotoImage(file = 'rabbit.gif')
        self.weight = 8

    def getRabbit(self,x,y):
        self.canvas.create_image(x,y, image=self.image)
    
    def move(self):
        pass

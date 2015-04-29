#Jamie Christy and Mai Li Goodman
#CS 111 Final Project
#Framework Script

import Tkinter as tk
import animation
import random
import rabbit

import Image
import ImageTk

class GameApp(tk.Frame):
    
    def __init__(self, root):
        tk.Frame.__init__(self, root, pady=20,padx=20,width=600, height=600)
        root.title('RABBITS RABBITS RABBITS')
        self.frame = tk.Frame(root)
        
        self.canvas = tk.Canvas(root)
        
        self.grid()
        self.grid_propagate(0)
        
        self.power = 1
        self.rabbitCount = 1
        self.setUp() 
        #self.spawn()

    def setUp(self):
        '''places a score counter and the first rabbit'''
        score = tk.Label(self, text='You have '+str(self.rabbitCount)+' rabbits!!!', font='Cambria 20 bold')
        score.grid(row=0,sticky=tk.N)
        x = random.randint(100,500)
        y = random.randint(100,500)
        
        firstRabbit = tk.PhotoImage(file = 'rabbit.gif')
        label = tk.Label(self,image = firstRabbit,background="red")
        label.grid(row=0,column=0)
        
        #self.canvas.create_image(200,200, image=firstRabbit)
        
    
root = tk.Tk()
app = GameApp(root)
app.mainloop()

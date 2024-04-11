#Main
import customtkinter as ctk
import tkinter as tk
from PIL import Image, ImageTk

from random import choice,choices
from random import sample

#Function for oposite sockets (Extra Code - 1)
from int_class import OppositeSocket as ops

#Functions to reduce/collapse variables (Extra Code - 2)
from collapsed_func import CollapseSide as cps
from collapsed_func import CollapsedFunc as cpf

#Index Images (Extra Code - 3)
from image_index import TileImageIndex

tiles = []
sides = [1,2,3,4]

root = tk.Tk()

#Tile Object
class TileCreator(tk.Canvas):
    def __init__(self, parent, cols, rows, tiles_num, tile = TileImageIndex["blank"], width = 50, height = 50,**kwargs):
        super().__init__(parent, width= width-2, height= height-2, **kwargs)
        self.width, self.height = width, height
        img_path, self.sockets = tile
        p, self.blank_sockets = tile  
        #Grid Info
        self.cols = cols
        self.rows = rows
        self.tiles_num = tiles_num

        self.state = "not analized"

        self.load_image(img_path)
        self.blank()

    #First loading
    def load_image(self, img_path):
        self.image = Image.open(img_path)
        self.tk_image = ImageTk.PhotoImage(self.image)

    def blank(self):
        self.sockets = self.blank_sockets     
        image = self.image.resize((self.width, self.height))
        self.tk_image = ImageTk.PhotoImage(image) 
        self.create_image(0, 0, image=self.tk_image, anchor="nw")
        self.create_text(0, 0, text= self.tiles_num, anchor="nw", font= ("Arial", 20))
        self.state = "not analized"

    #Render Image
    def show_image(self, tile):
        path, self.sockets  = TileImageIndex[tile]
        self.delete("all")
        image = Image.open(path)    
        self.tk_image = ImageTk.PhotoImage(image)
        image = image.resize((self.width, self.height))
        self.tk_image = ImageTk.PhotoImage(image)
        self.create_image(0, 0, image=self.tk_image, anchor="nw")
        self.state = "analized"

    #Extra function
    def random_image(self):
        keys = [str(k) for k in TileImageIndex.keys()]
        path, self.sockets  = TileImageIndex[choice(keys)]
        self.delete("all")
        image = Image.open(path)    
        self.tk_image = ImageTk.PhotoImage(image)
        image = image.resize((self.width, self.height))
        self.tk_image = ImageTk.PhotoImage(image)
        self.create_image(0, 0, image=self.tk_image, anchor="nw")

    #Analizes Neighbours
    def analyze(self):
        self.me = tiles.index(self)
        self.bord_sockets = (0, 0, 0, 0)


        for sid in range(len(sides)):
            if sid == 0:  # Top
                if(self.me - self.cols > -1):
                    self.up_me = tiles[self.me - self.cols]
                    self.up_poss = cps(sid, self.up_me.sockets)
                else:
                    self.up_me = "None"
                    self.up_poss = cps(sid, self.bord_sockets)

            elif sid == 1:  # Right
                if((self.me + 1)%self.cols != 0):
                    self.right_me = tiles[self.me + 1]
                    self.right_poss = cps(sid, self.right_me.sockets)
                else:
                    self.right_me = "None"
                    self.right_poss = cps(sid, self.bord_sockets)

            elif sid == 2:  # Bottom
                if((self.me + self.cols) < (self.cols*self.rows)):
                    self.down_me = tiles[self.me + self.cols]
                    self.down_poss = cps(sid, self.down_me.sockets)
                else:
                    self.down_me = "None"
                    self.down_poss = cps(sid, self.bord_sockets)

            elif sid == 3:  # Left
                if((self.me % self.cols) != 0):
                    self.left_me = tiles[self.me - 1]
                    self.left_poss = cps(sid, self.left_me.sockets)
                else:
                    self.left_me = "None"
                    self.left_poss = cps(sid, self.bord_sockets)
    
        self.all_pos = cpf(self.up_poss, self.right_poss, self.down_poss, self.left_poss)
        
        a_choice = choice(self.all_pos)
        print(f'\nchoice: {a_choice}')
        self.show_image(a_choice)

#Renders Blank Tiles
def CreateTiles(parent, col, row, width = 50, height = 50):
    in_row = 1
    in_col = 0
    for tile in range(0, col*row):
        in_col += 1

        if ((tile)%col) == 0:
            in_col = 1
            in_row += 1

        img = TileCreator(parent, tiles_num= tile,cols= col, rows= row, height= height, width=width, bg="red")  
        img.grid(column=in_col,row= in_row)

        tiles.append(img)

#------------------ Buttons Functions ------------------
def random(tile):
    tile.analyze()

def start():
    print("Started")
    aleatory_tiles = []
    aleatory_tiles.clear()
    aleatory_tiles = sample(tiles, k= len(tiles))
   
    for tile in aleatory_tiles:
        print(f'me: {tile}')
        if tile.state != "analized":
            tile.analyze()

def reset():
    print('\n---------------Reset------------------------')
    for tile in tiles:
        tile.blank()

def shofell():
    i  = 100
    for num in range(i):
        rando = choice(tiles)
        if rando.state != "analized":
            random(rando)

options_frame = ctk.CTkFrame(root)

button = tk.Button(options_frame, text= "Choose Random")
button.config(command=lambda: random(choice(tiles)))
button.pack(side= "left")

button = tk.Button(options_frame, text= "Start")
button.config(command=lambda: start())
button.pack(side= "left")

button = tk.Button(options_frame, text= "Reset")
button.config(command=lambda: reset())
button.pack(side= "left")

button = tk.Button(options_frame, text= "Shoffle")
button.config(command=lambda: shofell())
button.pack(side= "left")




#------------------ Options to chose ------------------
cols = 30 #Num of Columns
rows = 30 #Num of Rows

CreateTiles(root, cols, rows, 
            width= 15, # Width of tiles
            height= 15) # Height of tiles


options_frame.grid(row = 1000, column = 1, columnspan = cols)
root.mainloop()
#Collapsed functions
##Extra code 2

import tkinter as tk

from int_class import OppositeSocket as ops

from image_index import TileImageIndex

sides = [1,2,3,4]



class CollapseSide():
    def __new__(cls, side: int, sec_sockets: tuple):
        cls.side = side
        cls.sec_sockets = sec_sockets
        cls.poss_value_sockets = [s for path,s in TileImageIndex.values()]


        cls.poss_tiles = []

        if cls.sec_sockets == cls.poss_value_sockets[len(cls.poss_value_sockets) - 1]:
            cls.poss_tiles = [x for x in TileImageIndex.keys() if x != "blank"]
        else:
            cls.compare_socket(ops(side))
        poss_tiles = cls.poss_tiles
        return poss_tiles
        
    @classmethod
    def compare_socket(cls, side_i):
        sock_i = side_i

        poss_sockets = []
    
        for option in cls.poss_value_sockets:
            
            if option[cls.side] == cls.sec_sockets[sock_i]:
                poss_sockets.append(option)

        for option in poss_sockets:
            for key, value in TileImageIndex.items():
                path, socket = value
                if socket == option:
                  cls.poss_tiles.append(key)
            
                



class CollapsedFunc():
    def __new__(cls, top: list, right: list, bottom: list, left: list):
        cls.top = set(top)
        cls.right = set(right)
        cls.bottom = set(bottom)
        cls.left = set(left)

        #print(f'\ntop: {top} \nright: {right} \nbottom: {bottom} \nleft: {left}')
        
        # Encuentra la intersección de todos los conjuntos
        cls.all_pos = cls.top & cls.right & cls.bottom & cls.left
        #print(cls.all_pos)
        # Convierte el conjunto de nuevo a una lista
        cls.all_pos = [x for x in cls.all_pos]

        #print(f'final: {cls.all_pos}')

        return cls.all_pos
                    


#side_collapsed = CollapseSide(0, (-1, -1, -1, -1))
#side_collapsed1 = CollapseSide(1, (1, 0, 1, 1))
#side_collapsed2 = CollapseSide(2, (0, 0, 1, 0))
#side_collapsed3 = CollapseSide(3, (1, 1, 1, 1))

#full_collapse = CollapsedFunc(side_collapsed, side_collapsed1, side_collapsed2, side_collapsed3)

#print(full_collapse)
   
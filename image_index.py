#Image Index
##Extra code 3

TileImageIndex = {

#_|_ conections
'top': ("Assets/Grids/Top.png", (1, 1, 0, 1)),
'right': ("Assets/Grids/Right.png", (1, 1, 1, 0)),
'bottom': ("Assets/Grids/Bottom.png", (0, 1, 1, 1)),
'left': ("Assets/Grids/Left.png", (1, 0, 1, 1)),

#Conections +
'cross': ("Assets/Grids/Cross.png", (1, 1, 1, 1)),

#RightConections -- & |
'hor': ("Assets/Grids/MiddleHor.png", (1, 0, 1, 0)),
'ver':("Assets/Grids/MiddleVer.png", (0, 1, 0, 1)),

#NoEnds -◉
'top_end' : ("Assets/Grids/NoEndTop.png", (1, 0, 0, 0)),
'right_end': ("Assets/Grids/NoEndRight.png", (0, 1, 0, 0)),
'bottom_end': ("Assets/Grids/NoEndBottom.png", (0, 0, 1, 0)),
'left_end': ("Assets/Grids/NoEndLeft.png", (0, 0, 0, 1)),

#Corners L
'corner_top' : ("Assets/Grids/CornerTop.png", (1, 0, 0, 1)),
'corner_right' : ("Assets/Grids/CornerRight.png", (1, 1, 0, 0)),
'corner_bottom' : ("Assets/Grids/CornerBottom.png", (0, 1, 1, 0)),
'corner_left' : ("Assets/Grids/CornerLeft.png", (0, 0, 1, 1)),

'none': ("Assets/Grids/None.png", (0, 0, 0, 0)),

'blank': ("Assets/Grids/None.png", (-1, -1, -1, -1))

}
#Opposide side Manager
##Extra code 4

sides = [1,2,3,4]

class OppositeSocket(int):
    def __new__(cls, side: int):
        if not isinstance(side, int):
            raise ValueError("side must be an integer")
        if side < 0 or side >= len(sides):
            raise ValueError("side must be within the range of array")


        cls.oppos_side = cls.opposite_side(side)
        return cls.oppos_side
        #return sides[cls.oppos_side]
    
    @classmethod
    def opposite_side(cls, side):
        if(side + 2 > len(sides)-1):
            return abs(len(sides) - (side + 2))     
        else:       
            return side + 2

#chosing = OppositeSocket(2)
#print(chosing)

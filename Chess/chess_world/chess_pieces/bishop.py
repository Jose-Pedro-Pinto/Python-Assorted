from .chess_piece import *
class bishop(chess_piece):
    def __init__(self,pos,image=None,team=None):
        super(bishop,self).__init__(pos,"bishop",image,team=team)
    def get_moves(self,pieces):
        moves=[]
        for i in range(-1,2):
            for j in range(-1,2):
                for k in range(1,8):
                    if (i!=j and -i!=j) or i==j==0:
                        break
                    if 0<=self.pos[0]+k*j<8 and 0<=self.pos[1]+k*i<8:
                        p = pieces[(self.pos[0]+k*j,self.pos[1]+k*i)]
                        if p:
                            if p.team!=self.team:
                                moves.append((self.pos[0]+k*j,self.pos[1]+k*i))
                            break
                        moves.append((self.pos[0]+k*j,self.pos[1]+k*i))
                    else:
                        break
        return moves
        


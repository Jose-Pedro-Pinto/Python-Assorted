from .chess_piece import *
class knight(chess_piece):
    def __init__(self,pos,image=None):
        super(knight,self).__init__(pos,"knight",image)
    def get_moves(self,pieces):
        moves=[]
        for i in range(-1,2):
            for j in range(-1,2):
                if j==0 or i==0:
                    continue
                if 0<=self.pos[0]+j<8 and 0<=self.pos[1]+2*i<8:
                    p=pieces[(self.pos[0]+j,self.pos[1]+2*i)]
                    if p:
                        if p.team!=self.team:
                            moves.append((self.pos[0]+j,self.pos[1]+2*i))
                    else:
                        moves.append((self.pos[0]+j,self.pos[1]+2*i))
                if 0<=self.pos[0]+2*j<8 and 0<=self.pos[1]+i<8:   
                    p=pieces[(self.pos[0]+2*j,self.pos[1]+i)]
                    if p:
                        if p.team!=self.team:
                            moves.append((self.pos[0]+2*j,self.pos[1]+i))
                    else:
                        moves.append((self.pos[0]+2*j,self.pos[1]+i))
        return moves
    
        


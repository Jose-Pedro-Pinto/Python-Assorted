from .chess_piece import *
class rook(chess_piece):
    def __init__(self,pos,image=None):
        super(rook,self).__init__(pos,"rook",image)
        self.first_move=True
    def get_moves(self,pieces):
        moves=[]
        for i in range(-1,2):
            for j in range(-1,2):
                for k in range(1,8):
                    if i==j or -i==j:
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
    def move(self,pos):
        super(rook,self).move(pos)
        self.first_move=False

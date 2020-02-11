from .chess_piece import *
class king(chess_piece):
    def __init__(self,pos,image=None):
        super(king,self).__init__(pos,"king",image)
        self.first_move=True
    def get_moves(self,pieces):
        moves=[]
        for i in range(-1,2):
            for j in range(-1,2):
                if i == j == 0:
                    continue
                if 0<=self.pos[0]+j<8 and 0<=self.pos[1]+i<8:
                    p = pieces[(self.pos[0]+j,self.pos[1]+i)]
                    if p:
                        if p.team==self.team:
                            continue
                    moves.append((self.pos[0]+j,self.pos[1]+i))
        return moves
    def move(self,pos):
        super(king,self).move(pos)
        self.first_move=False


from .chess_piece import *
class pawn(chess_piece):
    def __init__(self,pos,image=None):
        super(pawn,self).__init__(pos,"pawn",image)
        self.first_move=True
    def get_moves(self,pieces):
        moves=[]
        if self.pos[1]+self.team>=0 and self.pos[1]+self.team<8:
            if  not pieces[(self.pos[0],self.pos[1]+self.team)]:
                moves.append((self.pos[0],self.pos[1]+self.team))
                if self.first_move and not pieces[(self.pos[0],self.pos[1]+2*self.team)]:
                    moves.append((self.pos[0],self.pos[1]+2*self.team))
            if self.pos[0]+1<8:
                if pieces[self.pos[0]+1,self.pos[1]+self.team]:
                    if pieces[self.pos[0]+1,self.pos[1]+self.team].team!=self.team:
                        moves.append((self.pos[0]+1,self.pos[1]+self.team))
            if self.pos[0]-1>=0:
                if pieces[self.pos[0]-1,self.pos[1]+self.team]:
                    if pieces[self.pos[0]-1,self.pos[1]+self.team].team!=self.team:
                        moves.append((self.pos[0]-1,self.pos[1]+self.team))
        return moves
    def move(self,pos):
        super(pawn,self).move(pos)
        self.first_move=False
        
        


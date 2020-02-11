from pygame.locals import *
import pygame
from .chess_pieces import *
class chess_world(object):
    def __init__(self,pieces,screen):
        self.pieces={}
        for i in range(8):
            for j in range(8):
                self.pieces[(i,j)]=None
        for piece in pieces:
            self.pieces[piece.pos]=piece
        self.board=chess_board(screen)
        self.image_correct()

        
    def select_piece(self):
        self.board.select()
        return self.pieces[self.board.selected_square]

    
    def move_piece(self,piece):
        if not piece:
            return False
        self.board.select()
        moves = self.get_moves(piece)
        for move in moves:
            if move == self.board.selected_square:
                self.pieces[piece.pos]=None
                self.pieces[move]=piece
                piece.move(move)
                return True
        return False

    
    def image_correct(self):
        for piece in self.pieces.values():
            if piece:
                if piece.image:
                    piece.correct_size((
                        self.board.square_size,
                        self.board.square_size
                        ))

                    
    def show_moves(self,piece):
        moves=self.get_moves(piece)
        for move in moves:
            p = self.pieces[move]
            x,y=self.board.get_square_pos(move)
            x=int(x+self.board.square_size/2)
            y=int(y+self.board.square_size/2)
            if p:
                if p.name=='king':
                    pygame.draw.circle(
                        self.board.screen,
                        (150,0,255),
                        (x,y),
                        self.board.square_size//4
                        )
                else:
                    pygame.draw.circle(
                        self.board.screen,
                        (255,255,0),
                        (x,y),
                        self.board.square_size//4
                        )
            else:
                pygame.draw.circle(
                    self.board.screen,
                    (0,255,0),
                    (x,y),
                    self.board.square_size//4
                    )
            if piece.is_cheking(self.pieces,move):
                pygame.draw.circle(
                    self.board.screen,
                    (255,0,0),
                    (x,y),
                    self.board.square_size//4
                    )
    def draw_pieces(self):
        for piece in self.pieces.values():
            if piece:
                x=piece.pos[0]*self.board.square_size+self.board.pos[0]
                y=piece.pos[1]*self.board.square_size+self.board.pos[1]
                piece.draw(self.board.screen,(int(x),int(y)))
    def get_moves(self,piece):
        moves1=piece.get_moves(self.pieces)
        moves=[]
        pos=piece.pos
        for move in moves1:
            p=self.pieces[move]
            self.pieces[pos]=None
            self.pieces[move]=piece
            piece.pos=move
            if self.check_check(team=piece.team):
                pass
            else:
                moves.append(move)
            self.pieces[move]=p
            self.pieces[pos]=piece
            piece.pos=pos
        return moves
    def check_game_end(self):
        alive_1=False
        alive_2=False
        for piece in self.pieces.values():
            if piece:
                if piece.name=="king":
                    if piece.team==1:
                        alive_1=True
                    elif piece.team==-1:
                        alive_2=True
        if not alive_1:
            return -1
        elif  not alive_2:
            return 1
        else:
            return 0

        
    def check_check(self,pos=None,team=None):
        king1=pos
        king2=pos
        #find king position
        if not pos:
            for piece in self.pieces.values():
                if piece:
                    if piece.name=="king":
                        if piece.team==1:
                            king1=piece.pos
                        elif piece.team==-1:
                            king2=piece.pos
        #verify check
        for piece in self.pieces.values():
            if piece:
                moves=piece.get_moves(self.pieces)
                for move in moves:
                    if move == king1:
                        if team:
                            if team==1:
                                return True
                            else:
                                return False
                        return 1
                    elif move == king2:
                        if team:
                            if team==-1:
                                return True
                            else:
                                return False
                        return -1
        if team:
            return False
        else:
            return 0
    def check_checkmate(self,team):
        for piece in self.pieces.values():
            if piece:
                if piece.team==team:
                    temp=self.get_moves(piece)
                    if len(temp)!=0:
                        return False
        return True
    
class chess_board(object):
    def __init__(self,screen):
        self.screen=screen
        self.image=self.create_chess_board()
        self.pos=self.get_board_pos()
        self.square_size=self.image.get_width()//8
        self.selected=None
        self.selected_square=None

        
    def create_chess_board(self):
        size = min(self.screen.get_height(),self.screen.get_width())
        square_size=size//8
        board = pygame.surface.Surface((size,size)).convert()
        for i in range(8):
            offset = i%2
            for j in range(4):
                rect = (
                    square_size*j*2+offset*square_size,
                    square_size*i,
                    square_size,
                    square_size
                    )
                pygame.draw.rect(board,(255,255,255),rect)
        return board

    
    def get_board_pos(self):
        x,y=self.screen.get_size()
        w,z=self.image.get_size()
        x=x/2-w/2
        y=y/2-z/2
        return (x,y)

    
    def select(self):
        x,y=pygame.mouse.get_pos()
        #center on board
        x-=self.pos[0]
        y-=self.pos[1]
        #choose square
        x=x//self.square_size
        y=y//self.square_size
        if x<0 or y<0 or x>8 or y>8:
            return
        self.selected_square=(x,y)
        #move to square pos
        x*=self.square_size
        y*=self.square_size
        #recenter on screen
        square_pos=(x+self.pos[0],y+self.pos[1])
        square=(square_pos,(self.square_size,self.square_size))
        self.selected=square

        
    def get_square_pos(self,pos):
        x,y=pos
        #resize to square size
        x*=self.square_size
        y*=self.square_size
        #center on square
        x+=self.pos[0]
        y+=self.pos[1]
        return (x,y)

    
    def show_selected(self):
        if self.selected:
            pygame.draw.rect(self.screen,(0,255,0),self.selected)

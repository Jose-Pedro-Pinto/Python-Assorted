#<imports>
import pygame
import time
from pygame.locals import *
#</imports>
#<screen>
pygame.init()
screen_size = (1920,1080)
screen = pygame.display.set_mode(screen_size,FULLSCREEN,32)
#</screen>
#<functions>
def quit_game():
    screen=pygame.display.set_mode((1,1),NOFRAME,0)
def end_game(player):
    if player == 1:
        text = "Red"
        color=(255,0,0)
    elif player == -1:
        text = "Blue"
        color=(0,0,255)
    else:
        text = "Gender Fluid Player"
        color=(150,150,150)
    font=pygame.font.SysFont("arial",170)
    h=font.get_linesize()
    screen.blit(font.render(text+" Has Won",True,color),(1920-1500,(1080-h)//2))
    font=pygame.font.SysFont("arial",20)
    screen.blit(font.render("Press 'Esc' to exit",True,(255,0,255)),(1920-1500,(1080+h)//2))
    pygame.display.update()
    while True:
        #Waiting until you press escape
        event=pygame.event.wait()
        if event.type==KEYDOWN:
            if event.key==K_ESCAPE:
                quit_game()
                return True
def draw_turn_text(player):
    if player == 1:
        text = "Red's"
        color=(255,0,0)
    elif player == -1:
        text = "Blue's"
        color=(0,0,255)
    else:
        text = "Gender Fluid Player's"
        color=(150,150,150)
    font=pygame.font.SysFont("arial",60)
    screen.blit(font.render(text+" Turn",True,color),(0,0))
def blit_alpha(target, source, location, opacity):
    x = location[0]
    y = location[1]
    temp = pygame.Surface((source.get_width(), source.get_height())).convert()
    temp.blit(target, (-x, -y))
    temp.blit(source, (0, 0))
    temp.set_alpha(opacity)        
    target.blit(temp, location)
#places all pieces on board
def standard_piece_placement():
    pieces=[]
    for i in range(8):
        pieces.append(pawn((i,1)))
        pieces.append(pawn((i,6)))
    pieces.append(king((3,0)))
    pieces.append(king((3,7)))
    pieces.append(queen((4,0)))
    pieces.append(queen((4,7)))
    pieces.append(knight((1,7)))
    pieces.append(knight((6,7)))
    pieces.append(knight((1,0)))
    pieces.append(knight((6,0)))
    pieces.append(rook((0,0)))
    pieces.append(rook((7,0)))
    pieces.append(rook((0,7)))
    pieces.append(rook((7,7)))
    pieces.append(bishop((5,7)))
    pieces.append(bishop((2,7)))
    pieces.append(bishop((5,0)))
    pieces.append(bishop((2,0)))
    return pieces
def run():
    #</functions>
    #<variables>
    background_color = (0,123,123)
    clock = pygame.time.Clock()
    time_passed = 0
    fps = 60
    #</variables>
    #<per program variables>
    chess=chess_world(standard_piece_placement(),screen)
    selected_piece = None
    player=1
    #</per program variables>
    #<main loop>
    while True:
        #<event handling>
        for event in pygame.event.get():
            if event.type == KEYDOWN:
                #<exit>
                if event.key == K_ESCAPE:
                    quit_game()
                    return True
                #</exit>
            if event.type==MOUSEBUTTONDOWN:
                if selected_piece:
                    #move piece
                    if chess.move_piece(selected_piece):
                        checkmate = chess.check_checkmate(-1*selected_piece.team)
                        player=-player
                        #check if players still have kings
                        end = chess.check_game_end()
                        if end!= 0:
                            #clear screen
                            screen.fill((0,123,123))
                            screen.blit(chess.board.image,chess.board.pos)
                            chess.draw_pieces()
                            end_game(end)
                            return True
                        if checkmate:
                            #clear screen
                            screen.fill((0,123,123))
                            screen.blit(chess.board.image,chess.board.pos)
                            chess.draw_pieces()
                            end_game(selected_piece.team)
                            return True 
                    #replace pawn with queen if reach opponent side
                    if selected_piece.name=="pawn" and (selected_piece.pos[1]==0 or selected_piece.pos[1]==7):
                        p=queen(selected_piece.pos,team=selected_piece.team)
                        p.correct_size((chess.board.square_size,chess.board.square_size))
                        chess.pieces[selected_piece.pos]=p
                    selected_piece=None
                elif pygame.mouse.get_pressed()[0]:
                    #select clicked piece
                    selected_piece=chess.select_piece()
        if selected_piece:
            if selected_piece.team!=player:
                selected_piece=None
        #</event handling>
        #<draw to screen>
        screen.fill((0,123,123))
        screen.blit(chess.board.image,chess.board.pos)
        draw_turn_text(player)
        if selected_piece:
            #draw square on selected piece
            chess.board.show_selected()
            if selected_piece:
                #draw possible moves of selected piece
                chess.show_moves(selected_piece)
        chess.draw_pieces()
        #</draw to screen>
        #<display update>
        pygame.display.update()
        fps = clock.get_fps()
        time_passed = clock.tick(fps)
        #</display update>
    #</main loop>
if __name__=='__main__':
    from chess_world.chess_world import chess_world
    from chess_world.chess_pieces import *
    run()
else:
    from .chess_world.chess_world import chess_world
    from .chess_world.chess_pieces import *

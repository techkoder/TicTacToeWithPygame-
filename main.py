#importing modules
import pygame,tkinter
from tkinter import *
from tkinter import Tk, messagebox

# initializing pygame
pg = pygame
pg.init()

x_hint = pg.image.load('img/x_hint.png')
o_hint = pg.image.load('img/o_hint.png')
x = pg.image.load('img/x.png')
o = pg.image.load('img/o.png')


# creatinng the screen
d = pg.display
s = d.set_mode((900,750))
clock = pg.time.Clock()
d.set_caption("Best TIC-TAC-TOE")

# colours for pygame
black = (0,0,0)
white = (255,255,255)
red = (255,0,0)
green = (0,255,0)
blue = (0,0,255)
yellow = (255,255,0)
neon = (0,255,255)
pink = (255,0,255)

# creating the list of board
board = [' ' for i in range(10)]

music = pg.mixer.music.load("sound\game_sound.mp3")

def spaceisfree(pos):
    if board [pos] == ' ':
        return True

def insertletter(pos,letter):
    if spaceisfree(pos):
        board[pos] = letter
    
def iswinner(bo,le):
    if bo[1] == le and bo[2] == le and bo[3] == le or bo[4] == le and bo[5] == le and bo[6] == le or bo[7] == le and bo [8] == le and bo[9] == le or bo[1] == le and bo[4] == le and bo[7] == le or bo[2] == le and bo[5] == le and bo[8] == le or bo[3] == le and bo[6] == le and bo[9] == le or bo[1] == le and bo[5] == le and bo[9] == le or bo[3] == le and bo[5] == le and bo[7] == le:
        return True
    else:
        return False
    
def isboardfull():
    if board.count(' ') <= 1:
        return True
    else:
        return False

#creating the buttons
class button():
    def __init__(self,x,y,width,height,colour):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.colour = colour
    def draw(self):
        pg.draw.rect(s,self.colour,(self.x,self.y,self.width,self.height))
    def isover(self,pos):
        if pos[0] > self.x and pos[0] < self.x + self.width:
            if pos[1] > self.y and pos[1] < self.y + self.height:
                return True

button1 = button(150,75,200,200,white)
button2 = button(350,75,200,200,white)
button3 = button(550,75,200,200,black)
button4 = button(150,275,200,200,black)
button5 = button(350,275,200,200,black)
button6 = button(550,275,200,200,black)
button7 = button(150,475,200,200,black)
button8 = button(350,475,200,200,black)
button9 = button(550,475,200,200,black)

def hint_x(pos):
    if button1.isover(pos):
        if board[1] == ' ':
            s.blit(x_hint,(button1.x+5,button1.y+5))
    if button2.isover(pos):
        if board[2] == ' ':
            s.blit(x_hint,(button2.x+5,button2.y+5))
    if button3.isover(pos):
        if board[3] == ' ':
            s.blit(x_hint,(button3.x+5,button3.y+5))
    if button4.isover(pos):
        if board[4] == ' ':
            s.blit(x_hint,(button4.x+5,button4.y+5))
    if button5.isover(pos):
        if board[5] == ' ':
            s.blit(x_hint,(button5.x+5,button5.y+5))
    if button6.isover(pos):
        if board[6] == ' ':
            s.blit(x_hint,(button6.x+5,button6.y+5))
    if button7.isover(pos):
        if board[7] == ' ':
            s.blit(x_hint,(button7.x+5,button7.y+5))
    if button8.isover(pos):
        if board[8] == ' ':
            s.blit(x_hint,(button8.x+5,button8.y+5))
    if button9.isover(pos):
        if board[9] == ' ':
            s.blit(x_hint,(button9.x+5,button9.y+5))

def hint_o(pos):
    if button1.isover(pos):
        if board[1] == ' ':
            s.blit(o_hint,(button1.x+5,button1.y+5))
    if button2.isover(pos):
        if board[2] == ' ':
            s.blit(o_hint,(button2.x+5,button2.y+5))
    if button3.isover(pos):
        if board[3] == ' ':
            s.blit(o_hint,(button3.x+5,button3.y+5))
    if button4.isover(pos):
        if board[4] == ' ':
            s.blit(o_hint,(button4.x+5,button4.y+5))
    if button5.isover(pos):
        if board[5] == ' ':
            s.blit(o_hint,(button5.x+5,button5.y+5))
    if button6.isover(pos):
        if board[6] == ' ':
            s.blit(o_hint,(button6.x+5,button6.y+5))
    if button7.isover(pos):
        if board[7] == ' ':
            s.blit(o_hint,(button7.x+5,button7.y+5))
    if button8.isover(pos):
        if board[8] == ' ':
            s.blit(o_hint,(button8.x+5,button8.y+5))
    if button9.isover(pos):
        if board[9] == ' ':
            s.blit(o_hint,(button9.x+5,button9.y+5))

def checkboard():
    if board[1] == 'x':
        s.blit(x,(button1.x+5,button1.y+5))
    if board[2] == 'x':
        s.blit(x,(button2.x+5,button2.y+5))
    if board[3] == 'x':
        s.blit(x,(button3.x+5,button3.y+5))
    if board[4] == 'x':
        s.blit(x,(button4.x+5,button4.y+5))
    if board[5] == 'x':
        s.blit(x,(button5.x+5,button5.y+5))
    if board[6] == 'x':
        s.blit(x,(button6.x+5,button6.y+5))
    if board[7] == 'x':
        s.blit(x,(button7.x+5,button7.y+5))
    if board[8] == 'x':
        s.blit(x,(button8.x+5,button8.y+5))
    if board[9] == 'x':
        s.blit(x,(button9.x+5,button9.y+5))
    if board[1] == 'o':
        s.blit(o,(button1.x+5,button1.y+5))
    if board[2] == 'o':
        s.blit(o,(button2.x+5,button2.y+5))
    if board[3] == 'o':
        s.blit(o,(button3.x+5,button3.y+5))
    if board[4] == 'o':
        s.blit(o,(button4.x+5,button4.y+5))
    if board[5] == 'o':
        s.blit(o,(button5.x+5,button5.y+5))
    if board[6] == 'o':
        s.blit(o,(button6.x+5,button6.y+5))
    if board[7] == 'o':
        s.blit(o,(button7.x+5,button7.y+5))
    if board[8] == 'o':
        s.blit(o,(button8.x+5,button8.y+5))
    if board[9] == 'o':
        s.blit(o,(button9.x+5,button9.y+5))

# funtion to draw the board  
def draw_board():
    s.fill(white)
    pg.draw.line(s,blue,(350,75),(350,675),5)
    pg.draw.line(s,green,(550,75),(550,675),5)
    pg.draw.line(s,red,(150,275),(750,275),5)
    pg.draw.line(s,red,(150,475),(750,475),5)

# funtion to display messagebox
def messagebox(text,description = "Game over"):
    window = Tk()
    window.eval('tk::PlaceWindow %s center' % window.winfo_toplevel())
    window.withdraw()
    if tkinter.messagebox.askyesno(description,text) == True:
        return True
    else:
        return False
    window.deiconify()
    window.destroy()
    window.quit()

def reset_board():
    global board
    board = [' ' for i in range(10)]

#game loop
def main():
    pg.mixer.music.play(-1)
    run = True
    move = 'x'
    while run:
        if not isboardfull():
            pos = pg.mouse.get_pos()
            if move == 'x':
                if not iswinner(board,'o'):
                    hint_x(pos)
                    for event in pg.event.get():
                        if event.type == pg.QUIT:
                            pg.quit
                            run = False
                        if event.type == pg.MOUSEBUTTONDOWN:
                            if button1.isover(pos):
                                insertletter(1,'x')
                                move = 'o'
                            if button2.isover(pos):
                                insertletter(2,'x')
                                move = 'o'
                            if button3.isover(pos):
                                insertletter(3,'x')
                                move = 'o'
                            if button4.isover(pos):
                                insertletter(4,'x')
                                move = 'o'
                            if button5.isover(pos):
                                insertletter(5,'x')
                                move = 'o'
                            if button6.isover(pos):
                                insertletter(6,'x')
                                move = 'o'
                            if button7.isover(pos):
                                insertletter(7,'x')
                                move = 'o'
                            if button8.isover(pos):
                                insertletter(8,'x')
                                move = 'o'
                            if button9.isover(pos):
                                insertletter(9,'x')
                                move = 'o'
                    pg.display.update()
                else:
                    if messagebox('o has won the game, do you want to play again') == True:
                        reset_board()
                    else:
                        run = False
            else:
                if not iswinner(board,'x'):
                    hint_o(pos)
                    for event in pg.event.get():
                        if event.type == pg.QUIT:
                            pg.quit()
                            run = False
                        if event.type == pg.MOUSEBUTTONDOWN:
                            if button1.isover(pos):
                                insertletter(1,'o')
                                move = 'x'
                            if button2.isover(pos):
                                insertletter(2,'o')
                                move = 'x'
                            if button3.isover(pos):
                                insertletter(3,'o')
                                move = 'x'
                            if button4.isover(pos):
                                insertletter(4,'o')
                                move = 'x'
                            if button5.isover(pos):
                                insertletter(5,'o')
                                move = 'x'
                            if button6.isover(pos):
                                insertletter(6,'o')
                                move = 'x'
                            if button7.isover(pos):
                                insertletter(7,'o')
                                move = 'x'
                            if button8.isover(pos):
                                insertletter(8,'o')
                                move = 'x'
                            if button9.isover(pos):
                                insertletter(9,'o')
                                move = 'x'
                    pg.display.update()
                else:
                    if messagebox('X has won the game, do you want to play again') == True:
                        reset_board()
                        move = 'x'
                    else:
                        run = False
            draw_board()
            checkboard()
            clock.tick(60)
            d.update()
        else:
            if not iswinner(board,'x'):            
                if not iswinner(board,'o'):
                    print("board is full")
                    if messagebox('The board is full,do you want too play again?') == True:
                        reset_board()
                        move = 'x'
                    else:
                        run = False
                else:
                    if messagebox('o has won the game,do you want to play again') == True:
                        reset_board()
                        move = 'x'
                    else:
                        run = False
            else:
                if messagebox('x has won the game,do you want to playagain') == True:
                    reset_board()
                    move = 'x'
                else:
                    run = False

main()

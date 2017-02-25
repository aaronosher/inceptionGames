from appJar import gui
import pygame
import sys

gui = gui("Inception Games", "600x800")

class GameMenu():
    def __init__(self, screen, items, bg_color=(0,0,0), font=None, font_size=30,
                    font_color=(255, 255, 255)):
        self.screen = screen
        self.scr_width = self.screen.get_rect().width
        self.scr_height = self.screen.get_rect().height
 
        self.bg_color = bg_color
        self.clock = pygame.time.Clock()
 
        self.items = items
        self.font = pygame.font.SysFont(font, font_size)
        self.font_color = font_color
 
        self.items = []
        for index, item in enumerate(items):
            label = self.font.render(item, 1, font_color)
 
            width = label.get_rect().width
            height = label.get_rect().height
 
            posx = (self.scr_width / 2) - (width / 2)
            # t_h: total height of text block
            t_h = len(items) * height
            posy = (self.scr_height / 2) - (t_h / 2) + (index * height)
 
            self.items.append([item, label, (width, height), (posx, posy)])
 
    def run(self):
        mainloop = True
        while mainloop:
            # Limit frame speed to 50 FPS
            self.clock.tick(50)
 
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    mainloop = False
 
            # Redraw the background
            self.screen.fill(self.bg_color)
 
            for name, label, (width, height), (posx, posy) in self.items:
                self.screen.blit(label, (posx, posy))
 
            pygame.display.flip()
 
 
if __name__ == "__main__":
    # Creating the screen
    screen = pygame.display.set_mode((640, 480), 0, 32)
 
    menu_items = ('Start', 'Quit')
 
    pygame.display.set_caption('Game Menu')
    gm = GameMenu(screen, menu_items)
    gm.run()
    
    
def draw(x,y):
    im = Image.open("o.png")
    im = im.convert("L")
    print (im)
    
    
def findbox(x,y):
    one=[1,2,3]
    two=[4,5,6]
    three=[7,8,9]
    i=(x // 98)+1 #row of x(1-9)
    j=(y // 98)+1 #row of y(1-9)
    if i in one:
        bigrow=1
    elif i in two:
        bigrow=2
    elif i in three:
        bigrow=3
    if j in one:
        bigcol=1
    elif j in two:
        bigcol=2
    elif j in three:
        bigcol=3
    if i%3!=0:
        tinyrow=i%3
    else:
        tinyrow=3
    if j%3!=0:
        tinycol=j%3
    else:
        tinycol=3
      
    return {(bigcol, bigrow): (tinycol, tinyrow)}

def joinGame(param):
    print(param)

def createGame(param):
    print(param)

def buttonPush(param):
    print(param)
    
def board():    
    pygame.init()
    DISPLAYSURF = pygame.display.set_mode((900, 900))
    pygame.display.set_caption('Hello World!')
    DISPLAYSURF.fill((33,124,126))
    
    pygame.draw.rect(DISPLAYSURF,(51,51,51),(100,0,2,900))
    pygame.draw.rect(DISPLAYSURF,(51,51,51),(200,0,2,900))
    pygame.draw.rect(DISPLAYSURF,(51,51,51),(400,0,2,900))
    pygame.draw.rect(DISPLAYSURF,(51,51,51),(500,0,2,900))
    pygame.draw.rect(DISPLAYSURF,(51,51,51),(700,0,2,900))
    pygame.draw.rect(DISPLAYSURF,(51,51,51),(800,0,2,900))
    pygame.draw.rect(DISPLAYSURF,(51,51,51),(0,100,900,2))
    pygame.draw.rect(DISPLAYSURF,(51,51,51),(0,200,900,2))
    pygame.draw.rect(DISPLAYSURF,(51,51,51),(0,400,900,2))
    pygame.draw.rect(DISPLAYSURF,(51,51,51),(0,500,900,2))
    pygame.draw.rect(DISPLAYSURF,(51,51,51),(0,700,900,2))
    pygame.draw.rect(DISPLAYSURF,(51,51,51),(0,800,900,2))
    pygame.draw.rect(DISPLAYSURF,(0,0,0), (300, 0, 3, 900))
    pygame.draw.rect(DISPLAYSURF,(0,0,0), (600, 0, 3, 900))
    pygame.draw.rect(DISPLAYSURF,(0,0,0), (0,300,900,3))
    pygame.draw.rect(DISPLAYSURF,(0,0,0),(0,600,900,3))
    mainloop=True
    while mainloop:
        for event in pygame.event.get():
            if event.type==pygame.QUIT:
                mainloop=False
            elif event.type == pygame.MOUSEBUTTONUP:
                print("mouse up")
                mousex, mousey = event.pos
                print(findbox(mousex, mousey))
                
                
        pygame.display.update()

def viewInit():
    board()
    #global gui
    # gui.setIcon("./resources/imagesTic-tac-toe.gif")
    #gui.addLabel("welcomeText", "Welcome to Incpetion Games", 0, 0, 2)
    #gui.addMenuList("Game", ["Create Game", "Join Game"])
    #gui.go()
    

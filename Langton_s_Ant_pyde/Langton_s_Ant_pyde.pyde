pix=0

class Node():
    def __init__(self,pix,x,y,clr=0):
        self.pix=pix
        self.x=x*pix
        self.y=y*pix
        self.clr=clr
        self.refresh()
        
    def refresh(self):
        fill(self.clr)
        rect(self.x,self.y,self.pix,self.pix)
    
Grid=list()
antx=0
anty=0
dir=0
up = (0,-1)
right = (1,0)
down = (0,1)
left = (-1,0)

def moveForward():
    global up,down,right,left,antx,anty
    if(dir==up):
        antx+=up[0]
        anty+=up[1]
    elif(dir==right):
        antx+=right[0]
        anty+=right[1]
    elif(dir==down):
        antx+=down[0]
        anty+=down[1]
    elif(dir==left):
        antx+=left[0]
        anty+=left[1]

def turnRight():
    global dir
    if(dir==up):
        dir=right
    elif(dir==right):
        dir=down
    elif(dir==down):
        dir=left
    elif(dir==left):
        dir=up

def turnLeft():
    global dir
    if(dir==right):
        dir=up
    elif(dir==down):
        dir=right
    elif(dir==left):
        dir=down
    elif(dir==up):
        dir=left                    
    
def flip():
    global Grid
    if(Grid[antx][anty]==0):
        Grid[antx][anty]=1
    else:
        Grid[antx][anty]=0    
                                                    

def setup():
    global dir
    global antx
    global anty
    global Grid
    global pix
    size(800,800)
    pix=10
    x=80
    y=80
    Grid=[[Node(pix,i,j,color(0)) for i in range(y)] for j in range(x)]
    #print(Grid)
    antx=40
    anty=40
    dir=up
    #print(Grid)
    pixelDensity(1)
    
def draw():
    global antx
    global anty
    global Grid
    global dir
    for i in range(100):
        antx=antx%(width/(pix))
        anty=anty%(height/(pix))
    
        if(Grid[antx][anty].clr==color(0)):
            turnRight()
            Grid[antx][anty].clr=color(255)
            Grid[antx][anty].refresh()
        else:
            turnLeft()
            Grid[antx][anty].clr=color(0)
            Grid[antx][anty].refresh()
        moveForward()
    # for i in range(width):
    #     for j in range(height):
    #         pix = i + width * j
    #         if(Grid[i][j]==0):
    #             pixels[pix] = color(255)
    #         else:    
    #             pixels[pix] = color(0)            

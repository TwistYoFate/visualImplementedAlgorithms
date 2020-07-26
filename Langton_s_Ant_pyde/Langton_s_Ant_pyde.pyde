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
    size(800,800)
    Grid=[[ 0 for i in range(width)] for j in range(height)]
    #print(Grid)
    antx=400
    anty=400
    dir=up
    #print(Grid)
    pixelDensity(1)
    
def draw():
    global antx
    global anty
    global Grid
    global dir
    loadPixels()
    for i in range(100):
        antx=antx%width
        anty=anty%height
    
        if(Grid[antx][anty]==0):
            turnRight()
        else:
            turnLeft()
        flip()
        moveForward()
    for i in range(width):
        for j in range(height):
            pix = i + width * j
            if(Grid[i][j]==0):
                pixels[pix] = color(255)
            else:    
                pixels[pix] = color(0)            
    updatePixels()

Grid=[]
pix=0

class Node():
    def __init__(self,pix,x,y,clr=0):
        self.pix=pix
        self.x=x*pix
        self.y=y*pix
        self.clr=clr
        self.refresh()
        
    def refresh(self):
        rect(self.x,self.y,self.pix,self.pix)

                
def setup():
    global Grid,pix
    pix=10
    x=40
    y=40
    size(400,400)
    Grid=[[Node(pix,i,j,color(0)) for i in range(y)] for j in range(x)]
    
def draw():
    for h in range(40):
        for w in range(40):
            Grid[h][w].refresh()
                
                    

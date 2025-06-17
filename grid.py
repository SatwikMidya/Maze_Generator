import numpy as np
import cv2 as cv
import math

blanck=np.zeros((500,500,3),dtype='uint8')    #creates the blanck screen to grid
grid=[]


class Cell:
    def __init__(self,x,y,w):

        self.x=x              
        self.y=y
        self.w=w
        self.cell=[True,True,True,True]
        self.visited = False
        self.index= 0 
    
    def draw(self,canvas):

        x=self.x
        y=self.y
        w=self.w
        if(self.cell[0]):
            cv.line(canvas,(x*w,y*w),((x+1)*w,y*w),(255,255,255),2)
        if(self.cell[1]):
            cv.line(canvas,(x*w,y*w),(x*w,(y+1)*w),(255,255,255),2)
        if(self.cell[2]):
            cv.line(canvas,(x*w,(y+1)*w),((x+1)*w,(y+1)*w),(255,255,255),2)
        if(self.cell[3]):
            cv.line(canvas,((x+1)*w,y*w),((x+1)*w,(y+1)*w),(255,255,255),2)
    

    
    def checkneighbours(self):
        x=self.x
        y=self.y
        w=self.w
        row=math.floor(500/w)
        col=math.floor(500/w)

        neighbour = []

        if y > 0 :
            top=grid[x+((y-1)*col)]
            neighbour.append(top)
        if x > 0 :
            left=grid[(x-1)+(y*col)]
            neighbour.append(left)
        if y < row-1 :
            bottom = grid[x+((y+1)*col)]
            neighbour.append(bottom)
        if x < col-1 :
            right = grid[(x+1)+(y*col)]
            neighbour.append(right)
    
        return neighbour

    
                
    

    def mark(self):
        x=self.x
        y=self.y
        w=self.w
        cv.rectangle(blanck,(x*w,y*w),((x+1)*w,(y+1)*w),(0,255,0),2)
    
    def markblue(self):
        x=self.x
        y=self.y
        w=self.w
        cv.rectangle(blanck,(x*w,y*w),((x+1)*w,(y+1)*w),(0,0,255),2) 
    
        
        
        
            

def setup(w):
   
    col=math.floor(500/w)
    row=math.floor(500/w)

    for y in range(row):          
        for x in range(col):      
            c=Cell(x,y,w)
            c.index = x + y * col
            grid.append(c)
            # print(c.index)
    



def drawGrid():
    setup(50)
    for cell in grid:
        cell.draw(blanck)
        # print(cell.index)



def createmaze(row , col):
    
    row , col = row, col
    index = row + col*10
    current = grid[index]
    current.visited = True
    current.mark()
    neighbours = current.checkneighbours()
    for neighbour in neighbours:
        print(neighbour.index)
        neighbour.markblue()
        
    
    







drawGrid()
createmaze(0,0)
# test = grid[2]
# test.mark()

cv.imshow('grid',blanck)
cv.waitKey(0)

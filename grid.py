import numpy as np
import cv2 as cv
import math
import random

blanck=np.zeros((500,500,3),dtype='uint8')
maze=np.zeros((500,500,3),dtype='uint8')    #creates the blanck screen to grid
grid=[]


class Cell:
    def __init__(self,x,y,w):

        self.x=x              
        self.y=y
        self.w=w
        self.cell=[True,True,True,True]
        self.visited = False
        self.index= 0 
        self.Nneighbour=[0,0,0,0]
    
    def draw(self,canvas):

        x=self.x
        y=self.y
        w=self.w
        if(self.cell[0]):
            cv.line(canvas,(x*w,y*w),((x+1)*w,y*w),(255,255,255),3)
        if(self.cell[1]):
            cv.line(canvas,(x*w,y*w),(x*w,(y+1)*w),(255,255,255),3)
        if(self.cell[2]):
            cv.line(canvas,(x*w,(y+1)*w),((x+1)*w,(y+1)*w),(255,255,255),3)
        if(self.cell[3]):
            cv.line(canvas,((x+1)*w,y*w),((x+1)*w,(y+1)*w),(255,255,255),3)

        if not self.cell[0]:
            cv.line(canvas,(x*w,y*w),((x+1)*w,y*w),(0,0,0),3)
        if not self.cell[1]:
            cv.line(canvas,(x*w,y*w),(x*w,(y+1)*w),(0,0,0),3)
        if not self.cell[2]:
            cv.line(canvas,(x*w,(y+1)*w),((x+1)*w,(y+1)*w),(0,0,0),3)
        if not self.cell[3]:
            cv.line(canvas,((x+1)*w,y*w),((x+1)*w,(y+1)*w),(0,0,0),3)
    

    
    def checkneighbours(self):
        x=self.x
        y=self.y
        w=self.w
        row=math.floor(500/w)
        col=math.floor(500/w)

        neighbour = []

        if y > 0 :
            top=grid[x+((y-1)*col)]
            if(top.visited == False):
                neighbour.append(top)
        if x > 0 :
            left=grid[(x-1)+(y*col)]
            if(left.visited==False):
                neighbour.append(left)
        if y < row-1 :
            bottom = grid[x+((y+1)*col)]
            if(bottom.visited==False):
               neighbour.append(bottom)
        if x < col-1 :
            right = grid[(x+1)+(y*col)]
            if(right.visited==False):
                neighbour.append(right)
    
        return neighbour
    
    def removeWall(self,current):
        dx=self.x-current.x
        dy=self.y-current.y

        if(dx==1):
            current.cell[3]=False
            self.cell[1]=False
        if(dx==-1):
            current.cell[1]=False
            self.cell[3]=False
        if(dy==1):
            current.cell[2]=False
            self.cell[0]=False
        if(dy==-1):
            current.cell[0]=False
            self.cell[2]=False
            
    
    



    
                
    

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



def createmaze(cell):
    
    current = cell
    current.visited = True
    # current.mark()
    neighbours = current.checkneighbours()
    random.shuffle(neighbours)
    for neighbour in neighbours:
        # print(neighbour.index)
        # neighbour.markblue()
        if not neighbour.visited:
            neighbour.removeWall(current)
            current.draw(blanck)
            neighbour.draw(blanck)
            cv.imshow('grid',blanck)
            # cv.imshow('maze',maze)
            cv.waitKey(60)
            createmaze(neighbour)


        
    
    







drawGrid()
# setup(50)
cell=grid[55]
cell.markblue()
createmaze(cell)
for cell in grid:
        cell.draw(maze)







cv.imshow('maze final', maze)
cv.waitKey(0)


# test = grid[2]
# test.mark()


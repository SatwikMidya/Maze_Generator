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
        w = self.w
        col = math.floor(500/w)
        top = self.index - col
        left = self.index -1
        bottom = self.index + col
        right = self.index +1
        neighbours = [top,left,bottom,right]
        return neighbours

    
        
        
        
            

def setup(w):
   
    col=math.floor(500/w)
    row=math.floor(500/w)

    for i in range(row):
        for j in range(col):
            c=Cell(i,j,w)
            c.index = i + j * col
            grid.append(c)


def drawGrid():
    setup(50)
    for cell in grid:
        cell.draw(blanck)



def createmaze(row , col):
    
    row , col = row, col
    current = Cell(row,col)
    current.visited = True
    
    







drawGrid()

cv.imshow('grid',blanck)
cv.waitKey(0)

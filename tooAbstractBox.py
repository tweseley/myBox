from sketch import *


class Box(Sketch):
    def __init__(self, width, depth, height):
        self.depth = depth
        self.width = width
        self.height = height 
        self.back = Side(['cut','cut','dashed','cut'],(self.height,0),(self.height+self.width,self.height))
        self.bottom = Side([None,'dashed','dashed','dashed'],(self.height,self.height),(self.height+self.width,self.height+self.depth))
        self.front = Side([None,'cut','dashed','cut'],(self.height,self.height+self.depth),(self.height+self.width,2*self.height+self.depth))
        self.top = Side([None,'cut','cut','cut'],(self.height,2*self.height+self.depth),(self.height+self.width,2*self.height+2*self.depth))
        self.left = Side(['cut',None,'cut','cut'],(0,self.height),(self.height,self.height+self.depth))
        self.right = Side(['cut','cut','cut',None],(self.height+self.width,self.height),(2*self.height+self.width,self.height+self.depth))

class Side(Sketch):
    def __init__(self, sides, start, end):
        self.start = start #top left corner
        self.end = end #bottom right corner
        #sides is a list containing description of what kind of line each side of the square is
        #order: topH, vertR, bottomH, vertL
        self.lineList = SimpleLineList()
        cutLine = MetaLine('TwoPoints',(SimpleLine,),{'operation':'cut'})
        dashedLine = MetaLine('TwoPoints',(SimpleLine,),{'operation':'dash'})
        def lineType(line):
            if line == "dashed":
                self.lineList.append(dashedLine().set(start=start,end=end))
            elif line == "cut":
                self.lineList.append(cutLine().set(start=start,end=end))
        for i in range(len(sides)):
            if i == 0:
                start=self.start
                end = (self.end[0],self.start[1])
                lineType(sides[i])
            elif i == 1:
                start = (self.end[0],self.start[1])
                end = (self.end[0],self.end[1])
                lineType(sides[i])
            elif i == 2:
                start = (self.end[0],self.end[1])
                end = (self.start[0],self.end[1])
                lineType(sides[i])
            elif i==3:
                start=self.start
                end = (self.start[0],self.end[1])
                lineType(sides[i])

        

        
if __name__ == '__main__':
	a = Box(50,75,100)
	a.render('abstractBox.svg',root=True)

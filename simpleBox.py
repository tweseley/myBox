from sketch import *


class Box(Sketch):
    def __init__(self, width, depth, height):
        
        self.lineList = SimpleLineList()
        cutLine = MetaLine('TwoPoints',(SimpleLine,),{'operation':'cut'})
        dashedLine = MetaLine('TwoPoints',(SimpleLine,),{'operation':'dash'})


        #back
        self.lineList.append(cutLine().set(start=(height,0),end=(height+width,0)))
        self.lineList.append(cutLine().set(start=(height,0),end=(height,height)))
        self.lineList.append(cutLine().set(start=(height+width,height),end=(height+width,0)))
        self.lineList.append(dashedLine().set(start=(height+width,height),end=(height,height)))

        #bottom
        self.lineList.append(dashedLine().set(start=(height,height),end=(height,height+depth)))
        self.lineList.append(dashedLine().set(start=(height+width,height+depth),end=(height+width,height)))
        self.lineList.append(dashedLine().set(start=(height+width,height+depth),end=(height,height+depth)))

        #front
        self.lineList.append(cutLine().set(start=(height,height+depth),end=(height,2*height+depth)))
        self.lineList.append(dashedLine().set(start=(height+width,2*height+depth),end=(height,2*height+depth)))
        self.lineList.append(cutLine().set(start=(height+width,2*height+depth),end=(height+width,height+depth)))

        #top
        self.lineList.append(cutLine().set(start=(height,2*height+depth),end=(height,2*height+2*depth)))
        self.lineList.append(cutLine().set(start=(height+width,2*depth+2*height),end=(height,2*height+2*depth)))
        self.lineList.append(cutLine().set(start=(height+width,2*depth+2*height),end=(height+width,2*height+depth)))

        #right
        self.lineList.append(cutLine().set(start=(height+width,height),end=(width+2*height,height)))
        self.lineList.append(cutLine().set(start=(width+2*height,height+depth),end=(width+height,height+depth)))
        self.lineList.append(cutLine().set(start=(width+2*height,height+depth),end=(width+2*height,height)))

        #left
        self.lineList.append(cutLine().set(start=(0,height),end=(height,height)))
        self.lineList.append(cutLine().set(start=(0,height),end=(0,height+depth)))
        self.lineList.append(cutLine().set(start=(0,height+depth),end=(height,height+depth)))
        

if __name__ == '__main__':
	a = Box(50,75,100)
	a.render('Box.svg',root=True)

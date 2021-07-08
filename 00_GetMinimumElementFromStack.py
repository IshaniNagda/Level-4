class stack:
    def __init__(self):
        self.s=[]
        self.minEle=None

    def push(self,x):
        self.s.append(x)

    def pop(self):
        if len(self.s)!=0:
            lastelement=self.s[-1]
            del(self.s[-1])
            return lastelement
        else:
            return -1
        

    def getMin(self):
        if len(self.s)!=0:
            self.minEle= min(self.s)
            return self.minEle
            
        else:
            return -1

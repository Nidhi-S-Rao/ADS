#Design Directed Graph class with minimum of 6 edges. 
#Write functions to retrieveminimum and maximum cost edges from constructed graph. 
#While returning min / max cost, provided the edge names also.
class Graph:
    class vertex:
        def __init__(self,ele):
            self.id=ele
            self.neighbours={}
        def addEdge(self,to,wt=0):
            if to not in self.neighbours:
                self.neighbours[to]=wt
        def getNeighbours(self):
            return self.neighbours.keys()
        def getCost(self):
            return self.neighbours.values()
    def __init__(self):
        self.count=0
        self.adjacencyList={}
    def addVertex(self,item):
        if item not in self.adjacencyList:
            node=self.vertex(item)
            self.adjacencyList[item]=node
            self.count+=1
    def addEdge(self,fro,to,wt):
        if fro not in self.adjacencyList:
            self.addVertex(fro)
        if to not in self.adjacencyList:
            self.addVertex(to)
        self.adjacencyList[fro].addEdge(to,wt)
    def getEdge(self):
        min=999999
        max=0
        min_edge=''
        max_edge=''
        for k in self.adjacencyList.keys():
            item=self.adjacencyList[k]
            for m in item.neighbours:
                if(item.neighbours[m]>max):
                    max=item.neighbours[m]
                    max_edge=item.id+'-'+m
                if(item.neighbours[m]<min):
                    min=item.neighbours[m]
                    min_edge=item.id+'-'+m
        print("Minimum cost:",min)
        print("Maximum cost:",max)
        print("Minimum cost edge:",min_edge)
        print("Maximum cost edge:",max_edge)
        

            


g=Graph()
g.addVertex('a')
g.addEdge('a','b',8)
g.addEdge('a','c',5)
g.addEdge('b','e',2)
g.addEdge('c','d',4)
g.addEdge('d','e',2)
g.addEdge('e','g',9)
g.addEdge('e','f',1)
g.addEdge('g','f',10)
g.getEdge()


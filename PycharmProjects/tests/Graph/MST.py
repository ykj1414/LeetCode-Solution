#加权无向图边的类型，为每条边做单独的数据结构和方法。
# 比直接在邻接表用数组做可读性和扩展性更强。
import sys
sys.path.append('../UnionFind')
from Union import Union

class Edge(object):
    def __init__(self,u,v,w):
        #u代表一个顶点，v代表另一个顶点，w代表权重，默认以u为主顶点
        self.__u = u
        self.__v = v
        self.__w = w

    def weight(self):
        return self.__w

    def either(self):
        return self.__u

    def other(self,p):
        if p==self.__u:
            return self.__v
        elif p==self.__v:
            return self.__u
        else:
            return None

    def compareTo(self,edge):
        if edge.weight()>self.__w:
            return -1
        elif edge.weight()<self.__w:
            return 1
        else:
            return 0

    def toString(self):
        return str(self.u)+"-"+str(self.v)+str(self.w)

class EdgeWeightedGraph(object):

    def __init__(self,v,input):
        self.__v = v
        self.__adj = [[] for i in range(v)]
        self.__e = 0
        self.__addEdge(input)


    def __addEdge(self,input):
        for i in input:
            cur = Edge(i[0],i[1],i[2])
            self.addEdge(cur)

    def addEdge(self,edge):
        u = edge.either()
        v = edge.other(u)
        self.__adj[u].append(edge)
        self.__adj[v].append(edge)

    def iterable(self,v):
        return self.__adj[v]

    def edges(self):
        return self.__adj

    def V(self):
        return self.__v

    def E(self):
        return self.__e

#延时Prim最小生成树算法，先遍历完顶点的所有边，再做删除和选择操作
class LazyPrimMST(object):

    def __init__(self, EWGraph):
        self.__MinPQ = []
        self.__marked = [0]*EWGraph.V()
        self.__mst = []
        self.__visit(0,EWGraph)
        while(self.__MinPQ):
            cedge = self.__MinPQ.pop(-1)
            u = cedge.either()
            v = cedge.other(u)
            if self.__marked[u] and self.__marked[v]:
                continue
            else:
                self.__mst.append(cedge)
                if self.__marked[u]:
                    self.__visit(v,EWGraph)
                else:
                    self.__visit(u,EWGraph)

    def __visit(self,v,EWGraph):
        self.__marked[v] = 1
        for i in EWGraph.iterable(v):
            if not self.__marked[i.other(v)]:
                self.__MinPQ.append(i)
        self.__MinPQ=sorted(self.__MinPQ,key = lambda x:x.weight(),reverse=True)
        # for i in self.__MinPQ:
        #     print(i.either(),i.other(i.either()),i.weight())


    def edges(self):
        return self.__mst

    def weight(self):
        return 0

#非延迟的Prim算法，在遍历顶点的所有边时，直接筛选出最小边
#书上的代码让人看了很迷惑，我选择了自己的实现方式，
class PrimMST(object):

    def __init__(self,EWGraph):
        self.__MinPQ = []
        self.__marked = [0]*EWGraph.V()
        self.__distto = [None]*EWGraph.V()  #保留下每个顶点出发的最短路径
        self.__edgeto = [None]*EWGraph.V()  #最小边
        self.__visit(0,EWGraph)
        while self.__MinPQ:
            cur = self.__MinPQ.pop(0)
            self.__visit(cur,EWGraph)

    def __visit(self,u,EWGraph):
        elist = EWGraph.iterable(u)
        self.__marked[u] = 1
        for i in elist:
            v = i.other(u)
            if self.__distto[v]==None or self.__distto[v]>i.weight():
                if self.__marked[v] and self.__edgeto[u] == v:
                    continue
                self.__distto[v] = i.weight()
                self.__edgeto[v] = u
                if v in self.__MinPQ:
                    continue
                self.__MinPQ.append(v)
    def edges(self):
        return (self.__edgeto,self.__distto)



#KruskalMST算法，与Prim算法不同，他利用到了森林的思想，
# 通过将不同的两块最小生成树不断合并，最后生成整个图的最小生成树
# 其中用到的数据结构是第一章使用的Union，
# 通过Union来判断，两个节点是否已经属于一个生成树
class KruskalMST(object):
    def __init__(self,EWGraph):
        self.__mst = []
        self.__MinPQ = []
        self.__uf = Union(EWGraph.V())
        elist = EWGraph.edges()
        for i in elist:
            for j in i:
                self.__MinPQ.append(j)
        self.__MinPQ = sorted(self.__MinPQ,key = lambda x:x.weight(),reverse=True)
        while self.__MinPQ and len(self.__mst)<EWGraph.V()-1:
            cur = self.__MinPQ.pop(-1)
            u = cur.either()
            v = cur.other(u)
            if(self.__uf.connected(u,v)):
                continue
            self.__mst.append(cur)
            self.__uf.quick_union(u,v)

    def edges(self):
        return self.__mst

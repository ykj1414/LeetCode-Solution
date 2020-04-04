#最短路径的实现，这里主要实现的是加权有向图的最短路径，而非普通有向图的最短路径。
#加权无向图的最短路径称为最小生成树

class DirectedEdge(object):
    def __init__(self,u,v,w):
        self.__u = u    #起点
        self.__v = v    #重点
        self.__w = w    #权重


    def from_p(self):
        return self.__u

    def to_p(self):
        return self.__v

    def weight(self):
        return self.__w


class EdgeWeightDigraph(object):
    def __init__(self,v,input):
        self.__v = v
        self.__e = len(input)
        self.__adj = [[] for i in range(self.__v)]
        self.__addadj(input)

    def V(self):
        return self.__v

    def E(self):
        return self.__e

    def addedge(self,directedEdge):
        self.__adj[directedEdge.from_p()].append(directedEdge)

    def __addadj(self,input):
        for i in input:
            cur = DirectedEdge(i[0],i[1],i[2])
            self.addedge(cur)

    def edges(self,u):
        return self.__adj[u]

    def adjs(self):
        return self.__adj


#DijkstraSP 算法，核心思想类似加权无向图的最小生成树算法
#最关键的递推公式就是dist[w] <=dist[v]+e.weight(),其中e是v到w的边.
class DijkstraSP(object):
    def __init__(self,EdgeWeightedDigraph,s):
        self.__s = s
        self.__edgeto = [None]*EdgeWeightedDigraph.V()
        self.__dist = [float("inf")]*EdgeWeightedDigraph.V()
        self.__dist[s] = 0
        self.__indexMinPQ = [[s,0]]
        while self.__indexMinPQ:
            cur = min(self.__indexMinPQ,key = lambda x:x[1])
            self.__indexMinPQ.remove(cur)
            self.__relax(EdgeWeightedDigraph,cur[0])


    #松弛操作，一旦发现s经由v到w的路径比原来s到w的路线更短，替换路线
    def __relax(self,EdgeWeightedDigraph,v):
        for i in EdgeWeightedDigraph.edges(v):
            w = i.to_p()
            if self.__dist[w]>self.__dist[v]+i.weight():
                self.__dist[w] = self.__dist[v]+i.weight()
                self.__edgeto[w] = i
                if w not in self.__indexMinPQ:
                    self.__indexMinPQ.append([w,self.__dist[w]])

    def haspathto(self,p):
        return self.__dist[p]<float("inf")
        pass

    def pathto(self,p):
        path = []
        if not self.haspathto(p):
            return path
        e = self.__edgeto[p]
        while e:
            path.insert(0,e)
            e = self.__edgeto[e.from_p()]
        return path
        pass

    def distTo(self,p):
        return self.__dist[p]
        pass

    # 利用拓扑排序实现有向加权无环图的最短路径,同理可以做最长路径
    # 如果是有环图，使用拓扑排序的这个算法会陷入死循环。
    # top参数控制先拓扑排序，再进行松弛，还是直接松弛，在松弛的过程中使用拓扑排序


# 利用拓扑排序完成的最短路径算法
class AcycilicSP(object):
    def __init__(self,EdgeWeightedDigraph,s,top = True):
        self.__v = EdgeWeightedDigraph.V()
        self.__e = EdgeWeightedDigraph.E()
        self.__edgeto = [None]*self.__v
        self.__distto = [float("inf")]*self.__v
        self.__distto[s] = 0
        self.__top = []
        self.__marked = [0]*self.__v
        if top:
            self.__topological(s,EdgeWeightedDigraph)
            for i in self.__top:
                self.__relax(EdgeWeightedDigraph,i)
        else:
            self.__relax(EdgeWeightedDigraph,s,False)

    # 采用拓扑排序，逆后序就是拓扑排序顺序
    def __topological(self,s,EdgeWeightedDigraph):
        self.__marked[s] = 1
        for i in EdgeWeightedDigraph.edges(s):
            if not self.__marked[i.to_p()]:
                self.__topological(i.to_p(),EdgeWeightedDigraph)
        self.__top.insert(0,s)

    # 松弛操作，如果disttp[w]>distto[v]+e.weight() 那么当前distto[w]作废
    def __relax(self,EdgeWeightedDigraph,s,topplogical=True):
        for i in EdgeWeightedDigraph.edges(s):
            w = i.to_p()
            if i.weight()+self.__distto[s]<self.__distto[w]:
                self.__distto[w] = i.weight()+self.__distto[s]
                self.__edgeto[w] = i
            if not topplogical:
                self.__relax(EdgeWeightedDigraph,w,topplogical)


    def haspathto(self,p):
        return self.__distto[p]<float("inf")

    def pathto(self,p):
        if not self.haspathto(p):
            return []
        path = []
        e = self.__edgeto[p]
        while e:
            path.insert(0,e)
            e = self.__edgeto[e.from_p()]
        return path

    def paths(self):
        return self.__edgeto

    def distto(self,p):
        return self.__distto[p]


#检测加权有向图中是否存在环
class EdgeWeightDiCycle(object):
    def __init__(self,EdgeWeightedDiGraph,s):
        self.__v = EdgeWeightedDiGraph.V()
        self.__edgeto = [None]*self.__v
        self.__mark = [0]*self.__v
        self.__stack = [0]*self.__v
        self.__cycle = []

    def __dfs(self,EdgeWeightedDiGraph,s):
        self.__mark[s] = 1
        self.__stack[s] = 1
        for i in EdgeWeightedDiGraph.edges(s):
            u = i.to_p()
            if self.__cycle:
                return
            elif not self.__mark[u]:
                self.__mark[u] = 1
                self.__dfs(EdgeWeightedDiGraph,u)
            elif self.__stack[u]:
                self.__cycle = []
                f = i
                while f.from_p()!=s:
                    self.__cycle.append(f)
                    f = f.from_p()
                self.__cycle.append(f)
                return
        self.__stack[u] = 0


class BellmanFordSP(object):
    def __init__(self,EdgeWeightDiGraph,s):
        self.__v = EdgeWeightDiGraph.V()
        self.__e = EdgeWeightDiGraph.E()
        self.__edgeto = [None]*self.__v
        self.__distto = [float("inf")]*self.__v
        self.__distto[s] = 0
        self.__mark = [0]*self.__v
        self.__mark[s] = 1
        self.__pq = [s]
        while self.__pq:
            self.__relax(self.__pq.pop(0),EdgeWeightDiGraph)


    def __relax(self,s,EdgeWeightedGraph):
        for i in EdgeWeightedGraph.edges(s):
            u = i.to_p()
            if self.__distto[u]>i.weight()+self.__distto[s]:
                self.__edgeto[u] = i
                self.__distto[u] = i.weight()+self.__distto[s]
                if not self.__mark[u]:
                    self.__pq.append(u)
                    self.__mark[u] = 1


    def haspathto(self,p):
        return self.__distto[p]<float("inf")

    def paths(self):
        return self.__edgeto

    def distto(self,p):
        return self.__distto[p]

    def pathto(self,p):
        if not self.haspathto(p):
            return []
        path = []
        e = self.__edgeto[p]
        while e:
            path.insert(0,e)
            e = self.__edgeto[e.from_p()]
        return path
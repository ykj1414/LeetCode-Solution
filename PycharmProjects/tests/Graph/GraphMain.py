from Graph import Graph
from Search import Search
from DGraph import DGraph
from MST import LazyPrimMST,EdgeWeightedGraph,PrimMST,KruskalMST
from SP import EdgeWeightDigraph,DijkstraSP,AcycilicSP,BellmanFordSP
import time
if __name__=="__main__":
    # a = open("../Data/tinyG.txt",'r')
    # content = a.readlines()
    # a.close()
    # v,e = int(content[0]),int(content[1])
    # elist = []
    # for i in range(2,len(content)):
    #     a = content[i].split(" ")
    #     elist.append([int(i) for i in a])
    # a = DGraph(v,elist)
    # print(a.adj)
    # b = Search(a,0)
    # c = 5
    # print(b.hasPathto(c,False))
    # print(b.hasPathto(c))
    a = open('../Data/tinyEWDAG.txt','r')
    content = a.readlines()
    a.close()
    v,e = int(content[0]),int(content[1])
    elist = []
    for i in range(2,len(content)):
        a = content[i].replace("\n","").split(" ")
        elist.append([int(a[0]),int(a[1]),float(a[2])])
    ewgraph = EdgeWeightedGraph(v,elist)
    test = EdgeWeightDigraph(v,elist)
    # 加权有向无环图的拓扑排序实现最小(长）路径
    since = time.time()
    a = AcycilicSP(test,5,True)
    b = BellmanFordSP(test,5)
    for k in range(test.V()):
        path_a = a.pathto(k)
        path_b = b.pathto(k)
        print("a:",a.distto(k))
        for i in path_a:
            print(i.from_p(),i.to_p(),i.weight())

        print("b:",b.distto(k))
        for i in path_b:
            print(i.from_p(),i.to_p(),i.weight())
    print(time.time()-since)
    # 普通加权有向无环图的最小路径排序
    # a = DijkstraSP(test,0)
    # path = a.pathto(6)
    # print(a.distTo(6))
    # for i in path:
    #     print(i.from_p(),i.to_p(),i.weight())
    # lmst = LazyPrimMST(ewgraph)
    # mst = PrimMST(ewgraph)
    # lmstlist = lmst.edges()
    # kmst = KruskalMST(ewgraph)
    # mst = mst.edges()
    # mstedges,mstdist= mst[0],mst[1]
    # for i in lmstlist:
    #     print(i.either(),i.other(i.either()),i.weight())
    # print()
    # for i in kmst.edges():
    #     print(i.either(), i.other(i.either()), i.weight())
    # for i in range(len(mstdist)):
    #     print(i, mstedges[i], mstdist[i])
    # print(mst.edges())

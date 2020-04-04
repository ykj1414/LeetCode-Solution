#图的表示方法大概有三种，邻接矩阵，边的数组，以及邻接表数组
#前两种表示法都有缺陷，所以常用邻接表数组,简称邻接表


class Graph(object):
    def __init__(self,v,elist):
        self.V = v
        self.adj = [[] for i in range(v)] #创造空邻接表
        self.__adjGraph(elist)

    # 和v相邻的所有顶点,塞入邻接表
    def __adjGraph(self, elist):
        for i in elist:
            self.addEdge(i[0],i[1])
        pass

    #python不支持多个构造函数，可以使用元祖输入，分别判断
    # def __E(self,In):
    #     if not In:
    #         return []
    #     return In
    #
    # def __V(self,In):
    #     if type(In)!=int:
    #         self.V = len(In)
    #     return In

    #添加v-w边函数
    def addEdge(self,v,w):
        self.adj[v].append(w)
        self.adj[w].append(v)
        pass

    #图的邻接表的字符串表示
    def toString(self):
        s = str(self.V)+" vertices, "+str(self.E)+" edges.\n"
        for i in range(self.V):
            s+=str(i)+" :"
            for j in self.adj(i):
                s+=str(j)+" "
            s+='\n'
        return s
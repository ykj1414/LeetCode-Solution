from Graph import Graph

class Search(object):

    def __init__(self,graph,s):
        self.graph = graph
        self.s = s

    def hasPathto(self,v,bfs=True):
        return self.__marked(v,bfs)
    #顶点v是否和s联通
    def __marked(self,v,bfs=True):
        if not bfs:
            path = [0]*self.graph.V
            path[self.s] = 1
            return self.__dfs(path,1,self.s,v)
        else:
            path = [self.s]
            ways = [0]*self.graph.V
            ways[self.s] = 1
            return self.__bfs(path,ways,v)
        pass

    #深度优先遍历寻找路径
    def __dfs(self,path,step,w,v):
        if step >= self.graph.V:
            return False
        if v in self.graph.adj[w]:
            return True
        for i in self.graph.adj[w]:
            if not path[i]:
                path[i] = 1
                if self.__dfs(path,step + 1, i,v):
                    return True
                path[i] = 0
        return False

    #利用bfs寻找路径
    def __bfs(self,path,ways,v):
        if not path:
            return False
        while path:
            cur = path.pop(0)
            for i in self.graph.adj[cur]:
                if i==v:
                    return True
                if ways[i]:
                    continue
                ways[i] = 1
                path.append(i)
        return False
        pass
    #与s联通的总数
    def count(self):
        pass
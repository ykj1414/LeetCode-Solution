#正则表达式的实现，通过非确定有限状态自动机NFA实现
#本质依旧是使用到了有向图算法！非确定有限状态自动机本质上就是构建了一个有向图的邻接表
class DGraph(object):
    def __init__(self,M):
        self.adj = {i:[] for i in range(M)}
        self.__mark = {}

    def addedge(self,s,v):
        self.adj[s].append(v)


class DFS(object):
    def __init__(self,graph,mp):
        self.mark = {i:0 for i in graph.adj}
        for s in mp:
            self.__dfs(graph,s)
    def __dfs(self,graph,s):
        self.mark[s] = 1
        for i in graph.adj[s]:
            if not self.mark[i]:
                self.__dfs(graph,i)

class NFA(object):

    def __init__(self,regexp):
        self.re = regexp
        self.M = len(regexp)
        self.__g = DGraph(self.M+1)
        stack = []
        for i in range(self.M):
            #注意lp的作用，lp是为了记录*号之前出现的字符，或者左括号的位置
            #如果是A*，那么lp的下标就是*的下标-1
            #如果是（AB)*或者（A|B)*，那么lp的下标就是左括号，
            # 意思是*的状态可以转移回lp处
            lp=i
            if regexp[i]=='(' or regexp[i]=='|':
                stack.append(i)
            elif regexp[i]==')':
                c_or = stack.pop(-1)
                if regexp[c_or]=='|':
                    lp=stack.pop(-1)
                    self.__g.addedge(lp,c_or+1)
                    self.__g.addedge(c_or,i)
                else:
                    lp = c_or
            if regexp[i]=='(' or regexp[i]=='*' or regexp[i]==')':
                self.__g.addedge(i,i+1)
            if i+1<self.M and regexp[i+1]=='*':
                self.__g.addedge(lp,i+1)
                self.__g.addedge(i+1,lp)
            # elif regexp[i]=='|':
            #     continue
            # else:
            #     self.__g.addedge(i,i+1)

        pass

    def recognizes(self,in_txt):
        pc = []
        dfs = DFS(self.__g,[0])
        for i in self.__g.adj:
            if dfs.mark[i]:
                pc.append(i)
        for i in range(len(in_txt)):
            match = []
            while pc:
                v = pc.pop(-1)
                if v<self.M:
                    if self.re[v] == in_txt[i] or in_txt[i] =='.':
                        match.append(v+1)
            dfs = DFS(self.__g,match)
            for index in self.__g.adj:
                if dfs.mark[index]:
                    pc.append(index)
        for v in pc:
            if v==self.M:
                return True
        return False

    def edges(self):
        return self.__g.adj
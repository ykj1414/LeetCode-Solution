#Union-Find 算法的API

class Union(object):
    def __init__(self,n): #初始化N个触点
        self.total = n
        self.points = [i for i in range(n)]
        self.size = [1]*n


        pass
    def quick_union(self,p,q): #在p,q点之间添加连线
        #这段本质上是实现了用父链接的形式表示了一篇森林，具体参考算法橙书第四版P142页
        # pid = self.find(p)
        # qid = self.find(q)
        # if pid==qid:
        #     return
        # self.points[pid] = qid
        # self.total-=1
        #改进版本的加权quick_union算法，利用size数组记录每个根节点的树的深度
        #永远保证小树挂载在大树上，大大降低了最坏情况下的查找时间
        pid = self.find(p)
        qid = self.find(q)
        if pid == qid:
            return
        if self.size[pid]>self.size[qid]:
            self.points[qid] = pid
            self.size[pid]+=self.size[qid]
        else:
            self.points[pid] = qid
            self.size[qid]+=self.size[pid]
        self.total-=1
        pass

    def find(self,p):#p(0到N-1)所在的分量的标识符
        while(p!=self.points[p]):
            p = self.points[p]
        return p
        pass

    def connected(self,p,q):#如果p,q属于同一个标识符(集合）则返回true
        return self.find(p)==self.find(q)
        pass

    def count(self):#连通分量的数量

        return self.total
        pass

if __name__ =="__main__":
    a = open('../Data/mediumUF.txt', 'r')
    contents = a.readlines()
    a.close()
    uf = Union(int(contents[0]))
    for i in range(1,len(contents)):
        cache = contents[i].split(' ')
        p = int(cache[0])
        q = int(cache[1])
        if(uf.connected(p,q)):
            continue
        else:
            uf.quick_union(p,q)
        print(p,q)
    # print(uf.points)
    print(uf.count())
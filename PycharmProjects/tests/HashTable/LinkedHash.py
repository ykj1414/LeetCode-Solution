#基于拉链法的散列表实现
class LinkedHash(object):
    #拉链法中散列表节点
    class Node(object):
        def __init__(self,key=None,val=None):
            self.key = key
            self.val = val
            self.next = None

    def __init__(self,N=10,M=997):
        self.N = N      #键值对总数
        self.M = M      #默认散列表长度
        self.count = 0  #键值对计数
        self.kvs = [None for i in range(self.M)]

    def put(self,key,value):
        hashkey = self.__hash(key)
        x = self.Node(key,value)
        if self.kvs[hashkey]:
            x.next = self.kvs[hashkey]
        self.kvs[hashkey] = x
        self.count+=1

    def get(self,key):
        key = self.__hash(key)
        x = self.kvs[key]
        while x:
            if x.key==key:
                return x.val
            x = x.next
        else:
            return None

    def delete(self,key):
        hashkey = self.__hash(key)
        x = self.kvs[hashkey]
        pre = self.Node()
        pre.next = x
        while x:
            if x.key==key:
                pre.next = x.next
                del(x)
                self.count-=1
                break
            x = x.next
        else:
            return None
        if not pre.key and not pre.val:
            self.kvs[key] = pre.next

    def __hash(self,key):
        return hash(key)%self.M

    def iterate(self):
        for i in range(self.M):
            x = self.kvs[i]
            while x:
                print(x.key,x.val)
                x = x.next
    pass
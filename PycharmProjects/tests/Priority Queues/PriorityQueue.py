# 利用二叉堆实现优先队列

class MaxPQ(object):
    def __init__(self,maxN=1,nums=[]):
        if nums:
            self.nlist = [0]+nums
            self.length = len(nums)
        else:
            self.nlist = [0]*(maxN+1)
            self.length = 0
        pass

    def heapSort(self):
        self.length
        k = self.length//2
        while k>=1:
            self.__sink(k)
            k-=1
        while self.length>1:
            self.__exch(1,self.length)
            self.length-=1
            self.__sink(1)
    # 私有化比较操作，可以通过添加函数实现更多类型的比较。
    def __less(self,i,j):
        return self.nlist[i]<self.nlist[j]

    # 私有化交换数据函数
    def __exch(self,i,j):
        self.nlist[i],self.nlist[j] = self.nlist[j],self.nlist[i]

    #二叉堆的下沉操作，如果父节点小于子节点的值，就不断下沉
    def __sink(self,k):
        while 2*k<=self.length:
            j = 2*k
            # 每个父节点有两个子节点，要选取更大的子节点值进行比较
            if j<self.length and self.__less(j,j+1):
                j+=1
            if not self.__less(k,j):
                break
            self.__exch(k,j)
            k = j

    # 二叉堆的上浮操作，如果子节点数值大于父节点，就不断上浮
    def __swim(self,k):
        while k<self.length and self.__less(k,k//2):
            self.__exch(k//2,k)
            k*=2

    def insert(self,value):
        self.length+=1
        self.nlist[self.length] = value
        self.__swim(self.length)
        pass

    def max_value(self):
        return self.nlist[1]
        pass

    def delMax(self):
        if self.length<1:
            return
        self.__exch(1,self.length)
        self.length-=1
        self.nlist[self.length+1] = None
        self.__sink(1)
        pass

    def isEmpty(self):
        return self.length==1
        pass

    def size(self):
        return self.length-1
        pass

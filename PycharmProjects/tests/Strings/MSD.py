#高位优先的字符串排序方法
class MSD(object):

    #M代表分割小数组的切换阈值
    def __init__(self,M=0):
        self.__R = 256
        self.__M = M

    def __insert(self,lo,hi,d,input):
        #插入排序，注意下标，算法书上的写法会导致越界
        for i in range(lo,hi):
            j = i+1
            while j>=lo and input[j][d:]<input[j-1][d:]:
                input[j],input[j-1] = input[j-1],input[j]
                j-=1

        pass

    def sort(self,input):
        N = len(input)
        def help(lo,hi,d):
            # 在高位字符串排序中，将小数组切换到插入排序时必须的。
            # 因为每次递归都会生成一个count[258]大小的索引计数数组，如果切割范围非常小，
            # 那么这种代价是相较于排序本身将会非常高昂
            if hi<=lo:
                return
            if hi<=lo+self.__M and d>0:
                self.__insert(lo,hi,d,input)
                return
            aux = [None]*(hi-lo+1)
            #由于高位字符串排序需要根据结尾字符判断大小，
            # 当前缀相同的字符串排序时，长度更短的字符视为更小，此时需要将'\0'结束符统计用于排序
            # 这样的话不同于低位字符串排序，高位字符串排序需要记录结束符出现的次数来进行短字符串的排序
            # 为了方便计算，把所有下标都往右移2位，并将结束符返回的缩印置为-1,这样就保证了所有字符的正确统计
            # 同时在计算偏移时没有改动，因为\0的优先级最高，所以依旧是count[r+1]+=count[r]
            count = [0]*(self.__R+2)
            for j in range(lo,hi+1):
                index = -1
                if d<len(input[j]):
                    index = ord(input[j][d])
                count[index+2]+=1
            for r in range(self.__R+1):
                count[r+1]+=count[r]
            for i in range(hi-lo+1):
                index = -1
                if d <len(input[i+lo]):
                    index = ord(input[i+lo][d])
                aux[count[index+1]]= input[i+lo]
                count[index+1]+=1
            for i in range(lo,hi+1):
                input[i] = aux[i-lo]
            for r in range(self.__R):
                help(lo+count[r],lo+count[r+1]-1,d+1)
        help(0,N-1,0)
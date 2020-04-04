#可以参考排序算法中的三向快速排序，对于有个大量重复值的情况，效果非常好。

class Quick3Sort(object):
    def sort(self,input):
        def help(lo,hi,d):
            if hi<=lo:
                return
            ls,lm,le = lo,lo+1,hi
            v  = self.__charAt(input[lo],d)
            while lm<=le:
                t = self.__charAt(input[lm],d)
                if t>v:
                    input[le],input[lm] = input[lm],input[le]
                    le-=1
                elif t<v:
                    input[lm],input[ls] = input[ls],input[lm]
                    ls+=1
                    lm+=1
                else:
                    lm+=1
            help(lo,ls-1,d)
            if v>=0:
                help(ls,le,d+1)
            help(le+1,hi,d)
        help(0,len(input)-1,0)



    def __charAt(self,instr,d):
        if d>=len(instr):
            return -1
        return ord(instr[d])
        pass
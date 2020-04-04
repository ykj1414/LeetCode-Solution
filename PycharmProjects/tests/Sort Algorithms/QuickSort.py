# 原始版本的快排算法
def quickSort(nlist):
    def help(left,right):
        if left>=right:
            return
        mid = left
        start,end = left,right
        while start<end:
            while end>=mid and nlist[mid]<=nlist[end]:
                end-=1
            if end<mid:
                break;
            nlist[end],nlist[mid] = nlist[mid],nlist[end]
            mid = end
            while start<=mid and nlist[mid]>=nlist[start]:
                start+=1
            if start>mid:
                break;
            nlist[start],nlist[mid] = nlist[mid],nlist[start]
            mid = start
        help(left,mid-1)
        help(mid+1,right)
    help(0,len(nlist)-1)

# 三向切分的快速排序,在有大量重复元素的时候，比原始快排效率高得多，比较重要！！！
def quick3Sort(nlist):
    def help(left,right):
        if left>=right:
            return
        ls,lm,le = left,left+1,right
        cmp = nlist[left]
        while lm<=le:
            if nlist[lm]<cmp:
                nlist[ls],nlist[lm] = nlist[lm],nlist[ls]
                ls+=1
                lm+=1
            elif nlist[lm]>cmp:
                nlist[le],nlist[lm] = nlist[lm],nlist[le]
                le-=1
            else:
                lm+=1
        help(left,ls-1)
        # 对于数字来说 ls-le之间的值都一样无需再排序
        # help(ls,le)
        help(le+1,right)
    help(0,len(nlist)-1)
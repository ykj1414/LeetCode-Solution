# 自顶向下的归并排序，由原始数组不断切割到小数组
def mergeSort1(nlist):
    nlen = len(nlist)
    def help(left,right):
        if left>=right:
            return
        mid = left+(right-left)//2
        i,j = left,mid+1
        help(left, mid)
        help(mid + 1, right)
        cur = []
        for k in range(right-left+1):
            if i>mid:
                cur.append(nlist[j])
                j+=1
            elif j>right:
                cur.append(nlist[i])
                i+=1
            elif nlist[i]>=nlist[j]:
                cur.append(nlist[j])
                j+=1
            elif nlist[i]<nlist[j]:
                cur.append(nlist[i])
                i+=1
        nlist[left:right+1] = cur
    help(0,nlen-1)

# 自底向上的归并排序，先从微笑数组开始排序，不断还原成最后的大数组,非常适合链表排序，
# 在链表排序时，使用插入排序，就可以实现链表的原地归并排序。
def mergeSort2(nlist):
    def help(left,mid,right):
        if left>=right:
            return
        i,j = left,mid+1
        cur = []
        for k in range(right-left+1):
            if i>mid:
                cur.append(nlist[j])
                j+=1
            elif j>right:
                cur.append(nlist[i])
                i+=1
            elif nlist[i]>=nlist[j]:
                cur.append(nlist[j])
                j+=1
            elif nlist[i]<nlist[j]:
                cur.append(nlist[i])
                i+=1
        nlist[left:right+1] = cur
    nlen = len(nlist)
    i = 1
    while i<nlen:
        j = 0
        while j<nlen:
            mid = j+i-1 if j+i<nlen else nlen-1
            help(j,mid,j+i-1+i if nlen-1>=j+i+i else nlen-1)
            j+=i+i
        i+=i
def insertSort(nlist):
    nlen = len(nlist)
    for i in range(nlen):
        j = 0
        for j in range(i):
            if nlist[j]>nlist[i]:
                break;
        cur = nlist[i]
        for k in range(j,i+1):
            nlist[k],cur = cur,nlist[k]

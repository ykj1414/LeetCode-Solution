def selectSort(nlist):
    nlen = len(nlist)
    for i in range(nlen):
        for j in range(i,nlen):
            if nlist[i]>=nlist[j]:
                nlist[i],nlist[j] = nlist[j],nlist[i]
                pass
            pass
        pass
    pass

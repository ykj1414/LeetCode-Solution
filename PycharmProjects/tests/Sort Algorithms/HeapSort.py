def heapSort(nlist):
    nlen = len(nlist)
    n = nlen
    def sink(k):
        while 2*k<nlen:
            j = 2*k+1
            if j<n-1 and nlist[j]<nlist[j+1]:
                j+=1
            if j>=n-1 or nlist[j]<nlist[k]:
                break
            nlist[k],nlist[j] = nlist[j],nlist[k]
            k = j
    k = nlen//2-1
    while k>=0:
        sink(k)
        k-=1
    print(nlist)
    while n>0:
        nlist[0],nlist[n-1] = nlist[n-1],nlist[0]
        n -= 1
        sink(0)
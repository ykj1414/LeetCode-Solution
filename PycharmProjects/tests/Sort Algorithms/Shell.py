def shellSort(nlist):
    nlen = len(nlist)
    h = 0
    def help(step):
        s = 0
        while s<step:
            i = s
            while i<nlen:
                j = i
                while j>=s:
                    if nlist[j]>=nlist[i]:
                        j-=step
                        continue
                    else:
                        j+=step
                        break
                else:
                    j = s
                k = j
                cur = nlist[i]
                while k<=i:
                    nlist[k],cur = cur,nlist[k]
                    k+=step
                i+=step
            s+=1
            pass

    while h<nlen//3:
        h = h*3+1
    while h>=1:
        help(h)
        h = h//3
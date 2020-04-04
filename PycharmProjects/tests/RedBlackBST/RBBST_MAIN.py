from RBBST import RedBlackBST



if __name__ =='__main__':
    a = RedBlackBST('S',0)
    # a.put('E', 1)
    # a.put('A', 2)
    # a.put('R', 3)
    # a.put('C', 4)
    # a.put('H', 5)
    # a.put('M', 6)
    # a.put('X', 7)
    # a.put('M', 8)
    # a.put('P', 9)
    # a.put('L', 10)
    # a.RBprint()
    bstr = 'ACEHLMPRSX'
    for i in bstr:
        a.put(i)
    a.delete('M')
    a.RBprint()
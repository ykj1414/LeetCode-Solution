#单词搜索树,也称前缀字典树

class trieST(object):
    class __Node(object):
        def __init__(self,R,value=None,isActive=False):
            self.val = value
            self.next = [None for i in range(R)]
    def __init__(self,R=256):
        self.R = R
        self.__root = self.__Node(R,None,True)

    def keys(self):
        p = []
        self.__collect(self.__root,'',p)
        return p

    #通配符字符串匹配的写法
    def keysThatMatch(self,pat):
        p = []
        self.__collectpat(self.__root,'',pat,p)
        return p

    def __collectpat(self,node,key,pat,p):
        if not node:
            return
        d = len(key)
        if d==len(pat) and node.val!=None:
            p.append(key)
        if d==len(pat):
            return
        index = ord(pat[d])
        for c in range(self.R):
            if pat[d]=='.' or index==c:
                self.__collectpat(node.next[c],key+chr(c),pat,p)


    def __collect(self,node,key,p):
        if not node:
            return
        for i in range(self.R):
            if node.next[i]:
                if node.next[i].val:
                    p.append(key + chr(i))
                self.__collect(node.next[i], key + chr(i),p)

    def longestPrefixOf(self,s):
        end = self.__search(self.__root,s,0,0)
        return s[:end]

    def __search(self,node,s,d,length):
        if not node:
            return length
        if node.val:
            length = d
        if d==len(s):
            return length
        index = ord(s[d])
        return self.__search(node.next[index],s,d+1,length)


    def delete(self,key):
        self.__delete(self.__root,key,0)
    def __delete(self,node,key,d):
        if not node:
            return None
        if d==len(key):
            node.val = None
        else:
            index = ord(key[d])
            node.next[index] = self.__delete(node.next[index],key,d+1)
        if node.val:
            return node
        for i in node.next:
            if i:
                return node
        return None

    def get(self,key):
        # print(self.__root.next)
        x = self.__get(self.__root,key,0)
        return x.val if x!=None else None

    def __get(self,node,key,d):
        if node ==None:
            return None
        if d==len(key):
            return node
        index = ord(key[d])
        cur = node.next[index]
        return self.__get(cur,key,d+1)

    def put(self,key,val):
        self.__root = self.__put(self.__root,key,val,0)
        pass

    def __put(self,node,key,val,d):
        if not node:
            node = self.__Node(self.R)
        if d==len(key):
            node.val = val
            return node
        index = ord(key[d])
        node.next[index] = self.__put(node.next[index],key,val,d+1)
        return node
    pass



#三向查找树，所需内存远低于一般的字典树
class TST(object):
    class __Node(object):
       def __init__(self,c,val):
           self.c = c
           self.val = val
           self.left = None
           self.right = None
           self.mid = None

    def __init__(self):
        self.__root = None

    def put(self,key,value):
        self.__root = self.__put(self.__root,key,value,0)
        pass

    def __put(self,node,key,value,d):
        if d == len(key):
            return None
        if not node:
            node = self.__Node(key[d],None)
        if d == len(key)-1:
            node.val = value
        if node.c==key[d]:
            node.mid = self.__put(node.mid,key,value,d+1)
        elif node.c<key[d]:
            node.right = self.__put(node.right,key,value,d+1)
        else:
            node.left = self.__put(node.left,key,value,d+1)
        return node
        pass

    def get(self,key):
        node = self.__get(self.__root,key,0)
        return node.val if node else None
        pass

    def __get(self,node,key,d):
        if not node:
            return None
        if d==len(key)-1:
            return node
        if node.c<key[d]:
            return self.__get(node.right,key,d)
        elif node.c>key[d]:
            return self.__get(node.left,key,d)
        else:
            return self.__get(node.mid,key,d+1)
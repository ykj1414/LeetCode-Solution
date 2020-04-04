#二叉搜索树 非常重要的一种数据结构，尤其中间的删除，插入操作值得反复思考学习。

class BST(object):
    class Node(object):
        def __init__(self,key,val):
            self.key = key
            self.val = val
            self.count = 1
            self.left = None
            self.right = None

    def __init__(self,key=None,val=None):
        if key:
            self.head = self.Node(key,val)
        else:
            self.head = None

    def getVal(self,key):
        cur = self.head
        while cur:
            if cur.key == key:
                return cur.val
            elif cur.key<key:
                cur = cur.right
            else:
                cur = cur.left
        return None

    def size(self):
        return self.__s_size(self.head)

    def __s_size(self,root):
        if not root:
            return 0
        else:
            return root.count

    def put(self,key,val=None):
        def help_put(root,key,val):
            if not root:
                return self.Node(key,val)
            if root.key<key:
                root.right=help_put(root.right,key,val)
            elif root.key>key:
                root.left=help_put(root.left,key,val)
            else:
                root.val = val
            root.count = self.__s_size(root.left)+self.__s_size(root.right)+1
            return root
        self.head = help_put(self.head,key,val)

    def deleteMin(self):
        self.head= self.__deleteMin(self.head)

    def __deleteMin(self,root):
        if not root.left:
            return root.right
        root.left = self.__deleteMin(root.left)
        root.count = self.__s_size(root.left)+self.__s_size(root.right)+1
        return root
    def Min(self):
        return self.__Min(self.head)

    def __Min(self,root):
        if not root.left:
            return root
        else:
            return self.__Min(root.left)

    def delete(self,key):
        self.head = self.__delete(self.head,key)

    def __delete(self,root,key):
        if not root:
            return None
        if root.key>key:
            root.left = self.__delete(root.left,key)
        elif root.key<key:
            root.right = self.__delete(root.right,key)
        else:
            if not root.left:
                return root.right
            elif not root.right:
                return root.left
            else:
                cur = root
                root = self.__Min(root.right)
                root.right = self.__deleteMin(cur.right)
                root.left = cur.left
        root.count = self.__s_size(root.left)+self.__s_size(root.right)+1
        return root


    # 搜索二叉树范围查找操作
    def findKeys(self,key1,key2):
        result = []
        self.__findKeys(self.head,key1,key2,result)
        return result

    def __findKeys(self,root,key1,key2,result):
        if not root:
            return
        if root.key>key1:
            self.__findKeys(root.left,key1,key2,result)
        if root.key <= key2 and root.key >= key1:
            result.append(root.key)
        if root.key<key2:
            self.__findKeys(root.right,key1,key2,result)

    #搜索二叉树中序遍历的非递归版本
    def bstmidprint(self):
        def help(root):
            nums = []
            while nums or root:
                if root:
                    nums.append(root)
                    root = root.left
                else:
                    root = nums.pop()
                    print(root.key,root.val)
                    root = root.right
        help(self.head)

    #搜索二叉树按层次遍历的非递归版本
    def bstprint(self):
        def help(root):
            nums = [root]
            while nums:
                cur = nums.pop(0)
                print(cur.key,cur.val)
                if cur.left:
                    nums.append(cur.left)
                if cur.right:
                    nums.append(cur.right)
        help(self.head)


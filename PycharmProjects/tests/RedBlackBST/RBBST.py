#红黑树的插入，查找，删除的实现
#其中插入和删除操作用到的红黑链接变换非常重要，需要反复推敲经常复习

class RedBlackBST(object):
    class __Node(object):
        def __init__(self,key,value=None,isRed=False):
            self.key = key
            self.val = value
            self.isRed = isRed
            self.left = None
            self.right = None
            self.count = 1

    def __init__(self,key,value = None):
        self.root = self.__Node(key,value)

    #get 方法和普通二叉搜索树没有区别
    def get(self,key):
        def help(root,key):
            if not root:
                return None
            if root.key<key:
                return help(root.right,key)
            elif root.key>key:
                return help(root.left,key)
            else:
                return root.val
        help(self.root,key)
    # 插入和二叉搜索树区别很大，需要考虑2-节点和3-节点的插入情况
    # 总共6种情况，每种情况都需要谨慎使用左旋转，右旋转和颜色变换操作

    #需要进行旋转操作和颜色变换操作的有三种情况，对应两种节点，一共6种情况
    # 1.左链接黑，右链接红，左旋转
    # 2.左链接红，左子链接红，右旋转
    # 3.左右链接都红，说明有一个3-节点退化成2个2-节点，颜色变换

    def put(self,key,value=None):
        def help(root,key,value):
            if not root:
                return self.__Node(key,value,True)
            elif root.key<key:
                root.right = help(root.right,key,value)
            elif root.key>key:
                root.left = help(root.left,key,value)
            else:
                root.val = value
            #判断旋转和颜色变换操作
            x = root
            if self.__color(root.left) and self.__color(root.right):
                    self.__flipColors(root)
            if self.__color(root.left) and self.__color(root.left.left):
                    x = self.__rotateright(root)
            if self.__color(root.right) and not self.__color(root.left):
                    x = self.__rotateleft(root)
            x.count = self.__size(x.left)+self.__size(x.right)+1
            return x
        self.root = help(self.root,key,value)
        self.root.isRed = False

    def color(self):
        return 'RED' if self.__color(self.root) else 'BLACK'

    def __color(self,root):
        if not root:
            return None
        return root.isRed

    def size(self):
        return self.__size(self.root)

    def __size(self,root):
        if not root:
            return 0
        return 1+self.__size(root.left)+self.__size(root.right)

    #出现红色右链接的时候，需要旋转到左链接
    def __rotateleft(self,root):
        if not root:
            return None
        h = root.right
        root.right = h.left
        h.left = root
        h.isRed = root.isRed
        root.isRed = True
        h.count = root.count
        root.count = self.__size(root.left)+self.__size(root.right)+1
        return h

    # 如果想将红色左链接变为右链接，代码如下，
    # 但是需要注意，红黑树红链接均为左链接，所以这个方法并不是单纯将右链接变为做链接
    # 而是和rotateleft一起使用解决插入时出现不符合红黑树结构的红链接的情况
    def __rotateright(self,root):
        h = root.left
        root.left = h.right
        h.right = root
        h.count = root.count
        root.count = self.__size(root.left)+self.__size(root.right)+1
        h.isRed = root.isRed
        root.isRed = True
        return h

    # 将一个节点的两个红色子节点连接线变为黑色
    def __flipColors(self,root):
        root.isRed = not root.isRed
        root.left.isRed = not root.left.isRed
        root.right.isRed = not root.right.isRed


    def Min(self):
        node = self.__Min(self.root)
        return node.key

    def __Min(self,root):
        if not root.left:
            return root
        return self.__Min(root.left)

    def __deleteMin(self,root):
        if not root.left:
            return None
        if not self.__color(root.left) and not self.__color(root.left.left):
            root = self.__moveRedLeft(root)
        root.left = self.__deleteMin(root.left)
        return self.__balance(root)
    #这两个方法都是为了删除节点时平衡黒链接数量，但是会破坏红黑树的结构
    #所以后续需要balance方法将结构修复
    def __moveRedLeft(self,root):
        self.__flipColors(root)
        if self.__color(root.right.left):
            root.right = self.__rotateright(root.right)
            root = self.__rotateleft(root)
            self.__flipColors(root)
            self.__flipColors(root)
        return root

    def __moveRedRight(self,root):
        self.__flipColors(root)
        #如果root.left.left是红色，说明原来的root.left是黑色
        #经过翻转已经时root.left和root.right都为红色，黑链接不减少
        #反之需要将右侧的黑链接变为红链接，保证叶子节点到根节点的黒链接数都一致
        if self.__color(root.left.left):
            root = self.__rotateright(root)
            self.__flipColors(root)
        return root

    def __balance(self,root):
        if self.__color(root.right):
            root = self.__rotateleft(root)
        if self.__color(root.left) and self.__color(root.right):
            self.__flipColors(root)
        if self.__color(root.left) and self.__color(root.left.left):
            root = self.__rotateright(root)
        root.count = self.__size(root.left)+self.__size(root.right)+1
        return root

    def delete(self,key):
        self.root = self.__delete(self.root,key)
        if self.root:
            self.root.isRed = False

    def __delete(self,root,key):
        if root.key>key:
            if not self.__color(root.left) and not self.__color(root.left.left):
                root.left = self.__moveRedLeft(root.left)
            root.left = self.__delete(root.left,key)
        else:
            if self.__color(root.left):
                root = self.__rotateright(root)
            if root.key==key and not root.right:
                return None
            if not self.__color(root.right) and not self.__color(root.right.left):
                root = self.__moveRedRight(root)
            if root.key==key:
                x = self.__Min(root.right)
                root.key,root.val = x.key,x.val
                root.right = self.__deleteMin(root.right)
            else:
                root.right = self.__delete(root.right,key)
        return self.__balance(root)
    def RBprint(self):
        nums = [self.root]
        while nums:
            cur = nums.pop(0)
            print(cur.key,cur.val,cur.isRed)
            if cur.left:
                nums.append(cur.left)
            if cur.right:
                nums.append(cur.right)
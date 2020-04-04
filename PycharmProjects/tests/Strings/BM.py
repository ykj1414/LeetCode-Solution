#启发式的处理不匹配的字符串，并且为最坏情况提供了线性级别的时间，
#核心思想是，模式字符串从右往左遍历，文本从左往右遍历，
#每次遇到不同的字符，就判断文本字符是否在模式字符串中，
# 如果是，就需要转移当前模式匹配字符的位置减去文本字符在模式字符串中最右的位置，若小于1就转移1
# 如果不存在，直接转移模式匹配串长度
class BM(object):
    def __init__(self,pat,R=256):
        self.M = len(pat)
        self.right = [-1]*R
        self.pat = pat
        for i in range(self.M):
            index = ord(pat[i])
            self.right[index] = i

    def search(self,s_txt):
        N = len(s_txt)
        skip,i = 0,0
        while i<N:
            skip=0
            j = self.M-1
            while j>=0:
                if self.pat[j]!=s_txt[i+j]:
                    skip = j-self.right[ord(s_txt[j])]
                    if skip<1:
                        skip = 1
                    break
                j-=1
            if skip==0:
                return (i,i+self.M,s_txt[i:i+self.M])
            i+=skip
        return N
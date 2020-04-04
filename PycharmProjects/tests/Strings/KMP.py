#KMP算法，需要重点理解回退机制，理解回退状态X的状态转移机制
#在实际应用中，由于需要构建的DFA往往很大，所以KMP比起暴力算法没有太大优势
class KMP(object):
    def __init__(self,pat,R=256):
        self.__pat = pat
        self.M = len(pat)
        self.dfa = [[0]*self.M for i in  range(R)]
        self.dfa[ord(pat[0])][0] = 1
        X,j=0,1
        while j<self.M:
            for c in range(R):
                self.dfa[c][j] = self.dfa[c][X] #不匹配的话，将状态退回X状态下，各个字符能到达的状态
            self.dfa[ord(pat[j])][j] = j+1  #更新字符匹配的状态
            X = self.dfa[ord(pat[j])][X]    #更新回退的状态X
            j+=1

    def search(self,strIn):
        N = len(strIn)
        i,j = 0,0
        while i<N and j<self.M:
            j = self.dfa[ord(strIn[i])][j]
            i+=1
        if j==self.M:
            return (i,i-j,strIn[i-j:i])
        else:
            return N
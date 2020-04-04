#低位优先的字符串排序，需要注意的是输入字符串都是定长的
class LSD(object):
    def sort(self,input):
        R = 256
        len_in = len(input)
        aux = [None]*len_in
        str_len = len(input[0])
        i = str_len-1
        while i>=0:
            #低位优先的字符串算法不用考虑结束符\0，所以count[0]永远是0
            count = [0] * (R+ 1)
            for j in input:
                # count[i]的值代表了当前字符i相对i-1的偏移量，即i-1字符出现的总数量
                count[ord(j[i])+1]+=1
            for r in range(R):
                # 为了方便排序，需要将count[i]的值变成相较于最小位的偏移量
                # 在字符排序中最小位是count[1],因为count[0]代表结束字符'\0'
                count[r+1]+=count[r]
            for j in input:
                aux[count[ord(j[i])]]=j
                count[ord(j[i])]+=1
            for k in range(len_in):
                input[k] = aux[k]
            i-=1


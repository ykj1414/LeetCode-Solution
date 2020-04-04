from LSD import LSD
from MSD import MSD
from Quick3Sort import Quick3Sort
from StringST import trieST,TST
from KMP import KMP
from BM import BM
from NFA import NFA
if __name__=="__main__":
    # lsd = LSD()
    # a = ['123','124','134','132','213','234','243']
    # lsd.sort(a)
    # print(a)
    # msd = MSD(15)
    # b = ['123', '124', '134', '132', '213', '234', '243']
    # msd.sort(b)
    # print(b)
    # c = ['123', '124', '134', '132', '213', '234', '243']
    # qks = Quick3Sort()
    # qks.sort(c)
    # print(c)
    # tst = trieST()
    # tst.put("she",1)
    # tst.put("shell",2)
    # print(tst.get("she"))
    # print(tst.get("shell"))
    # tst.delete("shell")
    # print(tst.keys())
    # print(tst.keysThatMatch(""))
    # print(tst.longestPrefixOf('shess'))
    # tpST = TST()
    # tpST.put("she",1)
    # tpST.put("shell",2)
    # print(tpST.get("shell"))
    # print(tpST.get("she"))
    # kmp = KMP('AACAA')
    # print(kmp.search('AABRAACADABRAACAADABRA'))
    # bm = BM('AACAA')
    # print(bm.search('AABRAACADABRAACAADABRA'))
    nfa = NFA("(a|(bc)*d)*")
    print(nfa.edges())
    print(nfa.recognizes("bcdbcd"))
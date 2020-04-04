from PriorityQueue import MaxPQ



if __name__ =="__main__":
    # mpq = MaxPQ(int(input()))
    # a = open("../Data/",'r')
    # cotents = a.readlines()
    a = ['S','O','R','T','E','X','A','M','P','L','E']
    # a = [1, 5, 2, 7, 8, 0, 10, 9, 1, 1, 2, 3, 4, 5, 1, 10, 7, 8, 6]
    pq = MaxPQ(nums=a)
    pq.heapSort()
    print(pq.nlist)




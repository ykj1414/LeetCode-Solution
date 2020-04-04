from LinkedHash import LinkedHash


if __name__=="__main__":
    a = LinkedHash(10,10)
    a.put('1',1)
    print(a.get('2'))
    a.iterate()
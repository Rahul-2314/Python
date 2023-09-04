def TowerOfHanoi(n,src,des,aux):
    if n ==1:
        print("Move disk 1 from source",src,"to destination",des)
        return
    TowerOfHanoi(n-1,src,aux,des)
    print("Move disk", n ," from source",src,"to destination",des)
    TowerOfHanoi(n-1,aux,des,src)

# Driver Code
n=4
TowerOfHanoi(n,"A","B","C")
# A,B,C are the name of rods

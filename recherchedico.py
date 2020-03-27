def recherchedicho(x,L) :
    d=len(L)
    g=0
    while (d-g)> 0:
        m=(d+g)//2
        if L[m]==x:
            return True
        elif L[m]>x:
            d=m
        else:
            g=m+1
    return False

L=[2,6,7,8,9,12,15,18,19]
print(recherchedicho(12,L))
def mortal_fibonacci_rabits(l,n): #n-broj generacija l-zivotni vek
    lista=[1]+[0]*(l-1) #pocinjemo sa jednim juvenilnim zecom
    for i in range (1,n):
        lista=[sum(lista[1:])]+lista[:-1]
    return sum(lista)#broj zeceva
mortal_fibonacci_rabits(5,10)

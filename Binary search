def binary_search(ls,item):
    index=0
    while True:
        mid=int(len(ls)/2)
        if ls[mid]==item:
            return(mid + index)
        elif len(ls)==1:
            return -1
        elif ls[mid]>=item:
            ls=ls[:mid]
        else:
            ls=ls[mid:]
            index=index+mid
print(binary_search([1,2,3,4,5,6,7,8,9,22,33,44,55,666,777],666))

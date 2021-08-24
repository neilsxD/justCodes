def func(n,k): 
    pass
    




def main(): 
    loop= int(input())
    na = []
    # arrs = []
    ka = []
    for _ in range(loop): 
        n , k = list(map(int,input().split()))
        # arrs.append(list(map(int,input().split())))
        na.append(n)
        ka.append(k)

    for i in range(loop): 
        print(func(na[i],ka[i]))

# main()










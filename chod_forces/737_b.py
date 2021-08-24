def func(n,k,arr): 
    if k == n  : return "Yes"
    indarr = [[el,i] for i,el in enumerate(arr) ]
    indarr.sort()
    count = 1
    for i in range(n-1): 
        if indarr[i][1] != indarr[i+1][1] -1 : 
            count+=1 



    if count<=k : return 'Yes'
    else : return 'No'




def main(): 
    loop= int(input())
    na = []
    arrs = []
    ka = []
    for _ in range(loop): 
        n , k = list(map(int,input().split()))
        arrs.append(list(map(int,input().split())))
        na.append(n)
        ka.append(k)

    for i in range(loop): 
        print(func(na[i],ka[i],arrs[i]))

main()










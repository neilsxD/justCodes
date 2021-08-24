def func(n,arr): 
    sum = 0 
    maxi = max(arr)
    for el in arr: 
        sum+=el
    sum-= maxi
    sum/= n-1 
    return maxi + sum








def main(): 
    loop= int(input())
    na = []
    arrs = []
    for _ in range(loop): 
        na.append(int(input()))
        arrs.append(list(map(int,input().split())))


    for i in range(loop): 
        print(func(na[i],arrs[i]))

main()










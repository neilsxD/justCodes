
def keypressed(n,arr,memo):
    
    if n not in memo: 
        nseprate = [] 
        temp = n
        while(temp): 
            nseprate.append(temp%10)
            temp//=10
        flag = 1
        for el in nseprate: 
            if not arr[el]:
                flag = 0
                break
        if flag:
            return len(nseprate)
        mini = float('inf')
        for i in range(int(n**0.5), 2 , -1):
            if n%i == 0: 
                mini = min(mini, keypressed(n//i, arr,memo) + keypressed(i, arr,memo) + 1)
        memo[n] = mini
    return memo[n]
    


def inputs(): 
    loop = int(input())
    arr = []
    n = []
    for i in range(loop):
        arr.append(list(map(int, input().split())))
        n.append(int(input()))
    return loop, arr, n

loop, arr, n = inputs()
for i in range(loop):
    memo = dict()
    ans = keypressed(n[i],arr[i],memo)
    if ans == float('inf'): ans = 'Impossible'
    else: ans += 1  # for equal
    print(f'Case #{i+1}: {ans}')




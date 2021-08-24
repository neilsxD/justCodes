
def main(arr, n):
    ans = []
    if arr[0] == 1 : 
        ans.append(n+1)
        for i in range(1,n+1):
            ans.append(i)
        return ans
    elif arr[-1] == 0 : 
        for i in range(1,n+1):
            ans.append(i)
        ans.append(n+1)
        return ans
    else : 
        for i in range(1,n+1):
            if arr[i-1] == 1 : 
                ans.append(n+1)
                for j in range(i,n+1):
                    ans.append(j)
                return ans
            else : 
                ans.append(i)

        return -1
            
    


def inputs(): 
        loop = int(input())
        strs = []
        n = []
        for i in range(loop):
            n.append(int(input()))
            strs.append(list(map(int,input().split())))
        return loop, strs, n

loop, strs, n = inputs()
for test in range(loop):
    string = strs[test]
    n_str = n[test]
    print(' '.join(list(map(str,main(string,n_str)))))




        
    







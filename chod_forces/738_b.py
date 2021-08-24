

def main():
    def inputs(): 
        loop = int(input())
        strs = []
        n = []
        for i in range(loop):
            n.append(int(input()))
            strs.append(input())
        return loop, strs, n

    loop, strs, n = inputs()
    for test in range(loop):
        opposite = {'B': 'R' , 'R' : 'B'}
        string = strs[test]
        n_str = n[test]
        # ? 
        # b?r
        # b?b
        # b?? 
        ans = []
        if n_str == 1: 
            if string[0] == '?': print('B') 
            else: print(string[0])
        else:
            for i in range(n_str):
                if string[i] == '?':
                    if i == 0: 
                        if string[i+1] in 'BR':
                            ans.append( opposite[string[i+1]])
                        else:
                            ans.append( 'B')
                    
                    elif i == n_str - 1:
                            ans.append( opposite[ans[i-1]])

                    elif string[i+1] in 'BR' :
                            ans.append( opposite[string[i+1]])
                    else: ans.append( opposite[ans[i-1]])
                else : ans.append(string[i])
            
            print(''.join(ans))



        
    


main()




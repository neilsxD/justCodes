




dic_t = {}

def func(s): 
    def diff(square, s): 

        j = 0
        count = 0

        for el in s :
            if j >= len(square) : break
            if square[j] == el : 
                j+=1
        return len(square) + len(s) - 2*j 

    global dic_t
    i = 0 
    mini = len(s) + 1
    while(1)  :
        if i not in dic_t: dic_t[i] = str(2**i) 
        mini = min(mini , diff(dic_t[i], s))
        if len(dic_t[i]) > len(s)+mini : break
        i+=1
    return mini



    




    




def main(): 
    loop= int(input())
    ss = []
    for _ in range(loop): 
        ss.append((input()))
    for i in range(loop):
        print(func(ss[i]))


main()









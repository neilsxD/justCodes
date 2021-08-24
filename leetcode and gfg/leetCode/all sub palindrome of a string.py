def main(s) :
    dic_t = {}
    def isPalindrome(st):
        if st in dic_t : return True
        n = len(st)
        for i in range(0,(n//2) + 1) : 
            if st[i] != st[n-i-1] : return False
        dic_t[st] = 1
        return True





    def recur(st,ans,curr) : 
        if st >= len(s) : 
            ans.append(curr[:])
            return
        for i in range(st,len(s)) :
            if isPalindrome(s[st:i+1]) : 
                curr.append(s[st:i+1])
                recur(i+1,ans,curr)
                curr.pop()


    ans = []
    curr = []
    recur(0,ans,curr)
    return ans




        

# def test_func1() :
#     s = [6,2,5,4,5,1,6]
#     x = main(s)
#     assert x == 12

def test_func1():
    s = "aab"
    x = main(s)
    print(x)
    assert x == [["a","a","b"],["aa","b"]]


def test_func2():
    s = "a"
    x = main(s)
    print(x)
    assert x == [["a"]]








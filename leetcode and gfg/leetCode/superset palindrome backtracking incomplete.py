def main(s) :

        def isPalindrome(st) : 
            n = len(st)
            for i in range(0 ,n//2) : 
                if st[i] != st[n-i-1] : return 0
            return 1

        def recur(st,ans,window) : 
            n = len(window)
            if st == n : return
            for end in range(st+1,n) : 
                if isPalindrome(''.join(window[st:(end+1)])) :
                    window[st:end+1] = [''.join(window[st:end+1])]
                    ans.append(window[:])
                    recur(st+1,ans,window)
                    window[st:st+1] = window[st][:]
            recur(st+1,ans,window)
        
        ans = []
        window =[]
        window.extend (s[:len(s)])
        ans.append(window[:])
        n = len(s)
        for i in range(0,n) :
            recur(i,ans,window)
        return ans






s = "aab"
main(s)



def test_func1() :
    s = "aab"
    x = main(s)
    print(x)
    assert x == [["a","a","b"],["aa","b"]]


def test_func2():
    s = "a"
    x = main(s)
    print(x)
    assert x == [["a"]]

def test_func3():
    s = "aabaa"
    x = main(s)
    print(x)
    assert x == [["a","a","b","a","a"],["a","a","b","aa"],["a","aba","a"],["aa","b","a","a"],["aa","b","aa"],["aabaa"]]








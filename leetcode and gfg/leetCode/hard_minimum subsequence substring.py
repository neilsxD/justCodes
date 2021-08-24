class LRUCache:

    def __init__(self, capacity: int):
        None
        

    def get(self, key: int) -> int:
        None
        

    def put(self, key: int, value: int) -> None:
        None
        


# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)



def main (s,t) :
        def issubs(dic_t,dic_w) :
            for key in dic_t :
                if (key not in dic_w) or (dic_t[key] > dic_w[key]) :
                    return False
            return True

        dic_t = {};dic_w = {}
        min_size = float('inf') ; max_i = 0; max_j=-1
        i=0
        for val in t :
            if val in dic_t: dic_t[val] +=1
            else : dic_t[val] = 1
        for j in range(0,len(s)):
            if s[j] in dic_t:    #stumbled on something valuable 
                if s[j] in dic_w : dic_w[s[j]] +=1
                else : dic_w[s[j]] = 1

                if max_j == -1 :
                    if issubs(dic_t, dic_w):
                        while(i<j):
                            if (s[i] in dic_t):
                                if dic_t[s[i]] < dic_w[s[i]]:
                                    dic_w[s[i]] -=1

                                else : break

                            i+=1

                        if min_size > j-i +1 : 
                            min_size = j-i+1
                            max_i = i
                            max_j = j
                
                elif s[j] == s[i] :
                    while(i<j) :
                        if (s[i] in dic_t):
                            if dic_t[s[i]] == dic_w[s[i]]:
                                if min_size > j-i +1 : 
                                    min_size = j-i+1
                                    max_i = i
                                    max_j = j
                                break
                            elif dic_t[s[i]] < dic_w[s[i]]:
                                dic_w[s[i]] -=1
                        i+=1

        return s[max_i:max_j+1]



s = "ADOBECODEBANC"; t = "ABC"
assert main(s,t) == "BANC"

def test_func1():
    s = "ADOBECODEBANC"; t = "ABC"
    assert main(s,t) == "BANC"


def test_func2():
    s = "a"; t = "aa"
    assert main(s,t) == ""

def test_func3():
    s = "ba"; t = "a"
    assert main(s,t) == "a"
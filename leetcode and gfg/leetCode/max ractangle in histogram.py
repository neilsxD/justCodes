class Solution:

    @classmethod
    def main(self, heights) :
        stack = []
        maxr = 0
        for i,el in enumerate(heights) : 
            while stack and el < stack[-1][0] : 
                temp = stack.pop()
                if stack : 
                    maxr = max(maxr, temp[0]*(i-stack[-1][1]-1))
                else :  maxr = max(maxr, temp[0]*i)
            stack.append([el,i])
            
        while stack : 
                temp = stack.pop()
                if stack : 
                    maxr = max(maxr, temp[0]*(len(heights)-stack[-1][1]-1))
                else :  maxr = max(maxr, temp[0]*len(heights))  
                    
        return maxr
            

print(Solution.main([2,1,5,6,2,3]))




        

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








# from heapq import heappush


class Solution:

    @classmethod
    def main(self, x,y,n) :
        ans= 0
        def isComp(val) : 
            while(val) :
                t = val % 10
                if t != x and t != y  : 
                    return False
                val= val//10
            return True
        
        def reccur(sum, pos): 
            nonlocal ans
            if pos == n-1 : 
                for i in range (1,10) : 
                    sum+= i 
                    if isComp(sum) : ans+=1
                    sum-= i
                return

            for i in range (10) : 
                sum+=i 
                reccur(sum,pos+1)
                sum-=i
            

        reccur(0,0)


        return ans





        


            

print(Solution.main(1,2,2))





        

# def test_func1() :
#     s = [6,2,5,4,5,1,6]
#     x = main(s)
#     assert x == 12

# def test_func1():
#     s = "aab"
#     x = main(s)
#     print(x)
#     assert x == [["a","a","b"],["aa","b"]]


# def test_func2():
#     s = "a"
#     x = main(s)
#     print(x)
#     assert x == [["a"]]








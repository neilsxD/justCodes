# from heapq import heappush
import collections

class Solution:

    @classmethod
    def main(self, piles,k):
        sum = 0 
        n = len(piles)
        if n == 1:
            for i in range(k):  
                piles[0]-=piles[0]//2
            return piles[0]
            
            
            
        piles.sort()
        for i in range(k): 
            maxi = piles.pop()
            maxi  -= maxi//2
            t1 = []
            
            while(piles): 
                temp = piles.pop()
                if(temp<maxi): 
                    piles.append(temp)
                    break
                t1.append(temp)
            piles.append(maxi)
            t1.reverse()
            piles.extend(t1)
            
        for el in piles: 
            sum+=el 
        return sum




        




            

print(Solution.main([4122,9928,3477,9942],
6))




        

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








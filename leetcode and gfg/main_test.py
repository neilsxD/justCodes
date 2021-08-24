# from heapq import heappush
import collections



class Solution:

    @classmethod
    def main(self, x , y ,n) :
        def reccur(pos, x) : 
            nonlocal memo
            if not x : return 1 
            if pos >= n : return 0

            key = str(pos) + ',' + str(x)
            if memo[key] is None : 
                start = 0 ; sum = 0
                if not pos : start = 1
                for i in range(start , 10) : 
                    sum+= reccur(pos+1, x-i)
                memo[key] =  sum
            return memo[key]

        def possibeles(x,y) : 
            v1 = min(x,y)
            v2 = max(x,y)
            nonlocal possx , nmax
            possx.extend([v1,v2])
            i = 0 
            while(1): 
                t1 = possx[i] * 10 + v1 
                if t1 > nmax : return
                possx.append(t1)
                t1 = possx[i] * 10 + v2
                if t1 > nmax : return
                possx.append(t1)
                i+= 1
            

        possx = [] 
        nmax = 9*n ; ansr = 0

        memo = collections.defaultdict(lambda : None)

        possibeles(x,y)




        for el in possx : 
            ansr+=reccur(0,el)

        return ansr



        




            

print(Solution.main(1,2,20))





        

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








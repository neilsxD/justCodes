# from heapq import heappush
import collections
from typing import Text 



class Solution:

    @classmethod
    def main(self, arr) :
        k = max(arr)
        ans=[]
        que = collections.deque()
        que.append([1])
        for _ in range(k):
            temp = que.popleft()
            if temp[-1] :
                t1 = temp.copy()
                t1.append(0)
                que.append(t1)
            else : 
                t1 = temp.copy()
                t2 = temp.copy()
                t1.append(0)
                t2.append(1)
                que.extend([t1,t2])
            ans.append(temp.copy())
        ansr = []
        for el in arr: 
            st_r = list(map(str, ans[el-1]))
            st_r = ''.join(st_r)
            ansr.append(int(st_r))

        return ansr



        




            

print(Solution.main([3,9,25]))





        

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








# from heapq import heappush


class Solution:

    @classmethod
    def main(self, arr: list[int], k: int) :
        ans,n = 0,len(arr)
        def reccur(st, product, flag, current): 
            nonlocal ans,n
            if current >= k : 
                if flag : 
                    ans += product
                return
            if st >= n : return
            for i in range(st,n): 
                product *= arr[i]
                if arr[i]%2 : flag = not flag
                reccur(i+1, product, flag, current+1)
                if arr[i]%2 : flag = not flag
                product //= arr[i]


        reccur(0,1,True,0)
        return ans





        


            

print(Solution.main(arr = [1,4,5,7], k = 2))




        

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








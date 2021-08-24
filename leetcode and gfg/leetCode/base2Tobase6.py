class Solution:

    @classmethod
    def main(self) : 
        ar = list(map(int , input().split()))
        def binartTodec(ar):
            ans = 0 
            for i in range(len(ar)) : 
                ans+= ar[i]*(2**i)
            return ans
        def decTosix(val) : 
            ans = []
            while(val):
                ans.append(val%6)
                val = val//6
            ans = list(map(str, ans))
            return ''.join(ans)
        temp = binartTodec(ar)
        print(temp)
        print(decTosix(temp))

        






Solution.main( )
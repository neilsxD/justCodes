def main (nums) :
        ans = []
        for val in nums : 
            temp  = [[val]]
            for old in ans :
                x = old[:]
                x.append(val)
                temp.append(x)
            ans.extend(temp)

        ans.append([])
        return ans






nums = [1,2,3]
ans =  [[],[1],[2],[1,2],[3],[1,3],[2,3],[1,2,3]]
print(main(nums))

def test_func1():
    nums = [1,2,3]
    ans =  [[],[1],[2],[1,2],[3],[1,3],[2,3],[1,2,3]]
    assert main(nums).sort() == ans.sort()


def test_func2():
    nums = [0]
    ans = [[],[0]]
    assert main(nums).sort() == ans.sort()




def main (arr) :
        total, l = 0 , len(arr)
        for val in arr :
            total+=val
        return ((l+1) * l /2 ) - total

def test_func1():
    nums = [9,6,4,2,3,5,7,0,1]
    assert main(nums) == 8

def test_func2():
    nums = [0]
    assert main(nums) == 1
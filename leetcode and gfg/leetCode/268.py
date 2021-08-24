

def main (arr) :
        set_l = set(arr)
        for i in range(0,len(arr)+1) :
            if i not in set_l :
                return i
        return len(arr)
    

def test_func1():
    nums = [9,6,4,2,3,5,7,0,1]
    assert main(nums) == 8

def test_func2():
    nums = [0]
    assert main(nums) == 1
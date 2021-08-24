

def main (n) :
        if n<3 : return 0
        tally = [1]*n ; count =0
        for i in range(2,n) :
            if tally[i] :
                count +=1
                for j in range(i,n,i) :
                    tally[j] = 0
        return count

def test_func1():
    n = 10
    assert main(n) == 4

def test_func2():
    nums = 1
    assert main(nums) == 0
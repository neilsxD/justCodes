

def main (n) :
        if n<2 : return 0
        count = 0
        vals = set()
        for i in range(2,n+1) :
            if i not in vals :
                count +=1
                for j in range(i,n+1,i) :
                    vals.add(j)



        return count


def test_func1():
    n = 10
    assert main(n) == 4

def test_func2():
    nums = 1
    assert main(nums) == 0
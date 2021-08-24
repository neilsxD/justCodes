
def main (nums1,nums2,nums3,nums4) :
        dic = {};count = 0
        for val1 in nums3 :
            for val2 in nums4:
                if (val1+val2) in dic : dic[val1+val2]+=1
                else : dic[val1 + val2] =1
        for val1 in nums1 :
            for val2 in nums2:
               
                    total = -(val1+val2)
                    if total in dic :
                        count += dic[total]
        return count


def test_func1():
    nums1 = [1,2]; nums2 = [-2,-1]; nums3 = [-1,2]; nums4 = [0,2]
    assert main(nums1,nums2,nums3,nums4) == 2


def test_func2():
    nums1 = [0]; nums2 = [0]; nums3 = [0]; nums4 = [0]
    assert main(nums1,nums2,nums3,nums4) == 1
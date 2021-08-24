

def main (arr) :
        temp , temp2 = 0 , 0
        arr.append(arr[0])
        for i in range (0,len(arr)) :
            temp = arr[i]
            while(arr[temp] != -1 and temp != -1) :
                temp2 = arr[temp]
                arr[temp] = -1
                temp = temp2
            i+=1
        for i in range (0,len(arr)) :
            if arr[i] != -1 :
                return i
        return len(arr)

main([1,0])

def test_func1():
    nums = [9,6,4,2,3,5,7,0,1]
    assert main(nums) == 8

def test_func2():
    nums = [0]
    assert main(nums) == 1
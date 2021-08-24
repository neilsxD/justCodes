from collections import deque

class LRUCache:

    def __init__(self, capacity: int):
        self.max_size = capacity
        self.size = 0
        self.dic_t = {}
        self.que = deque()
        self.trace = 0
        

    def get(self, key: int) -> int:
        if key not in self.dic_t : return -1
        self.trace += 1
        ans,t = self.dic_t[key]
        self.dic_t[key] = (ans, self.trace)
        self.que.appendleft((key, self.trace))
        return ans
        

    def put(self, key: int, value: int) -> None:
        self.trace +=1
        if key in self.dic_t : 
            self.dic_t[key] = (value,self.trace)
            self.que.appendleft((key,self.trace))
        else : 
            if self.size < self.max_size :
                self.dic_t[key] = (value,self.trace)
                self.que.appendleft((key,self.trace))
                self.size +=1
            else :
                while() : 
                    k,t = self.que.pop()
                    if k in self.dic_t and t == self.dic_t[k][1] : 
                        self.dic_t.pop(k)
                        break
                self.dic_t[key] = (value,self.trace)
                self.que.appendleft((key,self.trace))

        


# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)

from collections import Counter



def main (nums,t) :
        None







def test_func1():
    nums = [2,7,11,15]
    assert main(nums,9) == [0,1]


def test_func2():
    nums = [3,3]
    assert main(nums,6) == [0,1]


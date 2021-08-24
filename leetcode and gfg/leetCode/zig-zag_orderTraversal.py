class Solution:
    @classmethod
    def main(self, root) :
        def traverse(node):
            if node is None : return
            if node == 1 : 
                if que : 
                    que.append(1)
                    if self.flip: self.ans.append(self.temp[::-1])
                    else : self.ans.append(self.temp[:])
                        
                    self.flip =  not self.flip
                    self.temp = []
                return 
            self.temp.append(node.val)
            que.append(node.left)
            que.append(node.right)
                
        from collections import deque 
        que = deque()
        self.ans= []
        self.temp = []
        self.flip = 0
        que.append(root)
        que.append(1)
        while(que):
            traverse(que.popleft())
        return self.ans
                

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

root = TreeNode(1)
root.left = TreeNode(2,TreeNode(4))
root.right = TreeNode(3,None, TreeNode(5))

print(Solution.main(root))




        

# def test_func1() :
#     s = [6,2,5,4,5,1,6]
#     x = main(s)
#     assert x == 12

def test_func1():
    s = "aab"
    x = main(s)
    print(x)
    assert x == [["a","a","b"],["aa","b"]]


def test_func2():
    s = "a"
    x = main(s)
    print(x)
    assert x == [["a"]]








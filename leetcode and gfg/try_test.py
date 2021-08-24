# # # # lis = [[]]
# # # # lis[0].append(2)
# # # # print(lis)
# # # # a = []
# # # # a.extend([2])
# # # # print(a)
# # # # # dic_t = {2: 1}
# # # # # print(dic_t)
# # # # # dic_t[3]= ((1,2))
# # # # # print(dic_t[3][1])


# # # # # dic_t[3] = dic_t[3].append(11)
# # # # # print(dic_t)

# # # # # print(dic_t[3])
# # # # # print(dic_t[2])


# # # # a = None
# # # # b = 2
# # # # print(4 or 11)

# # # # print(int('2'))
# # # # x = (int('4') - 2)*3 + 97
# # # # print(chr(x))

# # # # a = [[1,2],[2,3]]
# # # # if a[2][2] and a[2][2] == 3 : print(a)

# # # # a = ['1','2','3','4']
# # # # print(a[1:3])
# # # # a[1:3] = [''.join(a[1:3])]
# # # # # s = 'hello'
# # # # x = []
# # # # x=[s[:len(s)]]
# # # # print(x)

# # # x = ['a','bcd', 'e']
# # # print(x[1][:])
# # # x[1:2] = x[1][:]
# # # print(x)

# # # print(''.join(x[1:3]))

# # # print([[1] * 3] * 3)

# # # st_r = 'abcdef'
# # # print(st_r[2:4])

# # # b = ['22']
# # # b.append(st_r[2:4])
# # # print(b)
# # # a = [1, 2]
# # # print(a[:])

# # # a= { 1 : 2 , 3: 4 } 
# # # if 1 in a : print("zfd")
# # # if 2 in a : print ("nooo")
# # # from functools import reduce

# # # print(reduce(lambda a,b : a.append([[0] * 3]) , [[0] * 4]) ) 

# # # a = set()
# # # print (a)
# # # # a = (1,2)
# # # # print (a)
# # # a.append(3)
# # # print (a)

# # # x=  {i:float('inf') for i in range(5)}
# # # print (x)
# # import heapq
# # a = [2,4,6,3,7,8]
# # min_heap = []
# # heapq.heappush(min_heap, 3)
# # heapq.heappush(min_heap, 2)
# # heapq.heappush(min_heap, a[1])
# # print(min_heap)
# # print(a)

# # a = float('-inf')
# # print(a)

# # import heapq 

# # li = [11,2, 4,3,5,12,14,15,21,26,22]

# # heapq.heapify(li)

# # print(li)

# # print(heapq.nlargest(8, li))
# # print(heapq.nsmallest(7,li))

# # L = ['aaaa', 'bbb', 'cc', 'd', 'eeeee', 'ffffff']
  
# # # sorted without key parameter
# # print(sorted(L))
# # print()

# # def comp(a):
# #     return len(a)%3 

# # # sorted with key parameter
# # print(sorted(L, key = comp))

# # string = "a,v,d,f"
# # print(string[2:5])
# # lis = string.split(',')
# # print(lis[1:3])
# # lis[1:3] = [ 'a' , 'd' , 'f ']
# # print(lis)

# # Python code to demonstrate working of 
# # append(), appendleft(), pop(), and popleft()
  
# # importing "collections" for deque operations
# # import collections
  
# # # initializing deque
# # de = collections.deque([1,2,3])
  
# # # using append() to insert element at right end 
# # # inserts 4 at the end of deque
# # de.append(4)
  
# # # printing modified deque
# # print ("The deque after appending at right is : ")
# # print (de)
  
# # # using appendleft() to insert element at left end 
# # # inserts 6 at the beginning of deque
# # de.appendleft(6)
  
# # # printing modified deque
# # print ("The deque after appending at left is : ")
# # print (de)
  
# # # using pop() to delete element from right end 
# # # deletes 4 from the right end of deque
# # de.pop()
  
# # # printing modified deque
# # print ("The deque after deleting from right is : ")
# # print (de)
  
# # # using popleft() to delete element from left end 
# # # deletes 6 from the left end of deque
# # de.popleft()
  
# # # printing modified deque
# # print ("The deque after deleting from left is : ")
# # print (de)

# # print(de[1])
# # # cop = de[:]
# # # print(cop)
# # cop2 = de.copy()
# # print(cop2)

# # print(de.remove(1))
# # print(de)

# # from collections import deque

# # lis = deque()
# # if lis : print('no')
# # else : print('yes')

# # a = [1,2,3,5,6,7,9]
# # for i,el in enumerate(a) : 
# #     print(i,el)


# # For list of integers
# # lst1 = [] 
 
# # # For list of strings/chars
# # lst2 = [] 
 
# # # lst1 = map(lambda x: int(x), input("Enter the list items : ").split())
# # a,b = [int(x) for x in input("list:").split()]
 
# # # lst2 = input("Enter the list items : ").split()
 
# # print(a,b)
# # print(type(a), type(b))
# # # print(lst2)

# # sumt = 

# # m = [[0]*3 for _ in range(4)]
# # print(m)
# # m[2][2] = 1
# # m[0][0] = 2
# # print(m)
# # n=2
# # # print(10**(n-1))
# # for i in range(10**(n-1), 10**n):
# #     print(i)

# # val = set()
# # st = 'hello me'
# # val.update(st)
# # print(val)
# # for i,el in enumerate(val) : 
# #     print(i,el)

# # import collections


# # dic_t = collections.defaultdict(lambda : [] )
# # dic_t[2].append([3])
# # print(dic_t[2]) 

# # print(max(dic_t[2], dic_t[3]))

# # que = collections.deque()
# # que.append([1])
# # print(que)
# # que.append([1,2])
# # print(que)

# # arr = [1, 0, 0, 0, 1, 0, 1]
# # st_r  = list(map(str, arr))
# # print(st_r)

# # ans = ''.join(st_r)
# # print(int(ans))

# # a = [[1,3],[4,8],[2,2]]
# # a.sort( key= lambda x : x[1] )
# # print(a)

# # a = [2,4,6,3,8,1]
# # s = a.copy()
# # s.sort(reverse=1)
# # print(a)
# # print(s)
# # x = set(s)
# # for i,e in enumerate(x) : 
# #     print(i,e)
# # dic_t =collections.Counter(a) 
# # print(dic_t)


# # el = 'ab'
# # temp = [el] 
# # temp.extend([])
# # print(temp)



# def numberOfWays(string):

#         # Code here
#         n = len(string)
        
#         def lenpalindrome(ind,f): 
#             nonlocal n 
            
#             i = 0
#             while(ind-i>=0 and ind+i+f<n):
#                 if string[ind-i] != string[ind+i+f] : break
#                 i+=1
#             return 2*(i-1) +1 + f 
        
#         total = n
#         for i in range(n) : 
#             l = lenpalindrome(i,0)
#             if l : 
#                 total+= l//2
#             l = lenpalindrome(i,1)
#             if l : 
#                 total+= l//2
        
#         return total

# print(numberOfWays('aaa'))

# print(str(44443).split('.'))
arr = [5,3,6,23,5]

print(max(arr))
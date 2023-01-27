
'''Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target.
You may assume that each input would have exactly one solution, and you may not use the same element twice.
You can return the answer in any order.
Example :
Input: nums = [2,7,11,15], target = 9
Output: [0,1]
Explanation: Because nums[0] + nums[1] == 9, we return [0, 1].'''



n=list(map(int,input().split()))
t=int(input())
m=[]
for i in range(len(n)):
    for j in range(len(n)):
        if(n[i]+n[j]==t):
           if(i not in m):
               m.append(i)
           if(j not in m):
               m.append(j)
print(m)
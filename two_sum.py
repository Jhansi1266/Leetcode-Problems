#Two sum code in Python
nums=list(map(int,input().split()))
target=int(input())
l=len(nums)
for i in range(l):
    for j in range(i+1,l):
        if nums[i]+nums[j]==target:
            print([i,j])
inp = int(input())

nums = []

for k in range(inp):
    nums.append(input().split(" "))
        
        
        
for i in range(len(nums)):
    if int(nums[i][0]) * int(nums[i][1]) == int(nums[i][2]):
        print("POSSIBLE DOUBLE SIGMA")
    if int(nums[i][0]) * int(nums[i][1]) != int(nums[i][2]):
        print("16 BIT S/W ONLY")
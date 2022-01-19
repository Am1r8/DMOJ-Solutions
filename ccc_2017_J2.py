shSum = int(input())
num = int(input())

nums = shSum

for i in range(num):
    shSum = shSum * 10
    nums = nums + shSum
    
print(nums)
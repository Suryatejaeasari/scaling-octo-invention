def sss(nums, target):
    
    def backtracking(start,curr_num,subset):
        if curr_num == target:
            print(subset)
            return
        if curr_num > target:
            return
        for i in range(start, len(nums)):
            backtracking(i+1, curr_num+nums[i], subset+[nums[i]])
    nums.sort()
    backtracking(0,0,[])
nums = [int(x) for x in input("Enter numbers:").split()]
target = int(input("Enter Target:"))
sss(nums, target)

class Solution:
    def threeSum(self, nums: list[int]) -> list[list[int]]:
        ans = nums[0] + nums[1] + nums[2]
        temp = []
        nums.sort()
        for i in range(len(nums) - 2):
            left = i + 1
            right = len(nums) - 1
            while left < right:
                print(i, left, right)
                current = nums[i] + nums[left] + nums[right]
                if(current == 0):
                    a = [nums[i], nums[left], nums[right]]
                    temp.append(a)
                if(current > 0):
                    right = right - 1
                else:
                    left = left + 1
        return temp
                # new = abs(current - target)
                # old = abs(ans - target)
                # if(new < old):
                #     ans = current
                # if(current < target):
                #     left = left + 1
                # else:
                #     right = right - 1
        return ans

a = Solution()
ans = a.threeSum([-1,0,1,2,-1,-4])
print("Ans: ", ans)
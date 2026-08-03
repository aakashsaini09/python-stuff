class Solution:
    def threeSum(self, nums: list[int]) -> list[list[int]]:
            temp = []
            nums.sort()
            for i in range(len(nums) - 2):
                if i > 0 and nums[i] == nums[i - 1]:
                    continue
                left = i + 1
                right = len(nums) - 1

                while left < right:
                    current = nums[i] + nums[left] + nums[right]

                    if current == 0:
                        temp.append([nums[i], nums[left], nums[right]])
                        left += 1
                        right -= 1
                        while left < right and nums[left] == nums[left - 1]:
                            left += 1
                        while left < right and nums[right] == nums[right + 1]:
                            right -= 1
                    elif current > 0:
                        right -= 1
                    else:
                        left += 1
            return temp
                # new = abs(current - target)
                # old = abs(ans - target)
                # if(new < old):
                #     ans = current
                # if(current < target):
                #     left = left + 1
                # else:
                #     right = right - 1

a = Solution()
ans = a.threeSum([1,2,0,1,0,0,0,0])
print("Ans: ", ans)
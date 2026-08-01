from typing import List
class Solution:
    def intToRoman(self, num: int) -> int:
        ans = ""
        if(num == 0):
            return 0
        obj = {
            1000: "M",
            900: "CM",
            500: "D",
            400: "CD",
            100: "C",
            90: "XC",
            50: "L",
            40: "XL",
            10: "X",
            9: "IX",
            5: "V",
            4: "IV",
            1: "I",
        }
        for key in obj:
            while(num >= key):
                print(ans, obj[key], key)
                ans = ans + obj[key]
                num = num - key
        return ans
        # while(i != len(rev)):
        #     current = obj[rev[i]]
        #     if(pre > current):
        #         value = pre - current
        #         ans = ans - pre + value
        #         pre = current
        #     else:
        #         if(pre != 0):
        #             print(current)
        #             pre = current
        #             ans = ans + current
        #         else:
        #             pre = current
        #             ans = ans + current
        #     i = i + 1


    def longestCommonPrefix(self, strs: List[str]) -> str:
        fir = strs[0]
        if(len(strs) == 0):
            return ""
        
        if(len(strs) == 1):
            return strs[0]
        l = 0
        while(l != len(fir)):
            for i in strs:
                # print("i[l]: ", i[l], "fir[l]: ", fir[l], "i: ", i)
                if(l >= len(i)):
                    return fir[0:l]
                if(i[l] != fir[l]):
                    return fir[0:l]
            l = l + 1
        return fir[0:l]
        # for i in l:
        #     print("i: ", i)
            # for j in strs:
            #     print("J is: ", j)
            #     if(j[i] == strs[0][i]):
            #         print("match: ", j[i], str[0][i])

    def threeSumClosest(self, nums: List[int], target: int) -> int:
        # self.bubble_sort(nums)
        nums.sort()
        print(nums)
        ans = nums[0] + nums[1] + nums[2]
        i = 0
        while i != len(nums) - 2:
            j = i + 1
            while j != len(nums) - 1:
                k = j + 1
                while k != len(nums):
                    current:float = nums[i] + nums[j] + nums[k]
                    new = abs(current - target)
                    old = abs(ans - target)
                    if(new < old):
                        ans = current
                    # print(current, nums[i], nums[j], nums[k])
                    k = k + 1
                j = j + 1
            i = i + 1
        return ans
    
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        ans = nums[0] + nums[1] + nums[2]
        nums.sort()
        for i in range(len(nums) - 2):
            left = i + 1
            right = len(nums) - 1
            print("l: ", nums[left])
            print("r: ", nums[right])
            while left < right:
                # print(i, left, right)
                current = nums[i] + nums[left] + nums[right]
                new = abs(current - target)
                old = abs(ans - target)
                if(new < old):
                    ans = current
                if(current < target):
                    left = left + 1
                else:
                    right = right - 1
        return ans
    def bubble_sort(self, arr):
        n = len(arr)
        for i in range(n):
            swapped = False
            for j in range(0, n - i - 1):
                if arr[j] > arr[j + 1]:
                    arr[j], arr[j + 1] = arr[j + 1], arr[j]
                    swapped = True
            if not swapped:
                break
        return arr
a = Solution()
# ans = a.threeSumClosest([0, 0, 0], 1)
ans = a.threeSumClosest([-4, 12, 45, 12, 56,7], 25)
print("Ans: ", ans)
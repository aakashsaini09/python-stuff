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
ans = a.threeSumClosest([-43,57,-71,47,3,30,-85,6,60,-59,0,-46,-40,-73,53,68,-82,-54,88,73,20,-89,-22,39,55,-26,95,-87,-57,-86,28,-37,43,-27,-24,-88,-35,82,-3,39,-85,-46,37,45,-24,35,-49,-27,-96,89,87,-62,85,-44,64,78,14,59,-55,-10,0,98,50,-75,11,97,-72,85,-68,-76,44,-12,76,76,8,-75,-64,-57,29,-24,27,-3,-45,-87,48,10,-13,17,94,-85,11,-42,-98,89,97,-66,66,88,-89,90,-68,-62,-21,2,37,-15,-13,-24,-23,3,-58,-9,-71,0,37,-28,22,52,-34,24,-8,-20,29,-98,55,4,36,-3,-9,98,-26,17,82,23,56,54,53,51,-50,0,-15,-50,84,-90,90,72,-46,-96,-56,-76,-32,-8,-69,-32,-41,-56,69,-40,-25,-44,49,-62,36,-55,41,36,-60,90,37,13,87,66,-40,40,-35,-11,31,-45,-62,92,96,8,-4,-50,87,-17,-64,95,-89,68,-51,-40,-85,15,50,-15,0,-67,-55,45,11,-80,-45,-10,-8,90,-23,-41,80,19,29,7], 255)
print("Ans: ", ans)
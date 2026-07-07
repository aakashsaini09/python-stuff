from typing import List

# 9th prob 
class Solution1:
    def isPalindrome(self, x: int) -> bool:
        ans: bool = False
        a = str(x)
        rev = ''
        i = len(a)
        if(len(a) == 1):
            return True
        if(len(a) == 0):
            return False
        while(i != 0):
            rev = rev + a[i - 1]
            i = i - 1
        # print(a, rev)
        i = len(a)
        while(i != 0):
            # print(i)
            if(rev[i - 1] == a[i - 1]):
                # print("rev", rev[i - 1], "a: ", a[i - 1])
                ans = True
            else:
                return False
            i = i - 1
        return ans

# 10th prob
class Solution2:
    def isMatch(self, s: str, p: str) -> bool:
        ans = False
        return ans
class Solution:
    def maxArea(self, height: List[int]) -> int:
        start = 0
        end = len(height) - 1
        area = 0
        print(start, end)
        while(start < end):
            dist = end - start
            sec = height[start]
            if(height[end] < height[start]):
                sec = height[end]
            temp = dist * sec
            if(area < temp):
                area = temp
            # print("temp: ", temp, "area", area)
            # print(start, " = ", height[start] ,  end, " = ", height[end])
            if(height[start] > height[end]):
                end = end - 1
                continue
            if(height[start] < height[end]):
                start = start + 1
                continue
            if(height[start] == height[end]):
                start = start + 1
                continue
        return area
a = Solution()
ans = a.maxArea([])
print("Ans: ", ans)
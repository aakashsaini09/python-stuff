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
class Solution3:
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
    
# 13 Roman number to intc conver
# Symbol       Value
# I             1
# V             5
# X             10
# L             50
# C             100
# D             500
# M             1000
class Solution:
    def romanToInt(self, s: str) -> int:
        ans = 0
        i = len(s)
        rev = ''
        pre: int = 0
        if(len(s) == 0):
            return 0
        while(i != 0):
            rev= rev + s[i - 1]
            i = i - 1
        obj = {
            "I": 1,
            "V": 5,
            "X": 10,
            "L": 50,
            "C": 100,
            "D": 500,
            "M": 1000
        }
        i = 0
        while(i != len(rev)):
            current = obj[rev[i]]
            print(pre, current, ans)
            if(pre > current):
                value = pre - current
                ans = ans - pre + value
                print("Value", value)
                pre = current
                print("#####################")
            else:
                if(pre != 0):
                    print(current)
                    pre = current
                    ans = ans + current
                else:
                    pre = current
                    ans = ans + current
                print("*************************")
            i = i + 1
        return ans

    # def rev(self, val):
    #     ab = ''
    #     i = len(val)
    #     while(i != 0):
    #         ab = ab + val[i - 1]
    #         i = i - 1
    #     return ab
   
a = Solution()
ans = a.romanToInt("LXX")
print("Ans: ", ans)
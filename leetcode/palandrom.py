# 9th prob 
class Solution2:
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


class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        ans = False
        return ans
a = Solution()
ans = a.isMatch("0")
print("Ans: ", ans)
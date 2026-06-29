class Solution:
    def longestPalindrome(self, s: str) -> str:
        if len(s) <= 1:
            return s

        def expand_from_center(left, right):
            while left >= 0 and right < len(s) and s[left] == s[right]:
                left -= 1
                right += 1
            return s[left + 1:right]

        max_str = s[0]

        for i in range(len(s) - 1):
            odd = expand_from_center(i, i)
            even = expand_from_center(i, i + 1)

            if len(odd) > len(max_str):
                max_str = odd
            if len(even) > len(max_str):
                max_str = even

        return max_str
    def longestP(self, s: str) -> str:
        ans = ''
        left=''
        right=''
        for i in range(len(s) - 1):
            if(i == 0):
                continue;
            left = s[i - 1]
            right = s[i + 1]
            if left == right:
                ans = left + s[i] + right

        return ans
    
    def lpSolution(self, s: str) -> str:
        if len(s) <=1:
            return s
        ml = 1
        ms = s[0]
        for i in range(len(s) - 1):
            for j in range (i+1, len(s)):
                if j-i+1 > ml and s[i:j+1] == s[i:j+1][::-1]:
                    ml = j - i + 1
                    ms = s[i:j+1]
        return ms
v1 = Solution()
# v2 = v1.longestP('Aakash')
# print("Ans: \n", v2)

class Solution1:
    def reverse(self, x: int) -> int:
        ans = 0
        # print("x: ", x) 
        if(len(x) == 1):
            ans = x
        else:
            ans = reversed(x)
        return ans

vi = Solution1()
ans = vi.reverse(231)
print("Ans: ", ans)
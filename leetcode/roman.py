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

a = Solution()
ans = a.intToRoman(3749)
print("Ans: ", ans)
# **************************************#8 String to Integer****************************************************
class Solution:
    def myAtoi(self, s: str) -> int:
        a = s.replace(" ", "")
        temp = ''
        ans = ''
        i = len(a)
        if(len(a) == 1):
            return int(a)
        if(a[0] == '-'):
            if(len(a) == 2):
                return int(a)
            z = a.split('-', 1)
            temp = z[1]
            while(i != 1):
                if(ans == '' and temp[i - 2] == '0'):
                    i = i - 1
                    continue
                if(temp[i-2].isalpha()):
                    i = i - 1
                    continue
                ans = ans + temp[i - 2]
                i = i - 1
            res = int(ans)
            r = res - res - res
            return r
        if(a[0] == '+'):
            if(len(a) == 2):
                return int(a)
            z = a.split('+', 1)
            temp = z[1]
            while(i != 1):
                if(temp[i-2].isalpha()):
                    i = i - 1
                    continue
                ans = ans + temp[i - 2]
                i = i - 1
            return int(ans)
        while(i != 0):
            if(temp[i-2].isalpha()):
                i = i - 1
                continue
            ans = ans + a[i - 1]
            i = i - 1
        return int(ans)
    
   
a = Solution()
result = a.myAtoi("   -042")
print(type(result), result)

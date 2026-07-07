# **************************************#8 String to Integer****************************************************
class Solution:
    def myAtoi(self, s: str) -> int:
        a = s.lstrip()
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
    

    def sol(self, s: str) -> int:
        if not s:
            return 0
        
        # Constants for 32-bit signed integer range
        INT_MAX = 2**31 - 1
        INT_MIN = -2**31
        
        i = 0
        n = len(s)
        
        # Step 1: Skip leading whitespace
        while i < n and s[i] == ' ':
            i += 1
        
        # Check if we've reached the end
        if i == n:
            return 0
        
        # Step 2: Check for sign
        sign = 1
        if s[i] == '+':
            i += 1
        elif s[i] == '-':
            sign = -1
            i += 1
        
        # Step 3: Read digits and convert
        res = 0
        while i < n and s[i].isdigit():
            digit = int(s[i])
            res = res * 10 + digit
            
            if sign * res <= INT_MIN:
                return INT_MIN
            if sign * res >= INT_MAX:
                return INT_MAX
            
            i += 1
        
        # Step 4: Apply sign and return
        return res * sign
   
a = Solution()
result = a.sol("-11919730356x")
print(type(result), result)

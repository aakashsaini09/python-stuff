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
        a = s.lstrip()
        ans = ''
        i = 0
        if(len(a) == 1):
            return int(a)
        if(a[0] == '-'):
            if(len(a) == 2):
                return int(a)
            z = a.split('-', 1)
            temp = z[1]
            while(i != len(temp)):
                if(ans == '' and temp[i] == '0'):
                    i = i + 1
                    continue
                if(temp[i].isalpha()):
                    i = i + 1
                    continue
                if(temp[i].isspace()):
                    return 0
                if(temp[i].isdigit()):
                    ans = ans + temp[i]
                    i = i + 1
                else:
                    return 0
            # res = self.rev(ans)
            temp = ''
            i = len(ans)
            while(i != 0):
                temp = temp + ans[i - 1]
                i = i - 1
            i = int(temp)
            r = i - i - i
            return r
        # *********************************************************************************
        if(a[0] == '+'):
            if(len(a) == 2):
                return int(a)
            z = a.split('+', 1)
            temp = z[1]
            while(i != len(temp)):
                if(ans == '' and temp[i] == '0'):
                    i = i + 1
                    continue
                if(temp[i].isalpha()):
                    i = i + 1
                    continue
                if(temp[i].isspace()):
                    return 0
                if(temp[i].isdigit()):
                    ans = ans + temp[i]
                    i = i + 1
                else:
                    return 0
            # res = self.rev(ans)
            temp = ''
            i = len(ans)
            while(i != 0):
                temp = temp + ans[i - 1]
                i = i - 1
            return int(temp)
        
        while(i != len(a)):
            if(ans == '' and a[i] == '0'):
                i = i + 1
                continue
            if(a[i].isalpha()):
                i = i + 1
                continue
            if(a[i].isspace()):
                    return 0
            if(a[i].isdigit()):
                ans = ans + a[i]
                i = i + 1
            else:
                return 0
        temp = ''
        i = len(ans)
        while(i != 0):
            temp = temp + ans[i - 1]
            i = i - 1
        
        return int(temp)
    def rev(self, val):
        ab = ''
        i = len(val)
        while(i != 0):
            ab = ab + val[i - 1]
            i = i - 1
        print("final ans: ", ab)
        return int(ab)
   
a = Solution()
result = a.sol("   0 43")
print(type(result), result)

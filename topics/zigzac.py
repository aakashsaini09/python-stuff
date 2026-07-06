class Solution:
    def convert(self, s: str, numRows: int) -> str:
        row = 0
        dir = 'down'
        res = ''
        list = [''] * numRows
        if(numRows == 1):
            return s
        st = s.replace(" ", "")
        for i in range(len(st)):
            if(row == 0):
                dir = 'down'
            if(row == numRows - 1):
                dir = 'up'
            if(dir == 'down' and row < numRows):
                list[row] += st[i]
            elif(dir == 'up' and row > 0):
                list[row] += st[i]
            if(dir == 'up'):
                row = row- 1
            if(dir == 'down'):
                row = row + 1
            print(row, dir, st[i], i, res)
        for r in list:
            print("r: ", r)
            res += r
        return res
c = Solution()
res = c.convert("thisistheway", 3)
print("res: ", res)
class Solution:
    def reverse(self, x: int) -> int:
        res = ''
        if x < 0:
            num = str(-x)
        else: num = str(x)
        i = len(num)
        if(num == 1):
            return x
        while(i != 0):
            res = res + num[i - 1];
            i = i - 1
        a = int(res)
        check = self.is_signed_32bit(x)
        print("check: ", check)
        if(check == False):
            return 0
        if(x < 0):
            return -a
        return a
    def is_signed_32bit(self, n):
        return -2**31 <= n < 2**31 - 1
c = Solution()
res = c.reverse(1534236469)
print(res)

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
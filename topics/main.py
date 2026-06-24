print("Hello world")
class Node: 
    def __init__(self, data=None, next=None):
        self.data = data
        self.next = next
class LinkedList:
    def __init__(self):
        self.head = None

if __name__ == "__main__":
    pass

# factorial
def fact(num):
    temp = 1
    while num > 0:
        print("running for values: ", temp, num)
        temp = num * temp
        num = num - 1
    return temp

result = fact(5);
print(result)

class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if(len(s) == 0):
            return 0
        ans = 1
        temp = ''
        for i in s:
            print("temp len: ", int(len(temp)))
            if(int(len(temp)) > 0):
                for j in temp:
                    print("j: ", j)
                    if(j == i):
                        if(ans < int(len(temp))):
                            ans = len(temp)
                        temp = ''
                        continue
            temp = temp+i
            print("ans: ", ans)
            print("Temp: ", temp)
            if(ans < int(len(temp))):
                ans = len(temp)
            print("********************")
        return ans
strings = Solution()
ans1 = strings.lengthOfLongestSubstring("tabcabcbb")
ans2 = strings.lengthOfLongestSubstring("au")
print(ans1, ans2)
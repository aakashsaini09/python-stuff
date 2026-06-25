from typing import List

class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        num = 0.0
        arr = self.mergeArray(nums1, nums2)
        if(len(arr) == 0):
            num = 0
            return num
        elif(len(arr) == 1):
            num = arr[0]
            return num
        else:
            print("array is bigger then 1")
            le = len(arr)
            if le % 2 == 0:
                print("even")
                temp = le / 2
                f: float = arr[int(temp - 1)] + arr[int(temp)]
                g: float = f / 2
                return g
            else:
                center: float = arr[len(arr) // 2]
                return center
        return num
    
    def mergeArray(self, a1: List[int], a2: List[int]) -> List[int]:
        ans = []
        i, j = 0, 0
        while i < len(a1) and j < len(a2):
            if a1[i] < a2[j]:
                ans.append(a1[i])
                i = i + 1
            else: 
                ans.append(a2[j])
                j = j + 1
        ans.extend(a1[i:])
        ans.extend(a2[j:])
        return ans
    
sol = Solution()
ans = sol.findMedianSortedArrays([], [5])
print(ans)
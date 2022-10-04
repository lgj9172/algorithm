class Solution:
    def popBigest(self, nums1: List[int], nums2: List[int]) -> int:
        if(len(nums1)>0 and len(nums2)>0):
            if nums1[-1] >= nums2[-1]:
                return nums1.pop()
            else:
                return nums2.pop()
        elif(len(nums1)>0 and len(nums2)==0):
            return nums1.pop()
        elif(len(nums1)==0 and len(nums2)>0):
            return nums2.pop()
        else:
            return 0
        
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        total = len(nums1) + len(nums2)
        half_index= ((total+1)/2)-1
        curr_index = 0
        before = 0
        while True:
            biggest = self.popBigest(nums1, nums2)
            if curr_index < half_index:
                before = biggest
                curr_index += 1
            elif curr_index == half_index:
                return biggest
            else:
                return (before+biggest) / 2
            
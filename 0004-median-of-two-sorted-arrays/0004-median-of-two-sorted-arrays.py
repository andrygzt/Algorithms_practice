class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        uniqueList = []
        pointer1, pointer2 = 0, 0

        while pointer1<len(nums1) and pointer2<len(nums2):
            if nums1[pointer1] > nums2[pointer2]:
                uniqueList.append(nums2[pointer2])
                pointer2 += 1
            else:
                uniqueList.append(nums1[pointer1])
                pointer1 += 1

        while pointer1<len(nums1):
            uniqueList.append(nums1[pointer1])
            pointer1 += 1
        
        while pointer2<len(nums2):
            uniqueList.append(nums2[pointer2])
            pointer2 += 1

        mid = len(uniqueList)//2

        if len(uniqueList)%2==0:
            return(uniqueList[mid-1]+ uniqueList[mid])/2
        else:
            return (uniqueList[mid])
class Solution(object):
    def findMedianSortedArrays(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: float
        """
        n3=sorted(nums1+nums2)
        if(len(n3)%2==0):
            a=len(n3)//2
            res=(n3[a-1]+n3[a])/2.0
        else:
            b=len(n3)//2
            res=n3[b]
        return(res)

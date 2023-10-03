class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        if m==0:
            nums1[:n]=nums2[:n]
            return
        if n==0:
            nums1 = nums1[:m]
            return

        i = len(nums1)-1
        while m and n:
            if nums1[m-1]>nums2[n-1]:
                nums1[i]=nums1[m-1]
                m -= 1
                print(nums1)
                print("1")
        
            else:
                nums1[i]=nums2[n-1]
                n -= 1
                print(nums1)
                print("2")
            i-=1
        if m>0:
            nums1[:m]=nums1[:m]
           
        if n>0:
            nums1[:n]=nums2[:n]
      


            
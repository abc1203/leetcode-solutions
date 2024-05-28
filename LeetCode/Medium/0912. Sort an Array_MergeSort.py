class Solution(object):
    def sortArray(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]

        idea:
         - mergesort
        """

        def merge(arr, l, m, r):
            left, right = arr[l:m+1], arr[m+1:r+1]
            i, j = 0, 0

            while i < len(left) or j < len(right):
                if i == len(left):
                    arr[l+i+j] = right[j]
                    j += 1
                elif j == len(right):
                    arr[l+i+j] = left[i]
                    i += 1
                else:
                    if left[i] < right[j]:
                        arr[l+i+j] = left[i]
                        i += 1
                    else:
                        arr[l+i+j] = right[j]
                        j += 1

        def mergeSort(arr, l, r):
            if l >= r: return arr

            mid = (l + r) / 2
            mergeSort(arr, l, mid)
            mergeSort(arr, mid+1, r)
            merge(arr, l, mid, r)

            return arr

        
        return mergeSort(nums, 0, len(nums)-1)
        

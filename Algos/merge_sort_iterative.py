#merging logic can be imporoved
#assume we have to merge 2 list of size 1 initially
#keep merging while there is atleast one element in right list

#in the end, merge the first 2 ** (logn - 1) and remaining elements in the array

class Solution:
    
    def sortArray(self, nums: List[int]) -> List[int]:
      
      list_size = 1
      length = len(nums)
      
      
      def merge(nums, left_array, right_array, left, left_len, right_len):
          i = 0
          j = 0
          nums_idx = left
          while(i < left_len and j < right_len):
            if left_array[i] <= right_array[j]:
              nums[nums_idx] = left_array[i]
              i += 1
            else:
              nums[nums_idx] = right_array[j]
              j += 1
            nums_idx += 1

          while(i < left_len):
            nums[nums_idx] = left_array[i]
            i += 1
            nums_idx += 1
          
      while(list_size*2 < length):
        left = 0
        
        while(left + list_size < length):
          right = min(left + 2*list_size - 1, length - 1)
          rstart = left + list_size
          merge(nums, nums[left:rstart], nums[rstart:right + 1], left, rstart - left, right - rstart + 1)
          
          left += 2*list_size
          
        list_size = list_size * 2
      
      merge(nums, nums[:list_size], nums[list_size:], 0, list_size, length - list_size)
      return nums
        
        

#TC: T(n) = 2T(n/2) + O(n) , a= 1, b=2, log a base b = 1, k = 1, logn*f(n) ie nlogn
#SC: O(n) for auxillary array and O(logn) for recursion stack

#Simple merge sort, make a copy when passing in func, and a new result array while returning

def merge(left, right):
 l_len, r_len = len(left), len(right)
 l, r = 0, 0
 result = []
 while(l < l_len and r < r_len):
   if left[l] <= right[r]:
     result.append(left[l])
     l += 1
   else:
     result.append(right[r])
     r += 1
 
 while(l < l_len):
   result.append(left[l])
   l += 1
 while(r < r_len):
   result.append(right[r])
   r += 1
 return result
 
 
def merge_sort_rec(arr):
 length = len(arr)
  if length > 1:
   l, r = 0, length - 1
   mid = l+ (r-l)//2
   left = merge_sort_rec(arr[l: mid + 1])
   right = merge_sort_rec(arr[mid+1: r + 1])
   return merge(left, right)
 else:
 
   return arr
 
def merge_sort(arr):
 return merge_sort_rec(arr)
 
print(merge_sort([-8,2,-3,-5,3,7,3,7, 100, 100, 99,98,98]))


#Space Optimised version, make a temp array, copy to temp array from l to r before merging the results in main array
class Solution:
  
    def merge(self, nums, temp, lstart, rstart, rend):
      
      for i in range(lstart, rend+1):
        temp[i] = nums[i]
        
      lend = rstart - 1
      
      result_idx = lstart
      
      while(lstart <= lend and rstart <= rend):
        if temp[lstart] <= temp[rstart]:
          nums[result_idx] = temp[lstart]
          lstart += 1
        else:
          nums[result_idx] = temp[rstart]
          rstart += 1
        result_idx += 1
      
      while(lstart <= lend):
          nums[result_idx] = temp[lstart]
          lstart += 1
          result_idx += 1
      
    def merge_sort(self, nums, temp, left, right):
      if right > left:
        mid = left + (right-left)//2
        self.merge_sort(nums, temp, left, mid)
        self.merge_sort(nums, temp, mid+1, right)
        self.merge(nums, temp, left, mid+1, right)
        
      
    def sortArray(self, nums: List[int]) -> List[int]:
        length = len(nums)
        temp_array = [-1]*length
        
        self.merge_sort(nums, temp_array, 0, length - 1)
        return nums

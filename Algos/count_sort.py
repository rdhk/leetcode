
#[8,2,3,1,1,5,3,7,3,7, 100, 100, 99,98,98]
Time Complexity: O(n+k) 
Space Complexity: O(n+k)
(where k is the range of nos ie (Max_el-Min_el +1))
Count sort can thus be used with negative nos or where the range of nos (Max - min) is significantly lesser than the size of array (N) by using a appropriate hashing func for index ie (num - min_num)
Application:
Can be used for finding the number of elements <= or strictly less than the curr number in array. Leetcode link 
Nums are from range 0 to 100

def count_sort(arr):
 count_arr = [0]*101

 for num in arr:
   count_arr[num] += 1
  for i in range(1, 101):
   count_arr[i] += count_arr[i-1]

 results = [0]*len(arr)
 for i in range(len(arr) -1, -1, -1):
   count_arr[arr[i]] -= 1
   results[count_arr[arr[i]]] = arr[i]
 return results

print(count_sort([0,0, 8,2,3,1,1,5,3,7,3,7, 100, 100, 99,98,98]))

def count_sort_generic(arr):
 min_el = min(arr)
 max_el = max(arr)
 no_elem_count_arr = max_el - min_el + 1
 count_arr = [0]*no_elem_count_arr

 for num in arr:
   count_arr[num - min_el] += 1
  for i in range(1, no_elem_count_arr):
   count_arr[i] += count_arr[i-1]

 results = [0]*len(arr)
 for i in range(len(arr) -1, -1, -1):
   num_idx_in_count = arr[i] - min_el
   count_arr[num_idx_in_count] -= 1
   results[count_arr[num_idx_in_count]] = arr[i]
 return results

print(count_sort_generic([8,2,3,5,3,7,3,7, 100, 100, 99,98,98]))

print(count_sort_generic([-8,2,-3,-5,3,7,3,7, 100, 100, 99,98,98]))

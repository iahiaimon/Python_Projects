def selection(nums):
    n = len(nums)
    for i in range (n-1):
        min_item = 100
        min_index = -1
        for j in range (i , n):
            if nums[j] < min_item :
                min_item = nums[j]
                min_index = j
        nums[min_index] = nums[i]
        nums[i] = min_item

list = [4 , 6 , 2 , 10 , 5 , 11 , 8]
print(f"Before Shorting {list}")

selection(list)
print(f"After Sorting {list}")
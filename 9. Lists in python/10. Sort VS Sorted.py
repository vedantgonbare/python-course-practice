

nums = [4, 7, 3, 8, 1, 1, 2, 10, 9, 6, 9, 1, 1, 1] 

# Sort VS Sorted

new_list = sorted(nums)                         #It returns value
print(f"new_list = {new_list}", id(new_list))

print(f"nums = {nums}", id(nums))

nums.sort()                                      # IT doesnt return
print(f"nums = {nums}", id(nums))                # In place sorting 

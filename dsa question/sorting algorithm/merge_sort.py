'''
## Merge Sort

**Theory:**
Merge Sort is a **Divide and Conquer** sorting algorithm.

It works in 3 steps:

**Divide → Sort → Merge**

genui{"learning_viz":{"type_id":"MERGE_SORT"}}

### Working

Take:

```text
[5, 3, 8, 1, 2, 7]
```

**1. Divide** the array into smaller parts:

```text
[5, 3, 8]    [1, 2, 7]

[5] [3, 8]   [1] [2, 7]

[5] [3] [8]  [1] [2] [7]
```

**2. Merge** the small parts in sorted order:

```text
[3] + [8] → [3, 8]

[5] + [3, 8] → [3, 5, 8]

[2] + [7] → [2, 7]

[1] + [2, 7] → [1, 2, 7]
```

**3. Final merge:**

```text
[3, 5, 8] + [1, 2, 7]

→ [1, 2, 3, 5, 7, 8]
```

### Complexity

* **Best:** `O(n log n)`
* **Average:** `O(n log n)`
* **Worst:** `O(n log n)`
* **Space:** `O(n)`

'''

def merge_sort(nums):
    
    length=len(nums)
    #checking the if the length is 1 or 0 then sorted
    if length<=1:
        return nums

    mid= len(nums)//2


    #dividing into the two halves
    left=nums[:mid]
    right=nums[mid:]


    #sort both halves
    left=merge_sort(left)
    right=merge_sort(right)



    #return the sorted array

    return merge_array(left,right)


def merge_array(left,right):
    result=[]

    i=0
    j=0

    while i<len(left) and j<len(right):
        if left[i]<right[j]:
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j +=1

    #adding the remaining element
    result.extend(left[i:])
    result.extend(right[j:])


    return result


nums=[4,5,6,2,8,7,6,4,3,98,9,2]

print("before sort ",nums)

result=merge_sort(nums)

print("after sort",result)

        


        


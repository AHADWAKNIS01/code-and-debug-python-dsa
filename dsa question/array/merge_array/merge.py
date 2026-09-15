def merge(nums1,nums2):
    i=0
    j=0
    n=len(nums1)
    m=len(nums2)
    result=[]

    while i<n and j<m:
        if nums1[i]<=nums2[j]:
            if len(result)==0 or result[-1]!=nums1[i]:
                result.append(nums1[i])
            i+=1

        else:
            if len(result)==0 or result[-1]!=nums2[j]:
                result.append(nums2[j])
            j+=1



    while i<n:
        if len(result)==0 or result[-1]!=nums1[i]:
             result.append(nums1[i])
        i+=1


    while j<m:
        if len(result)==0 or result[-1]!=nums2[j]:
            result.append(nums2[j])
        j+=1

    return result

nums1=[1,2,3,6,7,8,9,19,23]
print("your first array is:",nums1)
nums2=[1,2,3,4,5,6,7,8,9,18.45,67]
print("your second array is :",nums2)

merge_result=merge(nums1,nums2)

print("your merge array is:",merge_result)




        
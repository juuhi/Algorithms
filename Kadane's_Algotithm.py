"""Write a program to find the sum of contiguous subarray within a one-dimensional array
of numbers which has the largest sum.
for example : (-2,-3,4,-1,-2,1,4,-3) will give 6 for (4,-1,-2,1,4)"""

def maxSubArraySum(a,size):
    max_so_far = a[0]
    curr_max = a[0]

    for i in range(1,size):
        curr_max = max(a[i],curr_max+a[i])
        max_so_far = max(max_so_far,curr_max)
    return max_so_far

print ("Maximum contiguous sum is" , maxSubArraySum((-2,-3,4,-1,-2,1,4,-3),8))
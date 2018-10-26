"""
find if the list can be partitioned into 2 or not

"""


def subset_exists_with_sum(arr, target_sum):
    # The value of subset[i%2][j] will be true
    # if there exists a subset of sum j in
    # arr[0, 1, ...., i-1]
    subset = [[False for j in range(target_sum + 1)] for i in range(2)]
    n=len(arr)
    for i in range(n + 1):
        for j in range(target_sum + 1):

            if j == 0:
                subset[i % 2][j] = True

            elif i == 0:
                subset[i % 2][j] = False
            elif arr[i - 1] <= j:
                subset[i % 2][j] = subset[(i + 1) % 2][j - arr[i - 1]] or subset[(i + 1)% 2][j]
            else:
                subset[i % 2][j] = subset[(i + 1) % 2][j]
    return subset[n % 2][target_sum]

def partition_by_sum(arr):

    list_total_sum = sum(arr)
    if list_total_sum%2 ==1:
        return False
    else:
        return subset_exists_with_sum(arr,int(list_total_sum/2))

print(partition_by_sum([3,7,10]))
print(partition_by_sum([1,2,5,3,8,10]))
print(partition_by_sum([1,2,5,3,107,2,10]))

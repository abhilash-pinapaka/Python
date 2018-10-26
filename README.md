# Python

How to find if a given list can be partitioned into 2 lists with equal sum.

One way of approach if loop through each and every combination and find sum of each combination and match
if sum of any combinations are equal.
order of complexity of this approach is 2^N
this approach is not good if N is a bigger number.

We can minimize the complexity by breaking down the problem as follows:

if the list can be partitioned into two lists of equal sum, then there should be sub list whose sum should be qual to half of the 
sum of the given list.
if sum of the given list is an odd number then list cannot be partitioned
order of complexity will be O(n) in this scenario.

if sum of the given list is even number then we have to find if there exists a sub list whose sum is equal to half of the given list sum.

We can solve this in multiple ways recursive approach , looping through list to find elements whose sum is equal to target sum.

We can solve the problem in Pseudo-polynomial time using Dynamic programming.
We create a boolean 2D table subset[][] and fill it in bottom up manner.
The value of subset[i][j] will be true if there is a subset of set[0..j-1] with sum equal to i.,
otherwise false. Finally, we return subset[sum][n]
 We can minimize the complexity to O(n*k) 
 where k = target sum that is half of the given list sum

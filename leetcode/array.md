+ [Max Consecutive Ones](#max-consecutive-ones)
+ [Reshape the Matrix](#reshape-the-matrix)
+ [Image Smoother](#image-smoother)
+ [Flipping an Image](#flipping-an-image)
+ [Transpose Matrix](#transpose-matrix)
+ [Move Zeroes](#move-zeroes)
+ [Squares of a Sorted Array](#squares-of-a-sorted-array)
<!-----solution----->

## Squares of a Sorted Array

https://leetcode.com/problems/squares-of-a-sorted-array/

```python
def sortedSquares(self, A):
    answer = [0] * len(A)
    l, r = 0, len(A) - 1
    while l <= r:
        left, right = abs(A[l]), abs(A[r])
        if left > right:
            answer[r - l] = left * left
            l += 1
        else:
            answer[r - l] = right * right
            r -= 1
    return answer
```

## Move Zeroes

https://leetcode.com/problems/move-zeroes/

```python
def moveZeroes(self, nums):
    nums1 = [n for n in nums if n != 0]
    nums2 = [0]*nums.count(0)
    nums[:] = nums1 + nums2
```

## Transpose Matrix

https://leetcode.com/problems/transpose-matrix/

```python
def transpose(self, A):
    return [[row[i] for row in A] for i in range(len(A[0]))]
```

## Flipping an Image

https://leetcode.com/problems/flipping-an-image/

```python
def flipAndInvertImage(self, A):
    for lis in A:
        lis.reverse()
        for i in range(len(lis)):
            lis[i] = ~lis[i]+2
    return A
```

## Image Smoother

https://leetcode.com/problems/image-smoother/

```python
import math
class Solution:
def imageSmoother(self, M):
    cell = [[0 for i in range(len(M[0]))] for j in range(len(M))]
    for r in range(len(M)):
        for c in range(len(M[0])):
            total = 0
            count = 0
            for i in range(r-1, r+2):
                for j in range(c-1, c+2):
                    if(i >= 0 and i < len(M) and j >= 0 and j < len(M[0])):
                        count += 1
                        total += M[i][j]
            cell[r][c] = math.floor(total/count)
    return cell
```

## Reshape the Matrix

https://leetcode.com/problems/reshape-the-matrix/

```python
def matrixReshape(self, nums, r, c):
    if r*c != len(nums)*len(nums[0]):
        return nums
    nums_flat = []
    re = []
    for i in range(len(nums)):
        nums_flat += nums[i]
    for i in range(0, r*c, c):
        re.append(nums_flat[i:i+c])
    return re
```

## Max Consecutive Ones

https://leetcode.com/problems/max-consecutive-ones/

```python
def findMaxConsecutiveOnes(self, nums):
    return len(max("".join(map(str, nums)).split("0")))
```

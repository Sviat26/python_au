+ [House Robber II](#house-robber-ii)
+ [House Robber](#house-robber)
<!-----solution----->

## House Robber

https://leetcode.com/problems/house-robber/

```python
def rob(self, nums: List[int]) -> int:
    cur = pre=0
    for i in nums:
        _ = pre
        pre = cur
        cur = max(i+_, pre)
    return cur
```

## House Robber II

https://leetcode.com/problems/house-robber-ii/

```python
def rob(self, nums):
    if not nums: return 0
    res = [0,0]
    res[0] = nums[0] + self.helper(nums[1:-1])[1]
    res[1] = max(self.helper(nums[1:]))
    return max(res)
def helper(self, nums):
    if not nums: return [0,0]
    curr = self.helper(nums[1:])
    return [nums[0]+curr[1], max(curr)]
```
+ [Non-overlapping Intervals](#non-overlapping-intervals)
+ [Merge Intervals](#merge-intervals)
+ [Insert Interval](#insert-interval)
<!-----solution----->

## Insert Interval

https://leetcode.com/problems/insert-interval/

```python
def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
    intervals.append(newInterval)
    intervals.sort()
    ans = [intervals[0]]
    for i in range(1, len(intervals)):
        if intervals[i][0] > ans[-1][1]:
            ans.append(intervals[i])
        elif intervals[i][1] > ans[-1][1]:
            ans[-1][1] = intervals[i][1]
    return ans
```

## Merge Intervals

https://leetcode.com/problems/merge-intervals/

```python
def merge(self, intervals: List[List[int]]) -> List[List[int]]:
    intervals = sorted(intervals, key=lambda x: x[0])
    ret = []
    for i in intervals:
        newInterval = i
        if ret:
            if ret[-1][1] >= i[0]:
                newInterval = ret.pop()
                if i[1] > newInterval[1]:
                    newInterval[1] = i[1]
        ret.append(newInterval)
    return ret
```

## Non-overlapping Intervals

https://leetcode.com/problems/non-overlapping-intervals/

```python
def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
    if len(intervals) == 0:
        return 0
    intervals.sort()
    start = intervals[0][0]
    end = intervals[0][1]
    res = 0
    for i in range(1, len(intervals)):
        end = min(end, intervals[i][1])
        if end > intervals[i][0]:
            res += 1
        else:
            end = intervals[i][1]
    return res
```
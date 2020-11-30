+ [Reverse Integer](#reverse-integer)
+ [Palindrome Number](#palindrome-number)
+ [Base 7](#base-7)
+ [Fizz Buzz](#fizz-buzz)
+ [Fibonacci Number](#fibonacci-number)
+ [Largest Perimeter Triangle](#largest-perimeter-triangle)
+ [Sqrt(x)](#sqrtx)
<!-----solution----->

## Sqrt(x)

https://leetcode.com/problems/sqrtx/

```python
def mySqrt(self, x):
    if x <= 1:
        return x
    low, high = 1, x
    while low <= high:
        mid = (low + high)//2
        mid2 = mid**2
        if mid2 == x:
            return mid
        elif mid2 < x:
            low = mid + 1
        elif mid2 > x:
            high = mid - 1
    return high
```

## Largest Perimeter Triangle

https://leetcode.com/problems/largest-perimeter-triangle/

```python
def largestPerimeter(self, A):
    A.sort(reverse=True)
    for i in range(len(A) - 2):
        if A[i+1] + A[i+2] > A[i]:
            return A[i] + A[i+1] + A[i+2]
    return 0
```

## Fibonacci Number

https://leetcode.com/problems/fibonacci-number/

```python
def fib(self, N):
    phi = (1+5**0.5)/2
    return int((phi**N-(-phi)**-N)/(5**0.5))
```

## Fizz Buzz

https://leetcode.com/problems/fizz-buzz/

```python
def fizzBuzz(self, n: int) -> List[str]:
    return ['Fizz' * (not i % 3) + 'Buzz' * (not i % 5) or str(i) for i in range(1, n+1)]
```

## Base 7

https://leetcode.com/problems/base-7/

```python
def convertToBase7(self, num: int) -> str:
    if num == 0:
        return '0'
    is_negative = False
    if num < 0:
        is_negative = True
        num = -num
    ans = ''
    while num:
        quotient = num//7
        remain = num % 7
        ans = str(remain)+ans
        num = quotient
    return '-'+ans if is_negative else ans
```

## Palindrome Number

https://leetcode.com/problems/palindrome-number/

```python
def isPalindrome(self, x: int) -> bool:
    if x < 0:
        return False
    reverse = 0
    original = x
    while x > 0:
        reverse = reverse * 10 + x % 10
        x = x // 10
    return reverse == original
```

## Reverse Integer

https://leetcode.com/problems/reverse-integer/

```python
def reverse(self, x):          
    reversed = (-1 if x < 0 else 1) * int(str(x)[::-1].replace("-", ""))
    if reversed > pow(2, 31) - 1 or reversed < -1 * pow(2, 31):
        return 0
    return reversed
```

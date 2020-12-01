+ [Valid Anagram](#valid-anagram)
+ [Reverse string](#reverse-string)
+ [Reverse Vowels of a String](#reverse-vowels-of-a-string)
+ [Reverse Words in a String III](#reverse-words-in-a-string-iii)
+ [To Lower Case](#to-lower-case)
<!-----solution----->

## To Lower Case

https://leetcode.com/problems/to-lower-case/

```python
def toLowerCase(self, str):
        str = str.lower()
        return str
```

## Reverse Words in a String III

https://leetcode.com/problems/reverse-words-in-a-string-iii/

```python
def reverseWords(self, s):
    return " ".join(word[::-1] for word in s.split(" "))
```

## Reverse Vowels of a String

https://leetcode.com/problems/reverse-vowels-of-a-string/

```python
def reverseVowels(self, s: str) -> str:
    if s == "":
        return ""
    listy = ['a', 'o', 'e', 'i', 'u', 'A', 'O', 'E', 'I', 'U']
    queue = []
    temp_index = []
    for i in range(len(s)):
        if s[i] in listy:
            queue.append(s[i])
            temp_index.append(i)
    queue.reverse()
    j = 0
    s = list(s)
    for i in temp_index:
        s[i] = queue[j]
        j += 1
    s = "".join(s)
    return s
```

## Reverse string

https://leetcode.com/problems/reverse-string/

```python
def reverseString(self, s: List[str]) -> None:
    s.reverse()
```

## Valid Anagram

https://leetcode.com/problems/valid-anagram/

```python
def isAnagram(self, s, t):
    import collections
    return collections.Counter(s) == collections.Counter(t)

def isAnagram2(self, s, t):
    return sorted(s) == sorted(t)
```

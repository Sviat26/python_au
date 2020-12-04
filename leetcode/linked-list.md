+ [Reverse Linked List](#reverse-linked-list)
+ [Middle of the Linked List](#middle-of-the-linked-list)
+ [Palindrome Linked List](#palindrome-linked-list)
+ [Merge Two Sorted Lists](#merge-two-sorted-lists)
+ [Remove Nth Node From End of List](#remove-nth-node-from-end-of-list)
+ [Linked List Cycle II](#linked-list-cycle-ii)
+ [Linked List Cycle](#linked-list-cycle)
+ [Reorder List](#reorder-list)
+ [Intersection of Two Linked Lists](#intersection-of-two-linked-lists)
+ [Sort List](#sort-list)
<!-----solution----->

## Sort List

https://leetcode.com/problems/sort-list/

```python
def sortList(self, head):
    res = []
    while head:
        res.append(head.val)
        head = head.next
    res.sort()
    p = ListNode(0)
    s = p
    for r in res:
        p.next = ListNode(r)
        p = p.next
    return s.next
```

## Intersection of Two Linked Lists

https://leetcode.com/problems/intersection-of-two-linked-lists/

```python
def getIntersectionNode(self, headA, headB):
    len_a, len_b = self.getLength(headA), self.getLength(headB)
    if len_a > len_b:
        for i in range(len_a - len_b):
            headA = headA.next
    else:
        for i in range(len_b - len_a):
            headB = headB.next
    while headA and headB:
        if headA == headB:
            return headA
        headA = headA.next
        headB = headB.next
    return None
def getLength(self, head):
    l = 0
    while head:
        l += 1
        head = head.next
    return l
```

## Reorder List

https://leetcode.com/problems/reorder-list/

```python
def reorderList(self, head):
    if not head:
        return
    ltmp = []
    cur = head
    while cur:
        ltmp.append(cur)
        cur = cur.next
    n = len(ltmp)
    for i in range(n // 2):
        ltmp[i].next = ltmp[n - 1 - i]
        ltmp[n - 1 - i].next = ltmp[i + 1]
    ltmp[n // 2].next = None
```

## Linked List Cycle

https://leetcode.com/problems/linked-list-cycle/

```python
def hasCycle(self, head):
    seen = []
    while head:
        if head in seen:
            return True
        else:
            seen.append(head)
            head = head.next
    return False
```

## Linked List Cycle II

https://leetcode.com/problems/linked-list-cycle-ii/

```python
def detectCycle(self, head):
    if head is None or head.next is None:
        return None
    slow = fast = head
    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next
        if fast == slow:
            break
    if slow == fast:
        slow = head
        while slow != fast:
            slow = slow.next
            fast = fast.next
        return slow
    return None
```

## Remove Nth Node From End of List

https://leetcode.com/problems/remove-nth-node-from-end-of-list/

```python
def removeNthFromEnd(self, head, n):
    r = head
    for i in range(n):
        r = r.next
    if(r is None):
        return head.next
    l = head
    while(r.next is not None):
        r = r.next
        l = l.next
    x = l.next
    l.next = x.next
    return head
```

## Merge Two Sorted Lists

https://leetcode.com/problems/merge-two-sorted-lists/

```python
def mergeTwoLists(self, l1, l2):
    if l1 is None:
        return l2
    if l2 is None:
        return l1
    result = ListNode(0)
    l = result
    while 1:
        if l1.val <= l2.val:
            l.next = l1
            l1 = l1.next
            if l1 is None:
                break
        else:
            l.next = l2
            l2 = l2.next
            if l2 is None:
                break
        l = l.next
    l.next.next = l1 or l2
    return result.next
```

## Palindrome Linked List

https://leetcode.com/problems/palindrome-linked-list/

```python
def isPalindrome(self, head):
    if head is None or head.next is None:
        return True
    l = []
    p = head
    while p.next:
        l.append(p.val)
        p = p.next
    l.append(p.val)
    return l == l[::-1]
```

## Middle of the Linked List

https://leetcode.com/problems/middle-of-the-linked-list/

```python
def middleNode(self, head: ListNode) -> ListNode:
    length = 0
    count = head
    while count:
        length += 1
        count = count.next
    length = math.ceil(length/2)
    pre = post = head
    for _ in range(length):
        pre = pre.next
    while pre:
        pre = pre.next
        post = post.next
    return post
```

## Reverse Linked List

https://leetcode.com/problems/reverse-linked-list/

```python
def reverseList(self, head):
    p = None
    while head:
        tmp = head
        head = head.next
        tmp.next = p
        p = tmp
    return p
```
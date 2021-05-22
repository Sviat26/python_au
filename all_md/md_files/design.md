+ [Min Stack](#min-stack)
+ [Implement Queue using Stacks](#implement-queue-using-stacks)
+ [Implement Stack using Queues](#implement-stack-using-queues)
+ [Design Twitter](#design-twitter)
<!-----solution----->

## Design Twitter

https://leetcode.com/problems/design-twitter/

```python

def __init__(self):
    """
    Initialize your data structure here.
    """
    self.user_warehouse = {}
    self.twitter_warehouse = {}
    self.tweet_timeline = []
    

def postTweet(self, userId: int, tweetId: int) -> None:
    """
    Compose a new tweet.
    """
    if userId in self.twitter_warehouse:
        self.twitter_warehouse[userId].append(tweetId)
    else:
        self.twitter_warehouse[userId] = [tweetId]
    if userId not in self.user_warehouse:
        self.user_warehouse[userId] = []
    self.tweet_timeline.append(tweetId)

    

def getNewsFeed(self, userId: int) -> List[int]:
    """
    Retrieve the 10 most recent tweet ids in the user's news feed. Each item in the news feed must be posted by users who the user followed or by the user herself. Tweets must be ordered from most recent to least recent.
    """
    if userId not in self.twitter_warehouse:
        return []
    followee_ids = self.user_warehouse[userId]
    all_tweets = [each_tweet for user_id in followee_ids for each_tweet in self.twitter_warehouse[user_id] ]
    all_tweets += self.twitter_warehouse[userId]
    
    cnt = 0
    ret_tweets = []

    for each_tweet in self.tweet_timeline[::-1]:
        if each_tweet in all_tweets:
            ret_tweets.append(each_tweet)
            cnt += 1
        if cnt == 10:
            break
    return ret_tweets

    

def follow(self, followerId: int, followeeId: int) -> None:
    """
    Follower follows a followee. If the operation is invalid, it should be a no-op.
    """
    if followerId == followeeId:
        return
    if followerId in self.user_warehouse:
        self.user_warehouse[followerId].append(followeeId)
    else:
        self.user_warehouse[followerId] = [followeeId]
    if followerId not in self.twitter_warehouse:
        self.twitter_warehouse[followerId] = []
    if followeeId not in self.twitter_warehouse:
        self.twitter_warehouse[followeeId] = []

    

def unfollow(self, followerId: int, followeeId: int) -> None:
    """
    Follower unfollows a followee. If the operation is invalid, it should be a no-op.
    """
    if followerId in self.user_warehouse and followeeId in self.user_warehouse[followerId]:
        self.user_warehouse[followerId].remove(followeeId)
    

ur Twitter object will be instantiated and called as such:
j = Twitter()
j.postTweet(userId,tweetId)
ram_2 = obj.getNewsFeed(userId)
j.follow(followerId,followeeId)
j.unfollow(followerId,followeeId)
```

## Implement Stack using Queues

https://leetcode.com/problems/implement-stack-using-queues/

```python

def __init__(self):
    """
    Initialize your data structure here.
    """
    self.queue=collections.deque()
def push(self, x: int) -> None:
    """
    Push element x onto stack.
    """
    temp=[]
    while self.queue:
        temp.append(self.queue.popleft())
    self.queue.append(x)
    for item in temp:
        self.queue.append(item)
        
def pop(self) -> int:
    """
    Removes the element on top of the stack and returns that element.
    """
    return self.queue.popleft()

def top(self) -> int:
    """
    Get the top element.
    """
    return self.queue[0]

def empty(self) -> bool:
    """
    Returns whether the stack is empty.
    """
    return len(self.queue)==0
```

## Implement Queue using Stacks

https://leetcode.com/problems/implement-queue-using-stacks/

```python
def __init__(self):
    self.a = []
    self.b = [] 

def push(self, x):
    self.a.append(x)
    
def pop(self):
    if len(self.b) != 0: 
        return self.b.pop()
    else:
        while len(self.a) != 0:
            self.b.append(self.a.pop())
        return self.b.pop()  

def peek(self):
    if len(self.b) != 0: 
        return self.b[-1]
    else:
        while len(self.a) != 0:
            self.b.append(self.a.pop())
        return self.b[-1]

def empty(self):
    return len(self.a) == 0 and len(self.b) == 0
```

## Min Stack

https://leetcode.com/problems/min-stack/

```python
def __init__(self):
    self.value=[]
    self.stackmin=[]
def push(self, x: int) -> None:  
    self.value.append(x)
    if self.stackmin and self.stackmin[-1]<x:
        self.stackmin.append(self.stackmin[-1])
    else:
        self.stackmin.append(x)
        
def pop(self) -> None:
    self.value.pop()
    self.stackmin.pop()
    
def top(self) -> int:
    return self.value[-1]

def getMin(self) -> int:
    return self.stackmin[-1]
```
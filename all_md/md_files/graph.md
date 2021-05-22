+ [Course Schedule II](#course-schedule-ii)
+ [Number of Islands](#number-of-islands)
+ [Is Graph Bipartite?](#is-graph-bipartite)
+ [Cheapest Flights Within K Stops](#cheapest-flights-within-k-stops)
+ [Shortest Path in Binary Matrix](#shortest-path-in-binary-matrix)
+ [Maximum Depth of N-ary Tree](#maximum-depth-of-n-ary-tree)
<!-----solution----->

## Maximum Depth of N-ary Tree

https://leetcode.com/problems/maximum-depth-of-n-ary-tree/

```python
def maxDepth(self, root):
    if not root:
        return 0
    elif not root.children:
        return 1
    else:
        return 1+max(map(self.maxDepth,root.children))
```

## Shortest Path in Binary Matrix

https://leetcode.com/problems/shortest-path-in-binary-matrix/

```python
def shortestPathBinaryMatrix(self, grid: List[List[int]]) -> int:
    if grid[0][0] == 1 or grid[-1][-1] == 1:  
        return -1
    directions = [[1, 0], [-1, 0], [0, -1], [0, 1], [1, 1], [1, -1], [-1, 1], [-1, -1]]
    queue = [(0, 0, 1)] 
    n = len(grid)
    while len(queue):
        x0, y0, cnt = queue.pop(0)  
        if x0 == n - 1 and y0 == n - 1:  
            return cnt
        for i, j in directions:
            x, y = x0 + i, y0 + j
            if 0 <= x < n and 0 <= y < n and not grid[x][y]:
                queue.append((x, y, cnt + 1))
                grid[x][y] = 1
    return -1
```

## Cheapest Flights Within K Stops

https://leetcode.com/problems/cheapest-flights-within-k-stops/

```python
def findCheapestPrice(self, n, flights, src, dst, K):
    import collections
    flights_dict = collections.defaultdict(list)
    for flight in flights:
        flights_dict[flight[0]].append(flight[1:])
    memory = {}
    def dfs(K, src, price):
        if (src, K) in memory:
            return memory[(src, K)]
        if K < 0:
            memory[(src, K)] = float('inf')
            return float('inf')
        min_price = float('inf')
        for next_src in flights_dict[src]:
            price += next_src[1]
            if next_src[0] == dst:
                a = price
            else:
                a = dfs(K - 1, next_src[0], 0) + price
            min_price = min(a, min_price)
            price -= next_src[1]
        memory[(src, K)] = min_price
        return memory[(src, K)]
    ans = dfs(K, src, 0)
    return ans if ans != float('inf') else -1
```

## Is Graph Bipartite?

https://leetcode.com/problems/is-graph-bipartite/

```python
def isBipartite(self, graph):
    subsets_A = set()
    subsets_B = set()
    used = set()
    for i in range(len(graph)):
        if i not in used:
            subsets_A.add(i)
            cur_list = [i]
            count = 0
            while cur_list:
                next_list = []
                for j in cur_list:
                    used.add(j)
                    for opposite in graph[j]:                          
                        if count % 2 == 0:
                            if opposite in subsets_A:
                                return False
                            subsets_B.add(opposite)
                        else:
                            if opposite in subsets_B:
                                return False
                            subsets_A.add(opposite)
                        if opposite not in used:
                            next_list.append(opposite)
                count += 1
                cur_list = next_list
    return True
```

## Number of Islands

https://leetcode.com/problems/number-of-islands/

```python
def numIslands(self, grid):
    self.row_num = len(grid)
    if self.row_num == 0:
        return 0
    self.column_num = len(grid[0])
    self.visited = [[False for _ in range(self.column_num)] for _ in range(self.row_num)]
    islands = []
    for r in range(self.row_num):
        for c in range(self.column_num):
            if not self.visited[r][c] and grid[r][c] == '1':
                island = []
                self.visit(grid,r,c,island)
                islands.append(island)
    return len(islands)
def visit(self,grid,row,column,island):
    if not self.visited[row][column] and  grid[row][column] == '1':
        self.visited[row][column] = True
        island.append((row,column))
        if row - 1 >= 0:
            self.visit(grid,row-1,column,island)
        if row + 1 < self.row_num:
            self.visit(grid,row+1,column,island)
        if column - 1 >= 0:
            self.visit(grid,row,column-1,island)
        if column + 1 < self.column_num:
            self.visit(grid,row,column+1,island)
```

## Course Schedule II

https://leetcode.com/problems/course-schedule-ii/

```python
def findOrder(self, numCourses, prerequisites):
    res=[]
    graph_in, graph_out=collections.defaultdict(set), collections.defaultdict(set)
    for x,y in prerequisites:
        graph_in[x].add(y)
        graph_out[y].add(x)
    s=set([i for i in range(numCourses) if i not in graph_in])
    while s:
        n=s.pop()
        res.append(n)
        for m in graph_out[n]:
            graph_in[m].discard(n)
            if not graph_in[m]:
                del graph_in[m]
                s.add(m)
    if graph_in:
        return []
    return res
```
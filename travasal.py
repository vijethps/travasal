from collections import deque,defaultdict

class Graph:
    def __init__(self):
        self.graph = defaultdict(list)

    def add_edge(self,u,v):
        self.graph[u].append(v)
        self.graph[v].append(u)

    def bfs(self,start_node):
        queue = deque([start_node])
        visited = set()
        bfs_order = []
        while queue:
            node = queue.popleft()
            if node not in visited:
                visited.add(node)
                bfs_order.append(node)

            for neighbor in self.graph[node]:
                if neighbor not in visited:

                    queue.append(neighbor)
        return bfs_order
if __name__ == "__main__":
    g=Graph()
    V = int(input())
    for _ in range(V-1):
        u,v = map(int,input().split())
        g.add_edge(u,v)
    start_node = int(input())
    result = g.bfs(start_node)
    print(" ".join(map(str,result))) 

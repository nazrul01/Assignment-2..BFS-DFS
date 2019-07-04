from collections import defaultdict


class graph:
    def __init__(self):
        self.graph = defaultdict(list)

    def add_edge(self, u, v):
        self.graph[u].append(v)
        self.graph[v].append(u)

    def DFS(self, s):
        stack = []
        visited = [False for i in range(len(self.graph))]
        visited[s] = True
        stack.append(s);
        while stack:
            source = stack.pop()
            print(source, end=' ')
            for j in self.graph[source]:
                if visited[j] == False:
                    stack.append(j);
                    visited[j] = True


g = graph()
g.add_edge(0, 1)
g.add_edge(0, 2)
g.add_edge(1, 3)
g.add_edge(2, 3)
g.add_edge(3, 4)
g.add_edge(4, 5)
print("\n\n\nThe DFS traversal of the Graph is:\n\n")
g.DFS(1)
print("\n\n")
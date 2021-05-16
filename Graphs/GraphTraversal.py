class Graph:
    def __init__(self, edges):
        self.edges = edges
        self.graph_dict = {}
        for start, end in self.edges:
            if start in self.graph_dict:
                self.graph_dict[start].append(end)
            else:
                self.graph_dict[start] = [end]

        print('Graph dictionary', self.graph_dict)

    def dfs(self, start, visited=set()):
        visited.add(start)
        print(start,end=' ')
        if start not in self.graph_dict:
            return
        for next in self.graph_dict[start]:
            if next not in visited:
                self.dfs(next, visited)
        return

    def cycle_in_dfs(self,start,parent=-1,visited=set()):
        visited.add(start)
        if start not in self.graph_dict:
            return False

        for next in self.graph_dict[start]:
            if not next in visited:
                if self.cycle_in_dfs(next, start,visited):
                    return True
            elif next!=parent:
                return True
        return False

    def bfs(self,start):
        visited = set()
        queue=[]
        queue.append(start)
        visited.add(start)
        while queue:
            s=queue.pop(0)
            print(s,end=" ")
            if s not in self.graph_dict:
                continue
            for i in self.graph_dict[s]:
                if not i in visited:
                    queue.append(i)
                    visited.add(i)


if __name__ == "__main__":

    edges=[
        (1, 2), (1, 7), (1, 8), (2, 3), (2, 6), (3, 4),
        (3, 5), (8, 9), (8, 12), (9, 10), (9, 11)
    ]
    graph = Graph(edges)
    graph.dfs(1)
    print()

    if graph.cycle_in_dfs(1):
        print('Cycle detected in graph')
    else:
        print('No cycle detected')
    graph.bfs(1)
    print()

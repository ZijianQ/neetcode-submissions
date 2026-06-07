class Graph:
    
    def __init__(self):
        self.adj_list = {}


    def addEdge(self, src: int, dst: int) -> None:
        if src not in self.adj_list:
            self.adj_list[src] = set()

        self.adj_list[src].add(dst)


    def removeEdge(self, src: int, dst: int) -> bool:
        if src not in self.adj_list or dst not in self.adj_list[src]:
            return False
        # Remove the edge
        self.adj_list[src].remove(dst)
        return True

    def dfs(self, src:int, dst:int, visited:set) -> bool:
        if src ==dst : return True
        visited.add(src)
        for neighbor in self.adj_list.get(src, []):
            if neighbor not in visited:
                if self.dfs(neighbor, dst, visited):
                    return True
        return False



    def hasPath(self, src: int, dst: int) -> bool:
        visited = set()
        return self.dfs(src, dst, visited)



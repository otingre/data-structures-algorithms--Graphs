class Graph:
    def __init__(self, egdes):
        self.graph_dict = {}
        self.edges = egdes
        for start, end in self.edges:
            if start in self.graph_dict:
                self.graph_dict[start].append(end)
            else:
                self.graph_dict[start] = [end]
        print(self.graph_dict)

    def find_path(self, start, end, path=[]):
        path = path + [start]
        
        if start == end:
            return [path]
        
        if start not in self.graph_dict:
            return []

        paths = []

        for node in self.graph_dict[start]:
            if node not in path:
                new_paths = self.find_path(node, end, path)
                for p in new_paths:
                    paths.append(p)
        
        return paths

    
    def get_shortest_path(self, start, end, path=[]):
        path = path + [start]

        if start == end:
            return path

        if start not in self.graph_dict:
            return None

        shortest_path = None

        for node in self.graph_dict[start]:
            if node not in path:
                sp = self.get_shortest_path(node, end, path) 
                if sp:
                    if shortest_path is None or len(sp) < len(shortest_path):
                        shortest_path = sp
        return shortest_path

if __name__ == '__main__' :

    routes = [
        ("Mumbai", "Paris"),
        ("Mumbai", "Dubai"),
        ("Paris", "Dubai"),
        ("Paris", "New York"),
        ("Dubai", "New York"),
        ("New York", "Toronto"),
    ]


    graph_routes = Graph(routes)

    start = "Mumbai"
    end = "New York"

    print(f"All paths between: {start} and {end}: ",graph_routes.find_path(start,end))
    print(f"Shortest path between {start} and {end}: ", graph_routes.get_shortest_path(start,end))

    start = "Paris"
    end = "New York"

    print(f"All paths between: {start} and {end}: ",graph_routes.find_path(start,end))
    print(f"Shortest path between {start} and {end}: ", graph_routes.get_shortest_path(start,end))

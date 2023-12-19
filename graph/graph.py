class Graph:
    def __init__(self):
        self.graph = {}

    def add_vertex(self, vertex):
        if vertex not in self.graph:
            self.graph[vertex] = []

    def add_edge(self, source, destination):
        if source in self.graph and destination in self.graph:
            self.graph[source].append(destination)
            self.graph[destination].append(source)

    def remove_vertex(self, vertex):
        if vertex in self.graph:
            for v in self.graph[vertex]:
                self.graph[v].remove(vertex)
            del self.graph[vertex]

    def remove_edge(self, source, destination):
        if source in self.graph and destination in self.graph:
            self.graph[source].remove(destination)
            self.graph[destination].remove(source)

    def get_vertices(self):
        return list(self.graph.keys())

    def get_edges(self):
        edges = []
        for vertex in self.graph:
            for neighbor in self.graph[vertex]:
                edges.append((vertex, neighbor))
        return edges


graph = Graph()


graph.add_vertex('A')
graph.add_vertex('B')
graph.add_vertex('C')
graph.add_vertex('D')


graph.add_edge('A', 'B')
graph.add_edge('B', 'C')
graph.add_edge('C', 'D')
graph.add_edge('D', 'A')


graph.remove_vertex('D')
graph.remove_edge('A', 'B')


vertices = graph.get_vertices()
edges = graph.get_edges()

print("Vertices:", vertices)
print("Edges:", edges)
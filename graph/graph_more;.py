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
            del self.graph[vertex]
            for v in self.graph:
                self.graph[v] = [vtx for vtx in self.graph[v] if vtx != vertex]

    def remove_edge(self, source, destination):
        if source in self.graph and destination in self.graph:
            self.graph[source] = [vtx for vtx in self.graph[source] if vtx != destination]
            self.graph[destination] = [vtx for vtx in self.graph[destination] if vtx != source]

    def get_vertices(self):
        return list(self.graph.keys())

    def get_edges(self):
        edges = []
        for vertex in self.graph:
            for neighbor in self.graph[vertex]:
                if (neighbor, vertex) not in edges:
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
graph.add_edge('A', 'C')


graph.remove_vertex('D')
graph.remove_edge('A', 'B')


vertices = graph.get_vertices()
edges = graph.get_edges()

print("Vertices:", vertices)
print("Edges:", edges)
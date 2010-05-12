class Graph:
    """
    A class representing a weighted graph.
    - Undirected graph, so edges are two-way.
    - Vertices can exist without any edges connecting to them.
    - Multiple edges between a pair of vertices are disallowed.
    - Self connections are disallowed.
    """
    def __init__(self):
        self.connections = {} # vertex -> {connected vertices}
        self.weights = {} # {v1, v2} -> weight

    @property
    def vertices(self):
        return set(self.connections.keys())

    def add_vertex(self, vertex):
        self.connections.setdefault(vertex, set())

    def remove_vertex(self, vertex):
        # Remove from all referring connections entries.
        for neighbor in self.connections[vertex]:
            self.remove_edge(vertex, neighbor)
        del self.connections[vertex]

    def add_edge(self, a, b, weight):
        self.connections.setdefault(a, set()).add(b)
        self.connections.setdefault(b, set()).add(a)
        self.weights[frozenset((a, b))] = weight

    def remove_edge(self, a, b):
        self.connections[a].remove(b)
        self.connections[b].remove(a)
        self.weights.pop(frozenset((a, b)))

    @classmethod
    def from_dict(cls, data_dict):
        """
        >>> Graph.from_dict({0: {1: 9}}).vertices == {0, 1} # Two connected.
        True
        >>> Graph.from_dict({0: {}, 1: {}}).vertices == {0, 1} # Two disjoint.
        True
        >>> Graph.from_dict({0: {}}).vertices == {0} # One vertex, no connections
        True
        >>> Graph.from_dict({}).vertices == set() # Empty graph
        True
        """
        graph = cls()
        for a, connections in data_dict.items():
            graph.add_vertex(a)
            for b, weight in connections.items():
                graph.add_edge(a, b, weight)
        return graph

    @classmethod
    def from_csv(cls, s):
        """
        Parse a graph from a csv weight matrix.

        >>> Graph.from_csv('-,1\\n1,-').connections == {0: {1}, 1: {0}}
        True
        """
        graph = cls()
        for a, line in enumerate(s.strip().split('\n')):
            for b, cell in enumerate(line.strip().split(',')):
                try:
                    weight = int(cell)
                except ValueError:
                    continue
                graph.add_edge(a, b, weight)
        return graph

    def is_connected(self):
        """
        >>> Graph.from_dict({0: {1: 9}}).is_connected() # Two connected.
        True
        >>> Graph.from_dict({0: {}, 1: {}}).is_connected() # Two disjoint.
        False
        >>> Graph.from_dict({0: {}}).is_connected() # One vertex, no connections
        True
        >>> Graph.from_dict({}).is_connected() # Empty graph
        True
        """
        if not self.vertices:
            return True

        visited = set()
        def dfs(vertex):
            if vertex in visited:
                return
            visited.add(vertex)
            connections = self.connections.get(vertex)
            if not connections:
                return
            for neighbor in connections:
                dfs(neighbor)

        first = next(iter(self.vertices))
        dfs(first)

        return visited == self.vertices

    def calc_weight(self):
        return sum(self.weights.values())

    def minimum_connected(self):
        edges_by_weight = [
            ((a, b), weight)
            for (a, b), weight in self.weights.items()
        ]
        edges_by_weight.sort(key=lambda i: i[1], reverse=True)
        for (a, b), weight in edges_by_weight:
            self.remove_edge(a, b)
            if not self.is_connected():
                self.add_edge(a, b, weight)

if __name__ == '__main__':
    with open('data/network.txt') as f:
        network_string = f.read()
    network = Graph.from_csv(network_string)
    before = network.calc_weight()
    network.minimum_connected()
    after = network.calc_weight()
    print(before - after)

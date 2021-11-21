from collections import defaultdict
from queue import PriorityQueue

class Graph:
    def __init__(self, num_of_vertices):
        self.v = num_of_vertices
        self.edges = [[-1 for i in range(num_of_vertices)] for j in range(num_of_vertices)]
        self.visited = []

    def add_edge(self, u, v, weight):
        self.edges[u][v] = weight
        self.edges[v][u] = weight

    def dijkstra(self, start_vertex):
        D = {v:float('inf') for v in range(self.v)}
        D[start_vertex] = 0

        pq = PriorityQueue()
        pq.put((0, start_vertex))

        while not pq.empty():
            (dist, current_vertex) = pq.get()
            self.visited.append(current_vertex)

            for neighbor in range(self.v):
                if self.edges[current_vertex][neighbor] != -1:
                    distance = self.edges[current_vertex][neighbor]
                    if neighbor not in self.visited:
                        old_cost = D[neighbor]
                        new_cost = D[current_vertex] + distance
                        if new_cost < old_cost:
                            pq.put((new_cost, neighbor))
                            D[neighbor] = new_cost
        return D


g = Graph(28)
g.add_edge(0,1,5)
g.add_edge(0,7,3)
g.add_edge(1,0,5)
g.add_edge(1,2,1)
g.add_edge(1,4,1)
g.add_edge(2,1,1)
g.add_edge(2,3,1)
g.add_edge(2,4,1)
g.add_edge(3,2,1)
g.add_edge(3,5,2)
g.add_edge(4,2,1)
g.add_edge(4,1,1)
g.add_edge(4,5,1)
g.add_edge(4,8,1)
g.add_edge(5,4,2)
g.add_edge(5,3,2)
g.add_edge(5,12,1)
g.add_edge(5,6,2)
g.add_edge(6,5,2)
g.add_edge(6,16,1)
g.add_edge(6,22,2)
g.add_edge(7,0,3)
g.add_edge(7,10,6)
g.add_edge(7,18,4)
g.add_edge(8,4,1)
g.add_edge(8,10,1)
g.add_edge(8,9,1)
g.add_edge(9,8,1)
g.add_edge(9,12,2)
g.add_edge(9,11,1)
g.add_edge(10,8,1)
g.add_edge(10,7,6)
g.add_edge(10,11,1)
g.add_edge(10,13,1)
g.add_edge(11,9,1)
g.add_edge(11,10,1)
g.add_edge(11,14,1)
g.add_edge(11,15,2)
g.add_edge(12,9,2)
g.add_edge(12,5,1)
g.add_edge(12,16,1)
g.add_edge(12,17,1)
g.add_edge(16,12,1)
g.add_edge(16,6,2)
g.add_edge(16,22,5)
g.add_edge(16,17,1)
g.add_edge(13,10,1)
g.add_edge(13,18,5)
g.add_edge(13,14,1)
g.add_edge(13,19,2)
g.add_edge(14,13,1)
g.add_edge(14,11,1)
g.add_edge(14,15,1)
g.add_edge(14,20,2)
g.add_edge(15,11,2)
g.add_edge(15,14,1)
g.add_edge(15,17,1)
g.add_edge(15,20,1)
g.add_edge(17,15,1)
g.add_edge(17,12,1)
g.add_edge(17,16,1)
g.add_edge(17,21,1)
g.add_edge(22,16,5)
g.add_edge(22,6,2)
g.add_edge(22,21,4)
g.add_edge(18,13,5)
g.add_edge(18,7,4)
g.add_edge(18,19,2)
g.add_edge(18,24,2)
g.add_edge(19,18,2)
g.add_edge(19,13,2)
g.add_edge(19,20,1)
g.add_edge(19,25,2)
g.add_edge(20,14,2)
g.add_edge(20,15,1)
g.add_edge(20,19,1)
g.add_edge(20,26,5)
g.add_edge(20,21,1)
g.add_edge(20,23,1)
g.add_edge(21,17,1)
g.add_edge(21,20,1)
g.add_edge(21,22,4)
g.add_edge(21,23,1)
g.add_edge(24,18,2)
g.add_edge(24,25,2)
g.add_edge(25,19,3)
g.add_edge(25,24,2)
g.add_edge(25,26,1)
g.add_edge(26,20,5)
g.add_edge(26,25,1)
g.add_edge(26,27,1)
g.add_edge(27,26,1)
g.add_edge(27,23,5)

D = g.dijkstra(0)
print("Distance: ", D[15])

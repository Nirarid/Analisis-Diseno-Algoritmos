# Python3 program to find minimum edge
# between given two vertex of Graph
import queue

# function for finding minimum
# no. of edge using BFS
def minEdgeBFS(edges, u, v, n):
	
	# visited[n] for keeping track
	# of visited node in BFS
	visited = [0] * n

	# Initialize distances as 0
	distance = [0] * n

	# queue to do BFS.
	Q = queue.Queue()
	distance[u] = 0

	Q.put(u)
	visited[u] = True
	while (not Q.empty()):
		x = Q.get()
		
		for i in range(len(edges[x])):
			if (visited[edges[x][i]]):
				continue

			# update distance for i
			distance[edges[x][i]] = distance[x] + 1
			Q.put(edges[x][i])
			visited[edges[x][i]] = 1
	return distance[v]

# function for addition of edge
def addEdge(edges, u, v):
	edges[u].append(v)
	edges[v].append(u)

# Driver Code
if __name__ == '__main__':

	# To store adjacency list of graph
	n = 47
	edges = [[] for i in range(n)]
	addEdge(edges, 1, 2)
	addEdge(edges, 1, 8)
	addEdge(edges, 2, 3)
	addEdge(edges, 2, 5)
	addEdge(edges, 3, 4)
	addEdge(edges, 3, 5)
	addEdge(edges, 4, 6)
	addEdge(edges, 5, 6)
	addEdge(edges, 5, 9)
	addEdge(edges, 6, 13)
	addEdge(edges, 6, 7)
	addEdge(edges, 7, 17)
	addEdge(edges, 7, 23)
	addEdge(edges, 8, 11)
	addEdge(edges, 8, 19)
	addEdge(edges, 9, 11)
	addEdge(edges, 9, 10)
	addEdge(edges, 10, 13)
	addEdge(edges, 10, 12)
	addEdge(edges, 11, 12)
	addEdge(edges, 11, 14)
	addEdge(edges, 12, 15)
	addEdge(edges, 12, 16)
	addEdge(edges, 13, 17)
	addEdge(edges, 13, 18)
	addEdge(edges, 17, 23)
	addEdge(edges, 17, 18)
	addEdge(edges, 14, 19)
	addEdge(edges, 14, 15)
	addEdge(edges, 14, 20)
	addEdge(edges, 15, 16)
	addEdge(edges, 15, 21)
	addEdge(edges, 16, 18)
	addEdge(edges, 16, 21)
	addEdge(edges, 18, 17)
	addEdge(edges, 18, 22)
	addEdge(edges, 23, 22)
	addEdge(edges, 19, 20)
	addEdge(edges, 19, 25)
	addEdge(edges, 20, 21)
	addEdge(edges, 20, 26)
	addEdge(edges, 21, 27)
	addEdge(edges, 21, 22)
	addEdge(edges, 21, 24)
	addEdge(edges, 22, 24)
	addEdge(edges, 25, 26)
	addEdge(edges, 26, 27)
	addEdge(edges, 27, 28)


	u = 1
	v = 27
	print("Distance :" , minEdgeBFS(edges, u, v, n))

# This code is contributed by PranchalK

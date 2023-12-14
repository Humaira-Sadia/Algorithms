# DIJKSTRA'S ALGORITHMS
def dijkstras(G, n, src):
    distance = [float('inf')] * n
    visited = [False] * n

    distance[src] = 0

    for _ in range(n):
        u = extract_min(visited, distance, n)
        visited[u] = True

        for v in range(n):
            if not visited[v] and G[u][v] != 0:
                relax(u, v, G, distance)

    print("Vertex\t Distance from Source")
    for i in range(n):
        print("%d \t\t %d" % (i, distance[i]))

def relax(u, v, W, dist):
    if dist[u] != float('inf') and dist[u] + W[u][v] < dist[v]:
        dist[v] = dist[u] + W[u][v]

def extract_min(visited, dist, n):
    min_dist = float('inf')
    min_index = -1

    for v in range(n):
        if not visited[v] and dist[v] < min_dist:
            min_dist = dist[v]
            min_index = v

    return min_index


n = int(input("\nEnter the number of Vertices: "))
G = [[0, 3, 2, 0],
     [3, 0, 5, 5],
     [2, 5, 0, 6],
     [0, 5, 6, 0]]

src = int(input("Enter the source vertex: "))
dijkstras(G, n, src)
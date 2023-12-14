# PRIMS ALGO IMPLEMENTATION
n = 7
infinity =  99999
G = [[0, 28, 0, 0, 0, 10, 0],
     [28, 0, 6, 0, 0, 0, 14],
     [0, 16, 0, 12, 0, 0, 0],
     [0, 0, 12, 0, 22, 0, 18],
     [0, 0, 0, 22, 0, 25,24],
     [10, 0, 0, 0, 25, 0, 0],
     [0, 14, 0, 18, 24, 0, 0]]

visited = [0,0,0,0,0,0,0]
no_edges = 0
visited[0] = 1
min_cost = 0
while(no_edges < n-1):
    min = infinity
    u = 0
    v= 0
      
    for i in range(n):
        if visited[i]:
            for j in range (n):
                if((not visited[j] and G[i][j])):
                        if (min > G[i][j]):
                         min =  G[i][j]
                         u = i
                         v = j
    
    print(str(u+1) + "->" + str(v+1) + ": " + str(G[u][v]))
    min_cost += G[u][v]
    visited[v] = 1
    no_edges += 1
    
print("Minimum Spanning Tree Cost = " + str(min_cost))
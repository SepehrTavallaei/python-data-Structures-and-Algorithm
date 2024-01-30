matrix = [[0,8,float("inf"),1],
          [float("inf"),0,1,float("inf")],
          [4,float("inf"),0,float("inf")],
          [float("inf"),2,9,0]
        ]

def FloydWarshall(nV,G):
    distance = G
    for k in range(nV):
        for i in range(nV):
            for j in range(nV):
                distance[i][j] = min(distance[i][j],distance[i][k]+distance[k][j])
    
    print(distance)

FloydWarshall(4,matrix)

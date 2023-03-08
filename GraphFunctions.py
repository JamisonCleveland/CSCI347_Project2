import networkx as nx
import pandas as pd
import csv

#Preprocess the dataset
from Preprocess import largest_connected_component
G = largest_connected_component('lastfm_asia_edges.csv')

def num_vertices(edges):
    vertices = set()
    for edge in edges:
        vertices.add(edge[0])
        vertices.add(edge[1])
    return len(vertices)

def vertex_degree(edges, vertex_index):
    degree = 0
    for edge in edges:
        if vertex_index in edge:
            degree += 1
    return degree

def clustering_coefficient(edges, vertex_index):
    neighbors = set()
    for edge in edges:
        # add to neighbors if vertex exists in an edge (finds adjacent nodes)
        if vertex_index in edge:
            neighbors.add(edge[0] if edge[1] == vertex_index else edge[1])
    if len(neighbors) < 2:
        return 0.0
    num_edges = 0
    # count how many edges are between vertices adjacent to the vertex index
    for i in neighbors:
        for j in neighbors:
            if (i, j) in edges or (j, i) in edges:
                num_edges += 1
    # clustering coefficient: C = 2 * E / (k * (k - 1))
    length = len(neighbors)
    clustering = 2.0 * num_edges / (length * (length - 1))
    return clustering



def betweenness_centrality(G, vertex):

    G1 = nx.Graph()
    for edge in G:
        G1.add_edge(edge[0], edge[1])


    G2 = np.array(G)
    G2.flatten()
    num = np.unique(G2)
    tes = []
    possiblePaths = [(a, b) for idx, a in enumerate(num) for b in num[idx + 1:]]
    for x in possiblePaths:
        if (x.count(vertex) == 0):
            tes.append(x)


    shortestPaths = []
    shortestPathWithVertex = []
    for edge in tes:
        begin = edge[0]
        end = edge[1]
        numSP = len([p for p in nx.all_shortest_paths(G1, begin, end)])
        idk = [p for p in nx.all_shortest_paths(G1, begin, end)]
        for path in idk:
            count = 0
            if (path.count(vertex) == 1):
                count = count + 1
        shortestPathWithVertex.append(count)
        shortestPaths.append(numSP)


    sumArr = []
    for i in range(len(shortestPaths)):
        sumArr.append(shortestPathWithVertex[i]/shortestPaths[i])

    ans = 0
    for i in range(len(sumArr)):
        ans = ans + sumArr[i]

    return(ans)


def average_shortest_path_length(G):
    
    G1 = nx.Graph()
    for edge in G:
        G1.add_edge(edge[0], edge[1]) 

    G2 = np.array(G)
    G2.flatten()
    vertexes = np.unique(G2)

    graph = {}
    for i in range(1, len(vertexes)+1):
        graph[i] = [n for n in G1.neighbors(i)]

    possiblePaths = [(a, b) for idx, a in enumerate(vertexes) for b in vertexes[idx + 1:]]

    shortestPathLengths = []
    for path in possiblePaths:
        begin = path[0]
        end = path[1]
        pathVertices = [[begin]]
        previousVertices = {begin}
        count = 0
        
        while count < len(pathVertices):
            previous = pathVertices[count][-1]
            next = graph[previous]

            if end in next:
                pathVertices[count].append(end)
                shortestPathLengths.append(len(pathVertices[count])-1)
                break 

            for vertice in next:
                if not vertice in previousVertices:
                    cont = pathVertices[count][:]
                    cont.append(vertice)
                    pathVertices.append(cont)
                    previousVertices.add(vertice)
            count += 1

    sum = 0
    for i in range(len(shortestPathLengths)):
        sum += shortestPathLengths[i]

    ans = sum/len(possiblePaths)
    return(ans)


# ----- FUNCTION CALLS -------
# NOTE: for vertex index, use the number of a specific node.
if __name__ == '__main__':
    print("Number of vertices: ", num_vertices(G.edges))
    print("Degree: ", vertex_degree(G.edges, 1200)) #test index
    print("Clustering Coefficient: ", clustering_coefficient(G.edges, 1200)) #test index

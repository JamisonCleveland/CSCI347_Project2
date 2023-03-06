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

# ----- FUNCTION CALLS -------
# NOTE: for vertex index, use the number of a specific node.
print("Number of vertices: ", num_vertices(G))
print("Degree: ", vertex_degree(G, 1200)) #test index
print("Clustering Coefficient: ", clustering_coefficient(G, 1200)) #test index
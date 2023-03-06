import networkx as nx
import csv

def largest_connected_component(filename):
    # Read the CSV file
    with open(filename) as csvfile:
        reader = csv.reader(csvfile)
        next(reader)
        edges = [(row[0], row[1]) for row in reader]

    # Create a graph and add the edges
    G = nx.Graph()
    G.add_edges_from(edges)

    # Find the largest connected component
    largest_cc = max(nx.connected_components(G), key=len)

    # Return the largest connected component
    return largest_cc


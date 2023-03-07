import networkx as nx
import pandas as pd
import csv
import pickle


def largest_connected_component(csv_file, pct=0.30):
    # Read CSV file into a Pandas DataFrame
    df = pd.read_csv(csv_file, header=None, skiprows=1)
    # Create an undirected Graph from the DataFrame
    G = nx.from_pandas_edgelist(df, 0, 1, create_using=nx.Graph())

    shuffled_verts = []
    with open('shuffled_verts.pkl', 'rb') as file:
        shuffled_verts = pickle.load(file)

    nodes_to_take = int(len(G) * pct)
    G = nx.subgraph(G, shuffled_verts[:nodes_to_take])

    # Find the largest connected component
    largest_cc = max(nx.connected_components(G), key=len)
    # Create a new graph with only the largest connected component
    subgraph = G.subgraph(largest_cc)
    return subgraph

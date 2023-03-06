import networkx as nx
import pandas as pd
import csv


def largest_connected_component(csv_file):
    # Read CSV file into a Pandas DataFrame
    df = pd.read_csv(csv_file, header=None, skiprows=1)
    # Create an undirected Graph from the DataFrame
    G = nx.from_pandas_edgelist(df, 0, 1, create_using=nx.Graph())
    # Find the largest connected component
    largest_cc = min(nx.connected_components(G), key=len)
    # Create a new graph with only the largest connected component
    subgraph = G.subgraph(largest_cc)
    return subgraph

import matplotlib.pyplot as plt
import networkx as nx
import random
import heapq

from Preprocess import largest_connected_component
import GraphFunctions as gf

def random_sample_by_nodes(G: nx.Graph, p: float) -> nx.Graph:
    nodes = len(G)
    random_nodes = random.sample(list(G), int(nodes * p))
    return G.subgraph(random_nodes)

G = largest_connected_component('lastfm_asia_edges.csv')

# random sample of the graph, since nx.draw is too slow for such a large graph
G = random_sample_by_nodes(G, 0.15)
# and largest cc for the sample
G = G.subgraph(max(nx.connected_components(G), key=len))

# 11. [5 points] Produce a visualization of the graph (or graph sample that you used).
nx.draw(G, node_size=10)
#plt.savefig("graph.png")
plt.show()

# 12. [3 points] Find the 10 nodes with the highest degree.
degrees = (gf.vertex_degree(G.edges, v_idx) for v_idx in G)
print('Top 10 nodes by degree:', heapq.nlargest(10, degrees))

# 13. [3 points] Find the 10 nodes with the highest betweenness centrality.
### TODO: Replace w/ functions in `GraphFunctions.py`
bcs = nx.betweenness_centrality(G)
top_10_by_bc = heapq.nlargest(10, bcs.values())
print('Top 10 nodes by betweenness centrality:', top_10_by_bc)

# 14. [3 points] Find the 10 nodes with the highest clustering coefficient. If there are ties, choose 10 to report and explain how the 10 were chosen.
## maintain a heap of cc's, has to be negative to make it a max heap
neg_clustering_coeffs = [-gf.clustering_coefficient(G.edges, v_idx) for v_idx in G]
heapq.heapify(neg_clustering_coeffs)

## loop through heap until we have at most 10 unique greatest values
top_10_by_cc = []
while len(top_10_by_cc) < 10 and neg_clustering_coeffs:
    val = -heapq.heappop(neg_clustering_coeffs)
    if val in top_10_by_cc:
        continue
    top_10_by_cc.append(val)

print('Top 10 nodes by clustering coefficients:', top_10_by_cc)

# 15. [3 points] Find the top 10 nodes as ranked by eigenvector centrality
### TODO: Replace w/ functions in `GraphFunctions.py`
eigen_cs = nx.eigenvector_centrality(G)
top_10_by_eigen_c = heapq.nlargest(10, eigen_cs.values())
print('Top 10 nodes by eigenvector centrality:', top_10_by_eigen_c)

# 16. [3 points] Find the top 10 nodes as ranked by Pagerank
### TODO: Replace w/ functions in `GraphFunctions.py`
page_rank_cs = nx.pagerank(G)
top_10_by_page_rank = heapq.nlargest(10, page_rank_cs.values())
print('Top 10 by PageRank', top_10_by_eigen_c)

# 17. [3 points] Comment on the differences and similarities in questions 12-16. Are the highly ranked nodes mostly the same? Do you notice significant differences in the rankings? Why do you think this is the case?
### TODO

# 18. [3 points] Compute the average shortest path length in the graph. Based on your result, does the graph exhibit small-world behavior?
### TODO: Replace w/ functions in `GraphFunctions.py`
mu_length = nx.average_shortest_path_length(G)
print('Average shortest path length:', mu_length)

# 19. [5 points] Plot the degree distribution of the graph on a log-log-scale. Does the graph exhibit power law behavior? Include the plot and the code used to generate it in your submission.
### TODO: Replace w/ functions in `GraphFunctions.py`
deg_hist = nx.degree_histogram(G)
plt.hist(deg_hist)
plt.xscale('log')
plt.yscale('log')
plt.show()

# 20. [3 points EXTRA CREDIT] Create a log-log plot with the logarithm of node degree on the x-axis and the logarithm of the average clustering coefficient of nodes with that degree on the y-axis. Does the clustering coefficient exhibit power law behavior (is there a clustering effect)? Include the plot and the code used to generate it in your submission. μL
### TODO

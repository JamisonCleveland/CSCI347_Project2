import matplotlib.pyplot as plt
import networkx as nx
import random
import heapq

from Preprocess import largest_connected_component
import GraphFunctions as gf

G = largest_connected_component('lastfm_asia_edges.csv', pct=0.50)

# 11. [5 points] Produce a visualization of the graph (or graph sample that you used).
nx.draw(G, node_size=10)
#plt.savefig("graph.png")
plt.show()

# 12. [3 points] Find the 10 nodes with the highest degree.
degrees = nx.degree(G)
top_10_by_deg = heapq.nlargest(10, degrees, key=lambda p: p[1])
print('Top 10 nodes by degree:', top_10_by_deg)

# 13. [3 points] Find the 10 nodes with the highest betweenness centrality.
bcs = gf.betweenness_centrality_fast(G)
top_10_by_bc = heapq.nlargest(10, bcs.items(), key=lambda p: p[1])
print('Top 10 nodes by betweenness centrality:', top_10_by_bc)

# 14. [3 points] Find the 10 nodes with the highest clustering coefficient. If there are ties, choose 10 to report and explain how the 10 were chosen.
## maintain a heap of cc's, has to be negative to make it a max heap
neg_clustering_coeffs = [(-gf.clustering_coefficient(G.edges, v_idx), v_idx) for v_idx in G]
heapq.heapify(neg_clustering_coeffs)

## loop through heap until we have at most 10 unique greatest values
top_10_by_cc = []
visited = set()
while len(top_10_by_cc) < 10 and neg_clustering_coeffs:
    val, v_idx = heapq.heappop(neg_clustering_coeffs)
    val = -val
    if val in visited:
        continue
    visited.add(val)
    top_10_by_cc.append((v_idx, val))

print('Top 10 nodes by clustering coefficients:', top_10_by_cc)

# 15. [3 points] Find the top 10 nodes as ranked by eigenvector centrality
eigen_cs = nx.eigenvector_centrality(G)
top_10_by_eigen_c = heapq.nlargest(10, eigen_cs.items(), key=lambda p: p[1])
print('Top 10 nodes by eigenvector centrality:', top_10_by_eigen_c)

# 16. [3 points] Find the top 10 nodes as ranked by Pagerank
page_rank_cs = nx.pagerank(G)
top_10_by_page_rank = heapq.nlargest(10, page_rank_cs.items(), key=lambda p: p[1])
print('Top 10 by PageRank', top_10_by_eigen_c)

# 17. [3 points] Comment on the differences and similarities in questions 12-16. Are the highly ranked nodes mostly the same? Do you notice significant differences in the rankings? Why do you think this is the case?
### TODO

# 18. [3 points] Compute the average shortest path length in the graph. Based on your result, does the graph exhibit small-world behavior?
mu_length = nx.average_shortest_path_length(G)
print('Average shortest path length:', mu_length)

# 19. [5 points] Plot the degree distribution of the graph on a log-log-scale. Does the graph exhibit power law behavior? Include the plot and the code used to generate it in your submission.
degs = nx.degree(G)
hist = nx.degree_histogram(G)
plt.bar(list(range(len(hist))), hist, align='edge')
plt.loglog()
plt.xlabel('Degree')
plt.ylabel('Count')
plt.show()

# 20. [3 points EXTRA CREDIT] Create a log-log plot with the logarithm of node degree on the x-axis and the logarithm of the average clustering coefficient of nodes with that degree on the y-axis. Does the clustering coefficient exhibit power law behavior (is there a clustering effect)? Include the plot and the code used to generate it in your submission. μL
### TODO
by_deg = {}
degs = nx.degree(G)
ccs = nx.clustering(G)
for v, deg in degs:
    if deg not in by_deg:
        by_deg[deg] = []
    
    by_deg[deg].append(ccs[v])
avgs = []
m = max(by_deg.keys())
for i in range(m+1):
    avg = 0
    if i in by_deg:
        vals = by_deg[i]
        avg = sum(vals) / len(vals)
    avgs.append(avg)

plt.bar(list(range(m+1)), avgs, align='edge')
plt.loglog()
plt.xlabel('Degree')
plt.ylabel('Average clustering coefficients')
plt.show()
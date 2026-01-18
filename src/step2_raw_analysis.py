import osmnx as ox
import statistics

# Load raw graph
G = ox.load_graphml("data/raw/dehradun_raw.graphml")

# -------------------------
# Basic counts
# -------------------------
num_nodes = len(G.nodes)
num_edges = len(G.edges)

print("Nodes:", num_nodes)
print("Edges:", num_edges)

# -------------------------
# Node degree analysis
# -------------------------
degrees = [deg for _, deg in G.degree()]
print("Average node degree:", round(statistics.mean(degrees), 2))
print("Max node degree:", max(degrees))

# -------------------------
# Edge length analysis
# -------------------------
edge_lengths = [
    data["length"]
    for _, _, data in G.edges(data=True)
    if "length" in data
]

print("Average edge length (m):", round(statistics.mean(edge_lengths), 2))
print("Min edge length (m):", round(min(edge_lengths), 2))
print("Max edge length (m):", round(max(edge_lengths), 2))

# -------------------------
# Interpretation hint
# -------------------------
print("\nNOTE:")
print("- Very small edge lengths = over-segmentation")
print("- High-degree nodes = noisy intersections")

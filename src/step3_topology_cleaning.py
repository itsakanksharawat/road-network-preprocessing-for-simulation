import osmnx as ox
import networkx as nx
import math
import time

# -------------------------
# CONFIG
# -------------------------
RAW_GRAPH_PATH = "data/raw/dehradun_raw.graphml"
OUTPUT_PATH = "data/cleaned/dehradun_cleaned.graphml"

MIN_EDGE_LENGTH = 5.0       # meters (remove nonsense segments)
MERGE_DISTANCE = 10.0       # meters (merge close intersections)

# -------------------------
# Helpers
# -------------------------
def haversine(lat1, lon1, lat2, lon2):
    R = 6371000
    phi1, phi2 = math.radians(lat1), math.radians(lat2)
    dphi = phi2 - phi1
    dl = math.radians(lon2 - lon1)
    a = math.sin(dphi/2)**2 + math.cos(phi1)*math.cos(phi2)*math.sin(dl/2)**2
    return 2 * R * math.atan2(math.sqrt(a), math.sqrt(1-a))

# -------------------------
# Load graph
# -------------------------
start = time.time()
G = ox.load_graphml(RAW_GRAPH_PATH)

print("Original nodes:", len(G.nodes))
print("Original edges:", len(G.edges))

# -------------------------
# 1️⃣ REMOVE MICRO EDGES
# -------------------------
edges_to_remove = []

for u, v, k, data in G.edges(keys=True, data=True):
    length = data.get("length", 0)
    if length < MIN_EDGE_LENGTH:
        edges_to_remove.append((u, v, k))

for u, v, k in edges_to_remove:
    if G.has_edge(u, v, k):
        G.remove_edge(u, v, k)

print("Removed micro edges:", len(edges_to_remove))

# -------------------------
# 2️⃣ MERGE CLOSE INTERSECTIONS
# -------------------------
nodes = list(G.nodes(data=True))
merged = set()

for i in range(len(nodes)):
    n1, d1 = nodes[i]
    if n1 in merged:
        continue

    for j in range(i+1, len(nodes)):
        n2, d2 = nodes[j]
        if n2 in merged:
            continue

        dist = haversine(d1["y"], d1["x"], d2["y"], d2["x"])
        if dist <= MERGE_DISTANCE:
            # Redirect edges
            for u, v, k, data in list(G.edges(n2, keys=True, data=True)):
                G.add_edge(n1, v, **data)
            for u, v, k, data in list(G.in_edges(n2, keys=True, data=True)):
                G.add_edge(u, n1, **data)

            if G.has_node(n2):
                G.remove_node(n2)
                merged.add(n2)

print("Merged nodes:", len(merged))

# -------------------------
# Save cleaned graph
# -------------------------
ox.save_graphml(G, OUTPUT_PATH)

end = time.time()

print("\nCLEANING COMPLETE")
print("Cleaned nodes:", len(G.nodes))
print("Cleaned edges:", len(G.edges))
print("Time taken (sec):", round(end - start, 2))

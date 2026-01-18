import os
import osmnx as ox
import matplotlib.pyplot as plt

# -----------------------
# Configuration
# -----------------------
CITY_NAME = "Dehradun, Uttarakhand, India"
SAVE_DIR = "data/raw"

os.makedirs(SAVE_DIR, exist_ok=True)

# -----------------------
# Download road network
# -----------------------
print("Downloading Dehradun road network...")

G = ox.graph_from_place(
    CITY_NAME,
    network_type="drive",   # only drivable roads
    simplify=False          # keep raw data
)

# -----------------------
# Save data
# -----------------------
file_path = os.path.join(SAVE_DIR, "dehradun_raw.graphml")
ox.save_graphml(G, file_path)

print("Saved at:", file_path)

# -----------------------
# Visualize (optional)
# -----------------------
ox.plot_graph(
    G,
    node_size=2,
    edge_linewidth=0.5,
    bgcolor="white"
)

print("Nodes:", len(G.nodes))
print("Edges:", len(G.edges))

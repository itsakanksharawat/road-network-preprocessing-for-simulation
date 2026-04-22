
import os
import json
import osmnx as ox
import matplotlib.pyplot as plt


CITY_NAME = "Dehradun, Uttarakhand, India"

RAW_DIR = "data/raw"
IMG_DIR = "data/images"

os.makedirs(RAW_DIR, exist_ok=True)
os.makedirs(IMG_DIR, exist_ok=True)

# download road network
print(f"[INFO] Downloading road network for: {CITY_NAME}")

G_raw = ox.graph_from_place(
    CITY_NAME,
    network_type="drive",   
    simplify=False          
)

print("[INFO] Download complete")

# raw graph
raw_graph_path = os.path.join(RAW_DIR, "dehradun_raw.graphml")
ox.save_graphml(G_raw, raw_graph_path)

print(f"[INFO] Raw graph saved at: {raw_graph_path}")

# baseline metrics
baseline_metrics = {
    "city": CITY_NAME,
    "nodes": len(G_raw.nodes),
    "edges": len(G_raw.edges)
}

baseline_path = os.path.join(RAW_DIR, "baseline_metrics.json")

with open(baseline_path, "w") as f:
    json.dump(baseline_metrics, f, indent=4)

print(f"[INFO] Baseline metrics saved at: {baseline_path}")
print("[INFO] Nodes:", baseline_metrics["nodes"])
print("[INFO] Edges:", baseline_metrics["edges"])

#visuals
print("[INFO] Generating raw graph visualization...")

fig, ax = ox.plot_graph(
    G_raw,
    node_size=2,
    edge_linewidth=0.5,
    bgcolor="white",
    show=False,
    close=False
)

img_path = os.path.join(IMG_DIR, "raw_graph.png")
fig.savefig(img_path, dpi=300)
plt.close(fig)

print(f"[INFO] Raw graph image saved at: {img_path}")

print("[SUCCESS] Step 1 (Data Gathering) completed.")

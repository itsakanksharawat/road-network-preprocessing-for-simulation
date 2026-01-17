
# Road Network Preprocessing for Simulation

## Overview
This project demonstrates how large-scale, real-world road network data can be transformed into a
simulation-ready format through systematic preprocessing and topology optimization.

The focus is on handling messy data, reducing graph complexity, and improving preprocessing efficiency
before applying any simulation or AI models.

## Pipeline
1. Extract raw road network data from OpenStreetMap
2. Analyze graph structure and identify inefficiencies
3. Clean topology by removing micro-segments and merging redundant intersections
4. Benchmark preprocessing performance before and after cleaning

## Tech Stack
- Python
- OpenStreetMap (via OSMnx)
- NetworkX
- GeoPandas, Shapely

## Results
- Significant reduction in node and edge count
- Measurable reduction in preprocessing overhead

## Notes
Raw road network data is generated programmatically and is not stored in this repository.

"""
netvis.py

This script loads a GraphML file and generates an interactive
network visualization using NetworkX and PyVis.

Workflow:
1. Ensure G.graphml exists in the project directory.
2. Run this script.
3. Open the generated net.html file in a browser.
"""

import os
import networkx as nx
from pyvis.network import Network


GRAPH_FILE = "G.graphml"
OUTPUT_FILE = "net.html"


def main():
    """
    Load a GraphML file and generate an interactive HTML network visualization.
    """
    if not os.path.exists(GRAPH_FILE):
        raise FileNotFoundError(
            f"{GRAPH_FILE} not found. Generate the GraphML file first."
        )

    # Load graph
    graph = nx.read_graphml(GRAPH_FILE)

    # Create PyVis network
    network = Network(width="100%", select_menu=False, filter_menu=False)
    network.from_nx(graph)

    # Enable control buttons
    network.show_buttons(filter_=["nodes", "physics"])

    # Generate HTML output
    network.show(OUTPUT_FILE, notebook=False)


if __name__ == "__main__":
    main()
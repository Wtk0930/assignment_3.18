import networkx as nx
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
from collections import Counter
from tqdm import tqdm


def find_node_by_city(G, city_name):
    candidates = []
    for node in G.nodes:
        attrs = G.nodes[node]
        if attrs.get('city', '').lower() == city_name.lower():
            candidates.append(node)
    
    if len(candidates) == 0:
        raise ValueError(f"No matching node found: city='{city_name}'")
    elif len(candidates) > 1:
        print(f"Multiple matching nodes found: {candidates}, using the first node")
    return candidates[0]

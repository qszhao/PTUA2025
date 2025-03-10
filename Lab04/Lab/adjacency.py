#!/usr/bin/env python
# coding: utf-8

# In[1]:


get_ipython().run_cell_magic('writefile', 'adjacency.py', 'class Node:\n    def __init__(self, node_id):\n        self.node_id = node_id\n        self.neighbors = []\n\n    def add_neighbor(self, neighbor):\n        if neighbor not in self.neighbors:\n            self.neighbors.append(neighbor)\n\n    def connectivity(self):\n        return len(self.neighbors)\n\n\nclass Graph:\n    def __init__(self):\n        self.nodes = {}\n\n    def add_node(self, node_id):\n        if node_id not in self.nodes:\n            self.nodes[node_id] = Node(node_id)\n\n    def add_edge(self, node1_id, node2_id):\n        self.add_node(node1_id)\n        self.add_node(node2_id)\n        self.nodes[node1_id].add_neighbor(self.nodes[node2_id])\n        self.nodes[node2_id].add_neighbor(self.nodes[node1_id])\n\n    def load_from_gal(self, filepath):\n        with open(filepath, \'r\') as file:\n            for line in file:\n                parts = line.strip().split()\n                try:\n                    key = int(parts[0])\n                    values = [int(p) for p in parts[1:] if p.isdigit()]\n                    for val in values:\n                        self.add_edge(key, val)\n                except ValueError:\n                    print(f"Skipping line: {line}")\n\n    def average_connectivity(self):\n        total = sum(node.connectivity() for node in self.nodes.values())\n        return total / len(self.nodes) if self.nodes else 0\n\n    def max_connectivity(self):\n        max_conn = max(node.connectivity() for node in self.nodes.values())\n        max_nodes = [node.node_id for node in self.nodes.values() if node.connectivity() == max_conn]\n        return max_conn, max_nodes\n\n    def min_connectivity(self):\n        min_conn = min(node.connectivity() for node in self.nodes.values() if node.connectivity() > 0)\n        min_nodes = [node.node_id for node in self.nodes.values() if node.connectivity() == min_conn]\n        return min_conn, min_nodes\n\n    def disconnected_nodes(self):\n        disconnected = [node.node_id for node in self.nodes.values() if node.connectivity() == 0]\n        return disconnected if disconnected else None\n\n    def summary_statistics(self):\n        avg_conn = self.average_connectivity()\n        max_conn, max_nodes = self.max_connectivity()\n        min_conn, min_nodes = self.min_connectivity()\n        disconnected = self.disconnected_nodes()\n\n        print(f"Average connectivity: {avg_conn:.2f}")\n        print(f"Maximum connectivity: {max_conn} (Nodes: {max_nodes})")\n        print(f"Minimum connectivity: {min_conn} (Nodes: {min_nodes})")\n        if disconnected:\n            print(f"Disconnected nodes: {disconnected}")\n        else:\n            print("No disconnected nodes found.")\n')


# In[3]:


import adjacency
import importlib
importlib.reload(adjacency)  

graph = adjacency.Graph()
graph.load_from_gal('Lab04-1.gal') 
graph.summary_statistics()


# In[ ]:





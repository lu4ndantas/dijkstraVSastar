import networkx as nx
from random import randint
from networkx.readwrite import json_graph
import json


grafo1 = nx.gnp_random_graph(18000,0.0006)
for (u, v) in grafo1.edges():
    grafo1.edges[u,v]['weight'] = randint(0,10)
data = json_graph.adjacency_data(grafo1)
json_object = json.dumps(data, indent = 4) 
with open("18000.json", "w") as outfile: 
    outfile.write(json_object)


grafo2 = nx.gnp_random_graph(12000,0.0009)
for (u, v) in grafo2.edges():
    grafo2.edges[u,v]['weight'] = randint(0,10)
data = json_graph.adjacency_data(grafo2)
json_object = json.dumps(data, indent = 4) 
with open("12000.json", "w") as outfile: 
    outfile.write(json_object)


grafo3 = nx.gnp_random_graph(6000,0.0018)
for (u, v) in grafo3.edges():
    grafo3.edges[u,v]['weight'] = randint(0,10)
data = json_graph.adjacency_data(grafo3)
json_object = json.dumps(data, indent = 4) 
with open("6000.json", "w") as outfile: 
    outfile.write(json_object)



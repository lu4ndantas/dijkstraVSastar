import tracemalloc #Mede a Memória ultilizada
import networkx as nx #Grafos
from random import randint #Gera numero
from networkx.readwrite import json_graph #json para grafo
import json #ler o json
from time import time #Mede o tempo
import numpy as np #calculos estatisticos

with open('6000.json', 'r') as openfile: 
    json_object = json.load(openfile) 
g1 = json_graph.adjacency_graph(json_object)

with open('12000.json', 'r') as openfile: 
    json_object = json.load(openfile) 
g2 = json_graph.adjacency_graph(json_object)

with open('18000.json', 'r') as openfile: 
    json_object = json.load(openfile) 
g3 = json_graph.adjacency_graph(json_object)

grafos = [g1, g2, g3]
count = 1
for grafo in grafos:
    vertice_aleatorio = randint(0,len(grafo))

    tempo_dijkstra = []
    tempo_astar = []
    memoria_dijkstra = []
    memoria_astar = []
    for i in range(100):
        inicio = time()

        tracemalloc.start()

        snapshot1 = tracemalloc.take_snapshot()
        nx.dijkstra_path(grafo,0, vertice_aleatorio)
        snapshot2 = tracemalloc.take_snapshot()

        fim = time()
        tempo_dijkstra.append((fim-inicio)*1000)

        stat = snapshot2.compare_to(snapshot1, 'lineno')[0]
        memoria_dijkstra.append(stat.size/1024) 
    print(f"Dijkstra - grafo: {count}")
    print("Média tempo em MS: %.20f"%(np.average(tempo_dijkstra)))
    print("Disvio padrão tempo: %.20f"%(np.std(tempo_dijkstra)))
    print("Média Memória em kiB: %.20f"%(np.average(memoria_dijkstra)))
    print("Disvio padrão memória: %.20f"%(np.std(memoria_dijkstra)))

    for i in range(100):
        inicio = time()

        tracemalloc.start()

        snapshot1 = tracemalloc.take_snapshot()
        nx.astar_path(grafo,0, vertice_aleatorio)
        snapshot2 = tracemalloc.take_snapshot()

        fim = time()
        tempo_astar.append((fim-inicio)*1000) 

        stat = snapshot2.compare_to(snapshot1, 'lineno')[0]
        memoria_astar.append(stat.size/1024) 

    print(f"A* - grafo {count}")
    print("Média tempo em MS: %.20f"%(np.average(tempo_astar)))
    print("Disvio padrão tempo: %.20f"%(np.std(tempo_astar)))
    print("Média Memória em KiB: %.20f"%(np.average(memoria_astar)))
    print("Disvio padrão memória: %.30f"%(np.std(memoria_astar)))

    count += 1
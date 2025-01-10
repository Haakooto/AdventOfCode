import networkx as nx
from itertools import combinations

def read(file):
    with open(file, "r") as file:
        return file.read().split("\n")[:-1]  # Most typical case

def solver_alt2(input_file):
    lines = read(input_file)
    
    network = nx.Graph()
    for line in lines:
        n1, n2 = line.split("-")
        network.add_edge(n1, n2)

    cliques = list(nx.find_cliques(network))

    triangles = []
    for sub in cliques:
        for s in combinations(sub, 3):
            triangle = tuple(sorted(s))
            triangles.append(triangle)

    triplets = sum(1 for tri in set(triangles) if any(n.startswith("t") for n in tri))
    
    max_clique = sorted(cliques, key=len)[-1]
    password = ",".join(sorted(max_clique))
 
    return triplets, password

import networkx as nx

def get_networkx_gfu(name_path):
	G = nx.Graph()
	
	with open(name_path) as f:
		_ = f.readline()
		
		num_vertices = int(f.readline())
		
		for idx in range(num_vertices):
			label = int(f.readline())
			G.add_node(idx, label = label)
			
		num_edges = int(f.readline())
		
		for idx in range(num_edges):
			x,y = map(int, f.readline().split())
			G.add_edge(x, y)

	return G
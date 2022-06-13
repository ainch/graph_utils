import networkx as nx

def get_networkx_gfu_format(name_path):
	G = nx.Graph()
	
	with open(name_path,'r') as f:
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

def get_networkx_graph_format(name_path):
	G = nx.Graph()
	
	with open(name_path, 'r') as f:
		_, x, y = f.readline().split()
		
		num_vertices = int(x)
		num_edges = int(y)
		
		for _ in range(num_vertices):
			_, v, l, d = f.readline().split()
			G.add_node(int(v), label = int(l))
		
		for _ in range(num_edges):
			_, x, y = f.readline().split()
			G.add_edge(int(x), int(y))

	return G

def make_file_graph_format(G, name_path):
	num_vertices = len(G.nodes())
	num_edgs = len(G.edges())
	
	with open(name_path, 'w') as f:
		f.write('t {} {}\n'.format(num_vertices, num_edgs))

		for node_and_label in G.nodes.data():
			node = node_and_label[0]
			label = node_and_label[1]['label']
			degree = G.degree(node)
			f.write('v {} {} {}\n'.format(node, label, degree))

		for x,y in G.edges():
			f.write('e {} {}\n'.format(x, y))

	
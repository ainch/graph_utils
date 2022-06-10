class Data_graph():
	def __init__(self, adj_list = [], edges = [], labels = [], comps = [], idx = []):
		self.adj_list = adj_list
		self.edges = edges
		self.labels = labels
		self.comps = comps
		self.idx = idx

	def read_igraph_form(self, name):
		edges_set = set([])
		graph_idx = -1
		with open(name, "r") as f:
			while True:
				l = f.readline()
				if l:
					if l[0] == 'e':
						x,y,z,w = l.split()
						x,y = min(x,y),max(x,y)
						if x != y and (x,y) not in edges_set:
							self.edges_set.append((x,y))
							self.edges_set.append((y,x))
							self.adj_list[x].append(y)
							self.adj_list[y].append(x)
					else:
						x,y,z = l.split()
						if x=="t":
							graph_idx = graph_idx + 1
						elif x=="v":
							self.idx.append(graph_idx)
							self.labels.append(z)
							self.adj_list.append([])
				else:
					break
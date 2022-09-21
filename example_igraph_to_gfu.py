from itertools import product
import graph

def simple():
    G = graph.get_networkx_igraph_format('example/g2.igraph')
    graph.make_file_gfu_format(G, 'example/g2.gfu')

if __name__=='__main__':
    simple()
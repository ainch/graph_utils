from itertools import product
import graph
import os

def simple():
    Gs = graph.get_networkx_igraph_format('example/g2.igraph')
    print(Gs)
    graph.make_file_gfu_format(Gs[0], 'example/g2_a.gfu')
    graph.make_file_gfu_format(Gs[1], 'example/g2_b.gfu')

if __name__=='__main__':
    simple()
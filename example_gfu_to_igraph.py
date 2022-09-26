from itertools import product
import graph
import os

def simple():
    G = graph.get_networkx_gfu_format('example/g3.gfu')
    graph.make_file_igraph_format([ G ], 'example/g3.igraph')

if __name__=='__main__':
    simple()
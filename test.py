import graph

def test_gfu_format():
    path_gfu = 'example/g.gfu'
    G = graph.get_networkx_gfu_format(path_gfu)
    print(G.nodes())
    print(G.nodes.data())
    print(G.edges())

def test_gfu_graph_format():
    path_graph = 'example/g.graph'
    G = graph.get_networkx_graph_format(path_graph)
    print(G.nodes())
    print(G.nodes.data())
    print(G.edges())

if __name__:
    test_gfu_graph_format()
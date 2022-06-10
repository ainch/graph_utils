import graph

def test_gfu_format():
    path_gfu = 'example/g.gfu'
    G = graph.get_networkx_gfu_format(path_gfu)
    print(G.nodes())
    print(G.nodes.data())
    print(G.edges())

def test_graph_format():
    path_graph = 'example/g.graph'
    G = graph.get_networkx_graph_format(path_graph)
    print(G.nodes())
    print(G.nodes.data())
    print(G.edges())

def test_gfu_format_to_graph_format():
    path_gfu = 'example/g.gfu'
    path_out_graph = 'example/g_out.graph'
    
    G = graph.get_networkx_gfu_format(path_gfu)
    graph.make_file_graph_format(G, path_out_graph)

if __name__:
    test_gfu_format()
    test_graph_format()
    test_gfu_format_to_graph_format()
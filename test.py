import graph

def test_gfu():
    path_gfu = 'example/g.gfu'
    G = graph.get_networkx_gfu(path_gfu)
    print(G.nodes())
    print(G.nodes.data())
    print(G.edges())

if __name__:
    test_gfu()
from itertools import product
import graph

def transform_query_graph_gfu_to_graph_format():
    names = [ 'patents', 'google', 'berkstan' ]
    densities = [ 'sparse', 'nonsparse' ]
    sizes = [ 10, 20, 30, 40, 50, 100, 150, 200 ]

    for name, density, size in product(names, densities, sizes):
        path_dir = '../finalQuery080322'
        path_dir_query_set = '/'.join([path_dir, name, density, str(size)]) 
        
        for idx in range(100):
            path_src = path_dir_query_set + '/q' + str(idx) + '.gfu'
            path_dest = path_dir_query_set + '/q' + str(idx) + '.graph'
        
            G = graph.get_networkx_gfu_format(path_src)
            graph.make_file_graph_format(G, path_dest)
            

def transform_data_graph_gfu_to_graph_format():
    names = [ 'patents', 'google', 'berkstan',  \
        'dblp_label20', 'human', 'yeast' ]
    
    for name in names:
        print(name)
        path_data_gfu = '../data/' + name + '.gfu'
        path_data_graph = '../data/' + name + '.graph'
        
        print('read')
        G = graph.get_networkx_gfu_format(path_data_gfu)
        print('write')
        graph.make_file_graph_format(G, path_data_graph)        
    
if __name__=="__main__":
    transform_data_graph_gfu_to_graph_format()

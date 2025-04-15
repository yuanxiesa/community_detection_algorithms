import pandas as pd
import networkit as nk
import networkx as nx
import json
import argparse

def export_graph(nx_graph_induced, outfile):
    data = nx.node_link_data(nx_graph_induced, edges="edges")
    # Write JSON data to file
    with open(outfile, 'w') as f:
        json.dump(data, f, indent=4)

def main():

    # Set up argument parsing
    parser = argparse.ArgumentParser(description="this script creates an induced graph")
    parser.add_argument("edge_list_file", help="Path to the edge list file: all nodes")
    parser.add_argument("selected_node_list_file", help="Path to nodes that forms the induced graph")
    parser.add_argument("out_file_json", help="Path to the json file recording the induced graph")

    args = parser.parse_args()

    edge_list = pd.read_csv(args.edge_list_file)
    graph = nk.Graph(directed=True)
    current_index = 0
    node_mapping = {}

    def get_node_index(node, current_index, node_mapping):
        if node not in node_mapping:
            node_mapping[node] = current_index
            graph.addNode()
            current_index += 1
        return (node_mapping[node], current_index, node_mapping)

    # Add edges to the graph
    for _, row in edge_list[['cited', 'citing']].iterrows():
        u_return = get_node_index(row["cited"], current_index, node_mapping)
        u = u_return[0]
        current_index = u_return[1]
        node_mapping = u_return[2]

        v_return = get_node_index(row["citing"], current_index, node_mapping)
        v = v_return[0]
        current_index = v_return[1]
        node_mapping = v_return[2]

        graph.addEdge(u, v)

    # Print basic graph information
    print(f"Number of nodes: {graph.numberOfNodes()}")
    print(f"Number of edges: {graph.numberOfEdges()}")

    # create induced graph
    node_doi_l = pd.read_csv(args.selected_node_list_file)
    node_doi_l = list(node_doi_l['doi'])
    node_idx_l = [get_node_index(x, current_index, node_mapping)[0] for x in node_doi_l]
    nk_graph_induced = nk.graphtools.subgraphFromNodes(graph, node_idx_l)
    node_mapping_induced_graph = dict((k, node_mapping[k]) for k in node_doi_l)

    # Convert networkit graph to networkx
    print("Converting networkit graph to networkx graph ...")
    nx_graph_induced = nx.Graph(directed=True)

    reverse_mapping = {v: k for k, v in node_mapping_induced_graph.items()}  # Reverse mapping for labels

    for u in nk_graph_induced.iterNodes():
        nx_graph_induced.add_node(reverse_mapping[u])  # Add nodes with original labels

    for u, v in nk_graph_induced.iterEdges():
        nx_graph_induced.add_edge(reverse_mapping[u], reverse_mapping[v])  # Add edges with labels

    print("Conversion ended ...")
    print("Creating JSON file ...")
    export_graph(nx_graph_induced, args.out_file_json)

if __name__ == '__main__':
    main()

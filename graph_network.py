import json
import random
import networkx as nx
from networkx.drawing.nx_agraph import graphviz_layout
import matplotlib.pyplot as plt

entity_category = ["Commercial Registered Agent", "Owner Name", "Owners", "Registered Agent"]
def get_relationships(business, businessDetails):
    
    edges = []
    i = 0
    for key, value in business.items():
        detail = businessDetails[key]
        company_name = value.get("TITLE")[0]
        for item in detail:
            if item['LABEL'] in entity_category:
                entity = item['VALUE'].split("\n")[0]
                # print(company_name, "HELLO", entity)
                edges.append((company_name, entity))  
    return edges

def create_graph(edges):
    graph = nx.Graph()
    for company, entity in edges:
        graph.add_edge(company, entity)
    return graph



def plot_network(graph):
    positions = graphviz_layout(graph)
    plt.figure(2, figsize=(10, 10))
    connected_subgraphs = (
        graph.subgraph(c) for c in nx.connected_components(graph)
    )
    # print(connected_subgraphs)
    for connected_subgraph in connected_subgraphs:
        random_color = [random.random()] * nx.number_of_nodes(connected_subgraph)
        if len(connected_subgraph.nodes()) > 1:
            nx.draw(
                connected_subgraph,
                positions,
                node_size=40,
                node_color=random_color,
                vmin=0.0,
                vmax=1.0,
                with_labels=False,
                bbox=dict(facecolor="whitesmoke"),
            )
            
    plt.title("Connected SubGraphs of companies and Entities")
    plt.savefig("connected.png")
    plt.show()
    plt.close()
    

if __name__ == "__main__":

    with open('./webapp_crawl_sayari/businesssearch.json', 'r') as f:
        ip = json.load(f)
        business = ip[0]['rows']
        details = ip[1:]
    
    businessDetails = {k:v for x in details for k,v in x.items()}
    edges = get_relationships(business, businessDetails)
    # companies = [x[0] for x in edges]
    network = create_graph(edges)
    plot_network(network)

        




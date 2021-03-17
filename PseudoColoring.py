import matplotlib.pyplot as plt
import networkx as nx
import pandas as pd
import numpy as np

maple = {
    "a": ["b", "c", "d"],
    "b": ["a", "c", "e"],
    "c": ["a", "b", "e"],
    "d": ["a", "e", ],
    "e": ["c", "b", "d"],
}

star = {
    "a": ["b","g","e"],
    "b": ["h","c","a"],
    "c": ["b","i","d"],
    "d": ["c","j","e"],
    "e": ["d","f","a"],
    "g": ["a","i","j"],
    "h": ["b","f","j"],
    "i": ["g","f","c"],
    "j": ["h","g","d"],
    "f": ["h","i","e"],
}

complex = {
    "a": ["b", "g"],
    "b": ["a", "c", "d", "f"],
    "c": ["b", "d"],
    "d": ["c", "b", "e"],
    "e": ["d", "f"],
    "f": ["b", "g", "e"],
    "g": ["f", "a"]
}

colors = {1: {"a"}}
cicle = 0
added_nodes = []
nodes_from = []
nodes_to = []

for node in star:
    assigned = False

    for c in colors:
        # print('current color ' + str(c))
        valid = True

        for v in colors[c]:
            # print('node = ' + str(node) + " in  map[" + str(v) + "]" + str(complex[v]))
            if node in star[v]:
                # print(f'{node} + {v} ')
                nodes_from.append(str(node).upper())
                nodes_to.append(str(v).upper())
                # print("not valid")
                valid = False
                break

        if valid:
            if node not in added_nodes:
                colors[c].add(node)
                added_nodes.append(node)
                # print('CURRENT COLORS =' + str(colors))
                assigned = True

    if not assigned:
        colors[len(colors) + 1] = {node}
        # print('new color in node ' + str(colors) + ' xd ' + str({node}))

    cicle += 1

print('Total colors: ' + str(len(colors)))
print(colors)

# df = pd.DataFrame({ 'from':['A','A','B','D','E','F','F','F','B',], 'to':['B','G','G','C','D','E','G','B','D']})

# Create df with node connections
df = pd.DataFrame({'from': nodes_from, 'to': nodes_to})

print("Node connections in dataframe")
print(df)

# G = nx.DiGraph()
# Build graph
# Plot df nodes to Graph
G = nx.from_pandas_edgelist(df, 'from', 'to', create_using=nx.Graph())

# G.add_edges_from(node_conections) old

newlist = [i for i in star]
# print(newlist)
group_values = []

dataframelist = []
for i in colors.keys():
    for item in newlist:
        if item in colors[i]:
            dataframelist.append(item.upper())
            group_values.append(i)

# print(group_values)

# And a data frame with characteristics for your nodes
carac = pd.DataFrame({'ID': dataframelist, 'myvalue': group_values})

G.nodes()
carac = carac.set_index('ID')
carac = carac.reindex(G.nodes())

print("Nodes with selected color")
print(carac)

pos = nx.spring_layout(G, k=4.0)
nx.draw_networkx(G, pos, cmap=plt.get_cmap('cool'),
                 node_color=carac['myvalue'], node_size=400, arrows=False, with_labels=2, font_color='k')

plt.show()


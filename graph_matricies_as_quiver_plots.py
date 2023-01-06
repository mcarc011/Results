#!/bin/python
#%%
from data.testmatrix import test_data
import matplotlib.pyplot as plt
from polytopes2 import *
import networkx as nx
#from tqdm import tqdm
import numpy as np
import os


def tako_sample_arrays() -> tuple:
    """Sample arrays.

    Returns:
        tuple: Sample arrays.
    """
    black_line_mtx = np.array([[0,2,0,0],[0,0,0,0],[0,0,0,0],[2,0,0,0]])
    red_line_mtx = np.array([[0,0,2,0],[0,0,0,0],[2,0,0,0],[0,0,0,0]])
    b2 = np.array([[0,2,3,4],[5,6,7,8],[0,0,0,0],[2,0,0,0]])
    return (black_line_mtx, red_line_mtx, b2)

def mkdir_if_dne(path: str):
    """Make directory if it does not exist.

    Args:
        path (str): Path to directory.
    """
    isExist = os.path.exists(path)
    if not isExist:
        os.makedirs(path)
    return

def get_edges(input_mtx: np.array) -> dict:
    """Determine what edges are connect, based on matrix elements

    Args:
        input_mtx (np.array): Matrix describing connected elements.

    Returns:
        dict: Ordered dictionary with keys of nodes in connected order and values of "weights"/"number of arrows".
    """
    edge_labels_dict = {}
    for i in range(len(input_mtx)):
        for j in range(len(input_mtx[i])):
            if i != j:
                number_of_arrows = input_mtx[i][j]
                if number_of_arrows != 0:
                    start_node = i+1
                    end_node = j+1
                    edge_labels_dict[(start_node, end_node)] = int(number_of_arrows)
    return edge_labels_dict

def set_plotting_style(style="default"):
    """(Unused function.) Set plot style.  Does not work with nx.

    Args:
        style (str, optional): Style for plots. Defaults to "default".
    """
    plt.style.use(style)
    return

def draw_edges_and_labels(G: nx.DiGraph, pos: dict, edge_labels_dict: dict, color: str, font_size=12, node_color="yellow", node_size=500, label_pos=0.1, **kwargs):
    """Draw the connected nodes.

    Args:
        G (nx.DiGraph): networkx graph.
        pos (dict): Positions of nodes.
        edge_labels_dict (dict): Ordered dictionary with keys of nodes in connected order and values of "weights"/"number of arrows".
        color (str): Edge and label's font color.
        font_size (int, optional): Font size of label. Defaults to 12.
        node_color (str, optional): Color of nodes. Defaults to "yellow".
        node_size (int, optional): Node size. Defaults to 500.
        label_pos (float, optional): Position of edge label along edge (0=head, 0.5=center, 1=tail). Defaults to 0.1.
    """
    nx.draw(
        G, pos, edge_color=color, width=1, linewidths=0.5,
        node_size=node_size, node_color=node_color, alpha=0.9,
        labels={node: node for node in G.nodes()},
        **kwargs
    )
    if (color=="red") | (color=="r"):
        nx.draw_networkx_edges(G, pos, arrowsize=1, edge_color=color)
        nx.draw_networkx_edge_labels(
            G, pos, label_pos=0.5,
            edge_labels=edge_labels_dict,
            font_color=color,
            font_size=font_size,
            **kwargs
        )
    else:
        nx.draw_networkx_edges(G, pos, arrowsize=20, edge_color=color)
        nx.draw_networkx_edge_labels(
            G, pos, label_pos=label_pos,
            edge_labels=edge_labels_dict,
            font_color=color,
            font_size=font_size,
            **kwargs
        )
    return

def add_edges_to_graph(G: nx.DiGraph, edge_labels_dict: dict, color: str):
    """Add edges to connected nodes on graph.

    Args:
        G (nx.DiGraph): networkx graph.
        edge_labels_dict (dict): Ordered dictionary with keys of nodes in connected order and values of "weights"/"number of arrows".
        color (str): Color of edges.
    """
    list_for_add_edges_from = list(edge_labels_dict.keys())
    G.add_edges_from(list_for_add_edges_from, color=color)
    return

def generate_quiver_diagram(input_mtx: np.array, black_edge_labels_dict: dict, black_color: str, red_edge_labels_dict: dict, red_color: str, figsize=(5,5), savefig=False):
    """Generate quiver diagrams.  Connected nodes are determined by input matricies. 

    Args:
        input_mtx (np.array): Matrix of nodes connected with black lines.
        black_edge_labels_dict (dict): Black edge ordered dictionary with keys of nodes in connected order and values of "weights"/"number of arrows".
        black_color (str): Color used for plot black edges and labels.
        red_edge_labels_dict (dict): Red edge ordered dictionary with keys of nodes in connected order and values of "weights"/"number of arrows".
        red_color (str): Color used for plot black edges and labels.
        figsize (tuple): Size of output graphic. Defaults to (12,8).
        savefig (str or False, optional): Path for saved figure.  When set to False, figure is shown but not saved. Defaults to False.
    """
    fig = plt.figure(figsize=figsize)

    # set_plotting_style("ggplot") # doesnt work with nx
    Gk = nx.DiGraph() # for black nodes / edges
    Gr = nx.DiGraph() # for red nodes / edges
    
    # NOTE: shows connected nodes...ALSO SHOWS UNCONNECTED NODES (if they exist)
    nodes = np.arange(1, len(input_mtx)+1).tolist()
    Gk.add_nodes_from(nodes)

    # # NOTE: ONLY SHOWS CONNECTED NODES
    # list_for_add_edges_from = list(edge_labels_dict.keys())
    # G.add_edges_from(list_for_add_edges_from)

    # add black edges
    add_edges_to_graph(Gk, black_edge_labels_dict, black_color)

    # add red edges
    add_edges_to_graph(Gr, red_edge_labels_dict, red_color)

    # choose node locations / layout
    pos = nx.circular_layout(Gk)

    # add edges and labels
    draw_edges_and_labels(Gk, pos, black_edge_labels_dict, black_color, label_pos=0.3)
    draw_edges_and_labels(Gr, pos, red_edge_labels_dict, red_color, label_pos=0.3)

    if savefig:
        plt.savefig(savefig)
        plt.close()
    else:
        plt.show()
    return

def generate_web_diagram(mlist):
    """Generate quiver diagrams.  Connected nodes are determined by input matricies. 

    Args:
        input_mtx (np.array): Matrix of nodes connected with black lines.
        black_edge_labels_dict (dict): Black edge ordered dictionary with keys of nodes in connected order and values of "weights"/"number of arrows".
        black_color (str): Color used for plot black edges and labels.
        red_edge_labels_dict (dict): Red edge ordered dictionary with keys of nodes in connected order and values of "weights"/"number of arrows".
        red_color (str): Color used for plot black edges and labels.
        figsize (tuple): Size of output graphic. Defaults to (12,8).
        savefig (str or False, optional): Path for saved figure.  When set to False, figure is shown but not saved. Defaults to False.
    """
    fig = plt.figure(figsize=(5,5))

    # set_plotting_style("ggplot") # doesnt work with nx
    Glist = [nx.DiGraph() for i in range(len(mlist))]
    
    # NOTE: shows connected nodes...ALSO SHOWS UNCONNECTED NODES (if they exist)
    nodes = np.arange(1, len(mlist)*(len(mlist[0])+1)).tolist()
    Glist[0].add_nodes_from(nodes)

    pos = nx.circular_layout(Glist[0])

    Colorlist = ['red','green','blue','black','yellow','orange','purple']
    for i,g in enumerate(Glist):
        rpos = {}
        for j in range(len(mlist[0])):
            rpos[j+1] = pos[i+j+1]
        add_edges_to_graph(g, get_edges(Mlist[i]), Colorlist[i])
        draw_edges_and_labels(g, rpos, {}, Colorlist[i], label_pos=0.3,node_color='blue')

    plt.show()
    return

def generate_readme(rlist,path,modeln,tweb):
    f= open(path+'README.md','w')
    f.write('# Model '+modeln.split('model')[-1]+' #\n')
    for r in rlist:
        if len(rlist)>5:
            f.write(f'\n|<img src="'+r[-1]+ f'" width="100" height="100"> |')
        else:
            f.write(f'\n|<img src="'+r[-1]+ f'" width="200" height="200"> |')
        phase = r[-1].split('_')[-1]
        phase = int(phase.split('.')[0])+1
        phase = 'Phase '+str(phase)+'|\n'
        f.write('\n|---|\n|'+phase)
    f.write('\n---\n')
    cellsize = 0
    for i in tweb:
        for j in i:
            if len(j)>cellsize:
                cellsize = len(j)
    webtext = '## Web Table ##\n---\n'
    webtext += '||'
    for i in range(len(rlist)):
        webtext += 'Phase '+str(i+1)+'|'
    webtext += '\n'
    for i in range(len(rlist)+1):
        webtext += '|---'
    webtext += '|'
    for i,t in enumerate(tweb):
        webtext+='\nPhase ' + str(i+1)
        for j in t:
            webtext += '|' + str(j)[1:-1]
        webtext += '|'

    f.write(webtext)
    f.close()
    return

def plot_web(X: np.array, F: np.array, model_sub_path = "model"):
    """Plot results.

    Args:
        X (np.array): X array for black edges.
        F (np.array): F array for red edges.
        model_sub_path (str, optional): Path and figure prefix used for saving images. Defaults to "model".
    """

    dwebs, twebs, M = FindPhases(X, F)

    if len(dwebs)>=0:
        return
    
    readmequeue = []

    twebtable = [[[] for i in range(len(dwebs))] for j in range(len(dwebs))]
    for i,t in enumerate(twebs):
        twebtable[M[i][0]][M[i][1]] += [t[-1]]

    for i,dweb in enumerate(dwebs):
            black_line_mtx, red_line_mtx = dweb[0],dweb[1]
            # black_line_mtx, red_line_mtx = Triality(X,F,4)

            # generate dictionaries of edge data, for each matrix
            k_edge_labels_dict = get_edges(black_line_mtx)
            red_edge_labels_dict = get_edges(red_line_mtx)

            # set path and name for saved figures
            fig_path = "./figs"
            
            mkdir_if_dne(fig_path)
            mkdir_if_dne(f"{fig_path}/{model_sub_path}")

            _savefig_ = f"{fig_path}/{model_sub_path}/{model_sub_path}_phase_{i}.png"
            readmequeue += [('Phase '+str(i),f"./{model_sub_path}_phase_{i}.png")]
            generate_quiver_diagram(black_line_mtx, k_edge_labels_dict, "k", red_edge_labels_dict, red_color="r", savefig=_savefig_)
    
    # for i,tweb in enumerate(twebs):
    #         readmequeue += [((M[0],M[1],tweb[-1]),_savefig_)]
    #      for j, tw in enumerate(tweb):
    #         if j ==2:
    #             break
    #         black_line_mtx, red_line_mtx = tw[0],tw[1]
    #         # black_line_mtx, red_line_mtx = Triality(X,F,4)

    #         # generate dictionaries of edge data, for each matrix
    #         k_edge_labels_dict = get_edges(black_line_mtx)
    #         red_edge_labels_dict = get_edges(red_line_mtx)

    #         # set path and name for saved figures
    #         fig_path = "./figs"
            
    #         mkdir_if_dne(fig_path)
    #         mkdir_if_dne(f"{fig_path}/{model_sub_path}")

    #         if j ==0:
    #             label = "Phases_" +str(M[i])+"_Node_" + str(i) + 'A'+str(tweb[-1])
    #         if j ==1:
    #             label = "Phases_" +str(M[i])+"_Node_" + str(i) + 'B'+str(tweb[-1])
    #         _savefig_ = f"{fig_path}/{model_sub_path}/{model_sub_path}_Tweb_"+label+".png"

    #         generate_quiver_diagram(black_line_mtx, k_edge_labels_dict, "k", red_edge_labels_dict, red_color="r", savefig=_savefig_)
    generate_readme(readmequeue,f"{fig_path}/{model_sub_path}/",model_sub_path,twebtable)

    return


if __name__ == "__main__":
    for phase in range(18):
        model_name = "model"+str(phase+1)
        print('\n'+"Model "+str(phase+1))
        X, F = test_data(model_name)
        anomaly = False
        for i in range(len(X)):
            chirals = np.sum(X[i])+np.sum(np.transpose(X)[i])
            fermis = np.sum(F[i])
            if chirals-fermis !=2:
                print(chirals,fermis,i+1)
                anomaly = True

        if not anomaly:
            plot_web(X, F, model_name)

# %%

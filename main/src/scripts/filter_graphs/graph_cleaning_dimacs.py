################################################################
# dependencies: networkx
#
# Script that reads DIMACS files (extensions .clq, .col,
# or any file containing DIMACS format "p edge" + "e u v")
# from the INPUT_DIR and converts them to NetworkX graphs.
#
# The script writes to OUTPUT_DIR a .txt file containing:
#     num_vertices num_edges
#     u v
#     u v
#
# Vertices are renumbered to a consecutive 0-based labeling.
#
################################################################

import os
import networkx as nx

# Directories
INPUT_DIR = "BASE"
OUTPUT_DIR = "base_final"

def ensure_dir(path):
    if not os.path.exists(path):
        os.makedirs(path)


def read_dimacs_graph(path):
    """Read a graph in DIMACS (edge/clique) format.

    Returns:
        (G, num_vertices, num_edges)
    """
    G = nx.Graph()
    num_vertices = None
    num_edges = None

    with open(path, "r") as f:
        for line in f:
            line = line.strip()
            if not line:
                continue

            if line.startswith("c"):
                # comment line, skip
                continue

            parts = line.split()

            if parts[0] == "p":
                # p edge V E
                _, _, V, E = parts
                num_vertices = int(V)
                num_edges = int(E)

            elif parts[0] == "e":
                # e u v
                _, u, v = parts
                u = int(u)
                v = int(v)

                G.add_edge(u, v)
    return G, num_vertices, num_edges


def converter_dimacs_para_txt():
    ensure_dir(OUTPUT_DIR)

    for root, _, files in os.walk(INPUT_DIR):
        for file in files:

            if not file.endswith((".clq", ".col", ".txt", ".dimacs")):
                continue

            caminho_entrada = os.path.join(root, file)
            nome_base = os.path.splitext(file)[0]
            caminho_saida = os.path.join(OUTPUT_DIR, f"{nome_base}.txt")

            print(f"Converting {file} -> {caminho_saida}")
            try:
                G, numV, numE = read_dimacs_graph(caminho_entrada)
                # remove self-loops
                G.remove_edges_from(nx.selfloop_edges(G))

                # ensure simple graph
                if isinstance(G, nx.MultiGraph):
                    G = nx.Graph(G)

                # relabel nodes to consecutive 0-based
                mapping = {old: new for new, old in enumerate(sorted(G.nodes()))}
                G = nx.relabel_nodes(G, mapping)
                
                # write header and edge list
                with open(caminho_saida, "w") as f_out:
                    f_out.write(f"{G.number_of_nodes()} {G.number_of_edges()}\n")

                    for u, v in G.edges():
                        f_out.write(f"{u} {v}\n")

            except Exception as e:
                print(f"Error processing {file}: {e}")

    print("\nConversion completed successfully!")


if __name__ == "__main__":
    converter_dimacs_para_txt()

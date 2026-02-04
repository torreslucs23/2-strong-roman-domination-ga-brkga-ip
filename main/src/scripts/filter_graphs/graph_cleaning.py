import os
import networkx as nx
from scipy.io import mmread

INPUT_DIR = "descompactados"
OUTPUT_DIR = "base_final"

def ensure_dir(path):
    if not os.path.exists(path):
        os.makedirs(path)

def converter_mtx_para_txt():
    ensure_dir(OUTPUT_DIR)

    for root, _, files in os.walk(INPUT_DIR):
        for file in files:
            if file.endswith(".mtx"):
                input_path = os.path.join(root, file)
                base_name = os.path.splitext(file)[0]
                output_path = os.path.join(OUTPUT_DIR, f"{base_name}.txt")

                print(f"Converting {file} -> {output_path}")

                try:
                    matriz = mmread(input_path).tocsr()

                    if matriz.shape[0] != matriz.shape[1]:
                        print(f"Error: matrix {file} is not square")
                        continue

                    G = nx.from_scipy_sparse_array(matriz)

                    if isinstance(G, nx.MultiGraph):
                        G = nx.Graph(G)

                    G.remove_edges_from(nx.selfloop_edges(G))

                    mapping = {old_label: new_label for new_label, old_label in enumerate(sorted(G.nodes()))}
                    G = nx.relabel_nodes(G, mapping)

                    with open(output_path, "w") as f_out:
                        for u, v in G.edges():
                            f_out.write(f"{u} {v}\n")

                except Exception as e:
                    print(f"Error processing {file}: {e}")

    print("\nConversion completed successfully!")


if __name__ == "__main__":
    converter_mtx_para_txt()

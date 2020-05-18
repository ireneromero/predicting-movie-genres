import argparse
import networkx as nx
from node2vec import Node2Vec

def parse_args():
    parser = argparse.ArgumentParser()

    parser.add_argument('--input', default = 'data/movies.edgelist', help='Input edges list path')
    parser.add_argument('--output', default = 'data/movies.emb', help='Output embedding file')

    return parser.parse_args()

def main(args):

    DIMENSION = 100
    NUM_WALKS = 10
    WALK_LENGTH = 80
    P_VALUE = 0.3
    WINDOW_CONTEXT = 10

    # Create graph from edge list
    graph = nx.read_edgelist(args.input, delimiter=",")
    node2vec = Node2Vec(graph, dimensions=DIMENSION, walk_length=WALK_LENGTH, num_walks=NUM_WALKS, p=P_VALUE)
    model = node2vec.fit(window=WINDOW_CONTEXT)
    model.wv.save_word2vec_format(args.output)

if __name__ == "__main__":
	args = parse_args()
	main(args)

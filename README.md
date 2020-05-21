# predicting-movie-genres
Repository containing my attempt to predict movie genres using:
- Movies database: Neo4J 
- Embedding Technique: Node2Vec
- Multi-label classification models (ML): sklearn & skmultilearn
- Multi-label classification models (using a neural net): PyTorch


Steps:
1) Connect to Neo4J database using library neo4j and write the edge list to a csv file (src/01_get_data_from_neo4j.py)
2) Learn node embeddings using Node2Vec technique (src/01_learn_movie_embeddings.py)
3) Write the obtained movie embeddings to Neo4J (notebooks/03_Embeddings_to_Neo4J_Data_Preparation)
4) Prepare data [movie_id, embedding, genre] (notebooks/03_Embeddings_to_Neo4J_Data_Preparation)
5) Build the classification models (notebooks/04_Classification_Model)
6) Build the classification models using a neural net (notebooks/05_Neural_Network)

TODO: [embeddings] Since node2vec does not deal easily with dynamic graphs (when a new node is added to the graph, node2vec needs to recompute the embeddings -> computationally expensive), try a graph deep learning method (GCN) to learn the embeddings

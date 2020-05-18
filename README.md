# predicting-movie-genres
Repository containing my attempt to predict movie genres using:
- Neo4J: Movies database 
- Node2Vec: Embedding Computation
- Classification models

Steps:
1) Connect to Neo4J database using library neo4j and write the edge list to a csv file (src/01_get_data_from_neo4j.py)
2) Learn movie embeddings using Node2Vec technique (src/01_learn_movie_embeddings.py)
3) Write the obtained embeddings to Ne4J (notebooks/03_Embeddings_to_Neo4J_Data_Preparation)
4) Prepare data [movie_id, embedding, genre] (notebooks/03_Embeddings_to_Neo4J_Data_Preparation)
5) Build the classification model (notebooks/04_Classification_Model)

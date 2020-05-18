import csv
from neo4j import GraphDatabase, basic_auth


driver = GraphDatabase.driver("bolt://34.201.68.240:33498", auth=("neo4j", "hickory-approval-forties"))

with driver.session() as session, open("data/movies.edgelist", "w") as edges_file:
    result = session.run("""
    MATCH (m:Movie)--(other)
    RETURN id(m) AS source, id(other) AS target
    """)

    writer = csv.writer(edges_file, delimiter=",")

    for row in result:
        writer.writerow([row['source'], row['target']])
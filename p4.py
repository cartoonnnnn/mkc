docker start neo4j-container || docker run -d -p 7474:7474 -p 7687:7687 --name neo4j-container -e NEO4J_AUTH=neo4j/password neo4j
docker exec -it neo4j-container cypher-shell -u neo4j -p password

CREATE (:User {UserID:1, Username:'Alice'}),
       (:User {UserID:2, Username:'Bob'}),
       (:User {UserID:3, Username:'Jane'}),
       (:User {UserID:4, Username:'Tom'}),
       (:User {UserID:5, Username:'Emma'}),
       (:User {UserID:6, Username:'Liam'});

MATCH (a:User {Username:'Alice'}), (b:User {Username:'Bob'})
CREATE (a)-[:FOLLOWS]->(b);

MATCH (a:User {Username:'Jane'}), (b:User {Username:'Alice'})
CREATE (a)-[:FOLLOWS]->(b);

MATCH (a:User {Username:'Tom'}), (b:User {Username:'Alice'})
CREATE (a)-[:FOLLOWS]->(b);

MATCH (a:User {Username:'Emma'}), (b:User {Username:'Bob'})
CREATE (a)-[:FOLLOWS]->(b);

MATCH (a:User {Username:'Liam'}), (b:User {Username:'Alice'})
CREATE (a)-[:FOLLOWS]->(b);

MATCH (a:User {Username:'Liam'}), (b:User {Username:'Bob'})
CREATE (a)-[:FOLLOWS]->(b);

MATCH (u:User) RETURN u;

MATCH (:User {Username:'Jane'})-[:FOLLOWS]->(u:User) RETURN u;

MATCH (u:User) RETURN u ORDER BY u.Username ASC;

MATCH (u:User)-[:FOLLOWS]->(:User {Username:'Alice'}),
      (u)-[:FOLLOWS]->(:User {Username:'Bob'})
RETURN u;

MATCH (u:User)<-[:FOLLOWS]-(f:User)
RETURN u, COUNT(f) AS followers
ORDER BY followers DESC;

MATCH (u:User)
RETURN u
LIMIT 5;

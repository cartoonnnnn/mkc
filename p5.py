docker start neo4j-container
docker exec -it neo4j-container cypher-shell -u neo4j -p password

CREATE (:User {UserID:1, Username:'John'}),
       (:User {UserID:2, Username:'Alice'}),
       (:User {UserID:3, Username:'Bob'}),
       (:User {UserID:4, Username:'Emma'}),
       (:User {UserID:5, Username:'Liam'});

CREATE (:Movie {MovieID:1, Title:'Inception'}),
       (:Movie {MovieID:2, Title:'The Matrix'}),
       (:Movie {MovieID:3, Title:'Interstellar'}),
       (:Movie {MovieID:4, Title:'Avatar'}),
       (:Movie {MovieID:5, Title:'Titanic'});

MATCH (u:User {Username:'John'}), (m:Movie {Title:'Inception'}) CREATE (u)-[:LIKES]->(m);
MATCH (u:User {Username:'John'}), (m:Movie {Title:'The Matrix'}) CREATE (u)-[:LIKES]->(m);
MATCH (u:User {Username:'Alice'}), (m:Movie {Title:'Inception'}) CREATE (u)-[:LIKES]->(m);
MATCH (u:User {Username:'Bob'}), (m:Movie {Title:'The Matrix'}) CREATE (u)-[:LIKES]->(m);
MATCH (u:User {Username:'Emma'}), (m:Movie {Title:'Inception'}) CREATE (u)-[:LIKES]->(m);
MATCH (u:User {Username:'Liam'}), (m:Movie {Title:'The Matrix'}) CREATE (u)-[:LIKES]->(m);
MATCH (u:User {Username:'Liam'}), (m:Movie {Title:'Inception'}) CREATE (u)-[:LIKES]->(m);

MATCH (:User {Username:'John'})-[:LIKES]->(m:Movie) RETURN m;
MATCH (u:User)-[:LIKES]->(:Movie {Title:'Inception'}) RETURN u;
MATCH (m:Movie) RETURN m ORDER BY m.Title ASC;
MATCH (u:User)-[:LIKES]->(:Movie {Title:'The Matrix'}),(u)-[:LIKES]->(:Movie {Title:'Inception'}) RETURN u;
MATCH (m:Movie)<-[:LIKES]-(u:User) RETURN m, COUNT(u) AS likes ORDER BY likes DESC LIMIT 1;
MATCH (u:User)-[:LIKES]->(m:Movie) RETURN u, COUNT(m) AS totalLikes ORDER BY totalLikes DESC LIMIT 5;



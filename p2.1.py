sudo apt update
sudo apt install docker.io -y
sudo service docker start
docker --version

sudo docker run -d \
-p 5984:5984 \
-e COUCHDB_USER=admin \
-e COUCHDB_PASSWORD=admin123 \
--name couchdb-container \
couchdb

curl -X PUT http://admin:admin123@localhost:5984/studentdb

curl -X POST http://admin:admin123@localhost:5984/studentdb/_bulk_docs \
-H "Content-Type: application/json" \
-d '{
  "docs": [
    {"SRN":1,"Sname":"Rahul","Degree":"BCA","Sem":2,"CGPA":7.0},
    {"SRN":2,"Sname":"Asha","Degree":"BCA","Sem":5,"CGPA":6.8},
    {"SRN":3,"Sname":"Priya","Degree":"BSc","Sem":4,"CGPA":8.2},
    {"SRN":4,"Sname":"Kiran","Degree":"BCA","Sem":5,"CGPA":6.4},
    {"SRN":5,"Sname":"Vikram","Degree":"BCom","Sem":3,"CGPA":7.2},
    {"SRN":6,"Sname":"Nisha","Degree":"BCA","Sem":2,"CGPA":7.8},
    {"SRN":7,"Sname":"Manoj","Degree":"BCA","Sem":4,"CGPA":5.9}
  ]
}'

curl -X GET http://admin:admin123@localhost:5984/studentdb/_all_docs?include_docs=true

curl -X POST http://admin:admin123@localhost:5984/studentdb/_find \
-H "Content-Type: application/json" \
-d '{"selector":{"Degree":"BCA"}}'

curl -X POST http://localhost:5984/studentdb/_find \
-H "Content-Type: application/json" \
-d '{"selector":{},"sort":[{"Sname":"asc"}]}'

curl -X POST http://admin:admin123@localhost:5984/studentdb/_find \
-H "Content-Type: application/json" \
-d '{"selector":{},"limit":5}'

curl -X POST http://admin:admin123@localhost:5984/studentdb/_find \
-H "Content-Type: application/json" \
-d '{"selector":{"SRN":{"$in":[5,6,7]}}}'

curl -X POST http://admin:admin123@localhost:5984/studentdb/_find \
-H "Content-Type: application/json" \
-d '{"selector":{"Sname":"Rahul"},"fields":["Degree"]}'

curl -X POST http://admin:admin123@localhost:5984/studentdb/_find \
-H "Content-Type: application/json" \
-d '{"selector":{"SRN":{"$in":[5,6,7]}},"sort":[{"CGPA":"desc"}]}'

curl -X POST http://admin:admin123@localhost:5984/studentdb/_find \
-H "Content-Type: application/json" \
-d '{"selector":{"Degree":"BCA","CGPA":{"$gt":6,"$lt":7.5}}}'

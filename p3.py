sudo apt update
sudo apt install couchdb -y
sudo service couchdb start

curl -X POST http://admin:admin123@127.0.0.1:5984/librarydb \
-H "Content-Type: application/json" \
-d '{"ISBN":"101","Title":"The Great Gatsby","Author":"F. Scott Fitzgerald","Genre":"Fiction","PublicationYear":1925,"CopiesAvailable":5,"Rating":4.5}'

curl -X POST http://admin:admin123@127.0.0.1:5984/librarydb \
-H "Content-Type: application/json" \
-d '{"ISBN":"102","Title":"To Kill a Mockingbird","Author":"Harper Lee","Genre":"Fiction","PublicationYear":1960,"CopiesAvailable":4,"Rating":4.8}'

curl -X POST http://admin:admin123@127.0.0.1:5984/librarydb \
-H "Content-Type: application/json" \
-d '{"ISBN":"103","Title":"1984","Author":"George Orwell","Genre":"Dystopian","PublicationYear":1949,"CopiesAvailable":6,"Rating":4.7}'

curl -X POST http://admin:admin123@127.0.0.1:5984/librarydb \
-H "Content-Type: application/json" \
-d '{"ISBN":"104","Title":"Moby Dick","Author":"Herman Melville","Genre":"Fiction","PublicationYear":1851,"CopiesAvailable":3,"Rating":4.0}'

curl -X POST http://admin:admin123@127.0.0.1:5984/librarydb \
-H "Content-Type: application/json" \
-d '{"ISBN":"105","Title":"The Alchemist","Author":"Paulo Coelho","Genre":"Fiction","PublicationYear":1988,"CopiesAvailable":7,"Rating":4.2}'

curl -X POST http://admin:admin123@127.0.0.1:5984/librarydb \
-H "Content-Type: application/json" \
-d '{"ISBN":"106","Title":"Sapiens","Author":"Yuval Noah Harari","Genre":"Non-Fiction","PublicationYear":2011,"CopiesAvailable":5,"Rating":4.6}'

curl -X GET http://admin:admin123@127.0.0.1:5984/librarydb/_all_docs?include_docs=true


curl -X POST http://admin:admin123@127.0.0.1:5984/librarydb/_find \
-H "Content-Type: application/json" \
-d '{"selector":{"Genre":"Fiction"}}'

curl -X POST http://admin:admin123@127.0.0.1:5984/librarydb/_index \
-H "Content-Type: application/json" \
-d '{
"index": {
"fields": ["Title"]
},
"name": "title-index",
"type": "json"
}'

curl -X POST http://admin:admin123@127.0.0.1:5984/librarydb/_find \
-H "Content-Type: application/json" \
-d '{
"selector": {},
"sort": [{"Title":"asc"}]
}'

curl -X POST http://admin:admin123@127.0.0.1:5984/librarydb/_find \
-H "Content-Type: application/json" \
-d '{"selector":{},"limit":3}'

curl -X POST http://admin:admin123@127.0.0.1:5984/librarydb/_find \
-H "Content-Type: application/json" \
-d '{"selector":{},"skip":3,"limit":3}'

curl -X POST http://admin:admin123@127.0.0.1:5984/librarydb/_find \
-H "Content-Type: application/json" \
-d '{"selector":{"Title":"The Great Gatsby"},"fields":["Author"]}'


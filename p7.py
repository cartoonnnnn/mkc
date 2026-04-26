sudo apt update
sudo apt install redis-server -y
sudo service redis-server start
redis-cli

SET employee:1 '{"Name":"Rahul","Department":"HR","Position":"Manager","Salary":60000}'
SET employee:2 '{"Name":"Anita","Department":"Finance","Position":"Analyst","Salary":55000}'
SET employee:3 '{"Name":"Kiran","Department":"HR","Position":"Executive","Salary":48000}'
SET employee:4 '{"Name":"Sneha","Department":"IT","Position":"Developer","Salary":70000}'
SET employee:5 '{"Name":"Arjun","Department":"HR","Position":"Assistant","Salary":52000}'

SADD dept:HR employee:1 employee:3 employee:5
SADD dept:Finance employee:2
SADD dept:IT employee:4

ZADD salary_index 60000 employee:1
ZADD salary_index 55000 employee:2
ZADD salary_index 48000 employee:3
ZADD salary_index 70000 employee:4
ZADD salary_index 52000 employee:5

SMEMBERS dept:HR

ZRANGEBYSCORE salary_index 50000 +inf

SET employee:3 '{"Name":"Kiran","Department":"HR","Position":"Senior Executive","Salary":48000}'

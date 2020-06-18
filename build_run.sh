docker build -t maharshi_postman .

docker run --name postgres-0 \
-p 54320:5432 \
-e POSTGRES_USERNAME=postgres \
-e POSTGRES_PASSWORD=postgres \
-e POSTGRES_DB=postman \
-d postgres

docker run maharshi_postman

python codes/CSVtoDB.py -c codes/configurations/configurations.txt


docker exec -it postgres-0 psql -U postgres

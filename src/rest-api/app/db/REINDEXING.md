# Reindexing steps

1. Add new indexes to setup.py
  * `MongoClient["balanced"]["COLLACTION_NAME"].create_index([("FIELD_NAME", "INDEX_TYPE")])`
2. Rebuild rest-api docker image
  * `docker-compose build`
3. Stop icon-etl
  * `docker-compose stop icon-etl`
4. Stop connect
  * `docker-compose stop connect`
5. Restart rest-api container
  * `docker-compose up -d rest-api`
6. Wait and check for indexes in the mongo cli
  * `docker-compose exec mongodb mongo -u USERNAME -p PASSWORD`
  * `use balanced`
  * `db["COLLECTION_NAME"].getIndexes()`
7. Restart connect
  * `docker-compose up -d connect`
8. Restart kafka-connect-init and wait for it to `exit 0` (might take up to a minute or so)
  * `docker-compose up kafka-connect-init`
9. Restart icon-etl
  * `docker-compose up -d icon-etl`

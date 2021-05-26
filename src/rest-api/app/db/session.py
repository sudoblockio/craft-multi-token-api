import pymongo

from app.core.config import settings

MongoClient = pymongo.MongoClient(
    "mongodb://{user}:{pas}@{server}".format(
        user=settings.MONGO_USERNAME,
        pas=settings.MONGO_PASSWORD,
        server=settings.MONGO_SERVER,
    )
)

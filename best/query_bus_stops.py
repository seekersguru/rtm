# db.bus_stops.find({p:{$near:[19.116117,72.831718], $maxDistance: 0.0005 }}).count()
from pymongo import MongoClient
client = MongoClient('localhost', 27017)
from bson.son import SON
db=client.best # Create db name best
bus_stops = db.bus_stops
query = {"p": SON([("$near", [18.940708,72.833214]), ("$maxDistance", .0005)])}

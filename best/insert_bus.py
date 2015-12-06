from pymongo import MongoClient
client = MongoClient('localhost', 27017)
db=client.best # Create db name best
collection = db.bus_stops
#https://docs.google.com/spreadsheets/d/1JBUJa4vI0UT_35hs-6YvbjqDX_PdZt6V_e46buT5psk/edit#gid=665000&vpid=A1
f=open("bus_stops.tsv")
records=f.readlines()
#StopName    RouteNo    Lat    Long    StopNo
mapping={0:("StopName","n"),1:("RouteNo","r"),2:("Lat","l"),3:("Long","o"),4:("StopNo","s")}
for record in records:
    record_split=[e.strip() for e in record.split("\t") ]
    collection.insert_one({"n":str(record_split[0]),
                           "r":str(record_split[1]),
                           "p":[float(record_split[2]),float(record_split[3])],
                           "s":record_split[4]
                           }
                          )
    

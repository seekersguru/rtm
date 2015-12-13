from pymongo import MongoClient
client = MongoClient('localhost', 27017)
db = client['bestpis']
collection = db["bus_stops"]
f=open("lat_long.tsv")
lines=f.readlines()
cols=[e.strip().lower().replace(" ","_") for e in lines[0].split("\t")]
cols_mapping=dict([(i,cols[i]) for i in range(len(cols))])

for line in lines[1:]:
    values= line.split("\t")
    try:
        record=dict([(cols_mapping[i],values[i].strip()) for i in range(len(values))]) 
        record['latlong'] = [float(e) for e in record['latlong'].split(",")]
        if record['latlong'][0] < -180 or record['latlong'][0] > 180:
            raise Exception("Lat not in [-180,180]")
        if record['latlong'][1] < -180 or record['latlong'][1] > 180:
            raise Exception("Lat not in [-180,180]")
        if not isinstance(record['latlong'], list) and isinstance(record['latlong'][0], float) and isinstance(record['latlong'][1], float) :
            raise Exception("Invalid lat long")
    except :
        print record['latlong'] , record["stopname"]
        #import pdb;pdb.set_trace()
    collection.insert(record) 


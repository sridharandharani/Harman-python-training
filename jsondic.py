import json as j

data = {"name" : "sridharan","status" : "student" }

jsondata = j.dumps(data) #changing dict to json

myjsondata = j.loads(jsondata)  #parsing

print(myjsondata["name"])
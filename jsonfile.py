import json as j

data = ' {"name" : "sridharan","status" : "student" } '

myjsondata = j.loads(data)  #parsing

print(myjsondata["name"])
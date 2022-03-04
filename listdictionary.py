student = [
    {"name" : "Sridharan" ,
     "marks": [ { "eng" : 10 ,
                "sci" : 15,},]
     },

     { "name" : "Sridharan" ,
     "marks": [ { "eng" : 10 ,
                "sci" : 15,}, ]
       },
]
for i in student:
    print(i["name"])
    for j in i["marks"]:
        print (j["eng"])
        print(j["sci"])

import pymongo
myclient = pymongo.MongoClient("mongodb:// localhost:http://localhost/")
mydb = myclient["mydatabase"]
mycol = mydb["Customer"]
my_dict = {"name" : "John", "address" : "Royal Residency"}
ins_id = mycol.insert_one(my_dict)
# insert one has the property insert_id which holds id of the inserted document
print(ins_id.inserted_id)
my_dict_many = {
    {"name" : "John1", "address" : "Royal Residency"},
    {"name" : "John2", "address" : "Royal Residency"},
    {"name" : "John3", "address" : "Royal Residency factory"},
    {"name" : "John4", "address" : "Royal Residency"},
    {"name" : "John5", "address" : "Royal Residency factory"},
    {"name" : "John6", "address" : "Royal Residency factory"}}

mycol.insert_many(my_dict_many)
# find query find_one, find_all, find
print(mycol.find_one())
for _ in mycol.find():
    print(_)

print(mycol.find({},{'address' : 'sRoyal Residency'}))
myquery = mycol.find({"address" : {"$gt" : "R"}})
myquery1 = mycol.find({"address" : {"$regex" : ".+factory"}}) # using regex
# using sort method for sorting result, sort -1 descending sort +1 ascending
myquery2 = mycol.find().sort("name", -1)

# delete delete_one(), delete_many()
myquery3 = mycol.delete(myquery1)

# droping table
mycol.drop()
# update update_one, update_many query , new_value
new_value = {"$set" : {"name" : "Parijat"}}
mycol.update_many(myquery1, new_value)

#limit for limiting result as in mysql
mycol.find().limit(2)

# create index 
mycol.create_index("address")




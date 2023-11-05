import pymongo
import os

files = os.listdir("Articles/") #Getting list of articles in the directory

client = pymongo.MongoClient("mongodb://localhost:27017")
db = client["FYP"]
collection = db["File_Score"] #Initialising the parameters to establish connection the MongoDB collection

def init_file_score():

    data = []
    cnt=0

    for i in files:
        data += [{"Name" : i , "File_Score" : 0}] #Initialising a list to store the file score of all the articles in the directory

        cnt+=1
        if(cnt==5000):
            break


    x = collection.insert_many(data) #Storing the list in the MongoDB collection

def update_file_score(file,score):

    query = {"Name": file}
    update = {"$inc": {"File_Score": score}}

    collection.update_one(query, update)

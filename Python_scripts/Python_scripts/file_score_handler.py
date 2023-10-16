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

    x = collection.insert_many(data) #Storing the list in the MongoDB collection

init_file_score()

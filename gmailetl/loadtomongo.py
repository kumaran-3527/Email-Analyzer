import pymongo
import transform
import extract

def CreateConnection():
    myclient = pymongo.MongoClient("mongodb://localhost:27017/")
    return myclient

def CreateDatabase(name):
    myclient = CreateConnection()
    mydb = myclient['gmailetl']
    return mydb
    


def CreateCollection():
    mydb = CreateDatabase("gmailetl")
    mycol = mydb['emails']
    return mycol

def InsertMails():
    mycol = CreateCollection()
    emails = extract.extract_emails()
    mails_inserted = 0
    for mail in emails:
        cleaned_emails = transform.clean_data(emails)
        x = mycol.insert_one(cleaned_emails)
    return x

def main():
    x = InsertMails()
    print("Inserted "+str(x.inserted_count)+" records")
    
if __name__ == "__main__":
    main()







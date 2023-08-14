
import numpy 
import string
import re

def clean_data(emails):
    

    
    cleaned_emails = []
    for mail in emails:
        sender = mail["Sender"]
        sub = mail["Subject"]   
        body = mail["Body"]
        clean_body = re.sub(r"<br\s*/?>", " ", body)
        clean_body = re.sub(r"<[^>]*>", " ", clean_body)
        clean_body = re.sub(r"\b(?![\w&]*&)[\w&]+\b ", " ", clean_body)
        clean_body = re.sub(r"(?<!\s),(?!\s) ", "", clean_body)
        clean_body = re.sub(r"&gt;", "", clean_body)
        clean_body = re.sub(r"\[.*?\]" ," ", clean_body)
        clean_body = re.sub(r"[\n*]" ," ", clean_body)
        
        dict = {"_id":mail["_id"] , "Sender" : sender , "Subject" : sub , "Body" : clean_body , "TimeRecieved" : mail["TimeRecieved"]}
        cleaned_emails.append(dict)
    return cleaned_emails


 
 


 


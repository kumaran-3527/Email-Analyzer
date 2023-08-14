import GmailService
from bs4 import BeautifulSoup
import email
import base64
import os.path
import pickle
from google.auth.transport.requests import Request
from google_auth_oauthlib.flow import InstalledAppFlow
from googleapiclient.discovery import build
import lxml
from datetime import datetime

def extract_emails():
    service = GmailService.get_service()
    sender_to_exclude = ["director@iitm.ac.in" , "english-personalized-digest@quora.com"]
    query1 = ' '.join([f'-from:{sender}' for sender in sender_to_exclude])
    query2 = 'is:unread'
    query = f'{query1} AND {query2}'
    result = service.users().messages().list(userId='me',q = query , maxResults =20).execute()
    messages = result.get('messages')
    mails = []
    index=0
    for msg in messages:
        txt = service.users().messages().get(userId='me', id=msg['id']).execute()
        internal_date = int(txt['internalDate']) / 1000
        email_time = datetime.fromtimestamp(internal_date)
        try:
            payload = txt['payload']
            headers = payload['headers']

            for d in headers:
                if d['name'] == 'Subject':
                    subject = d['value']
                if d['name'] == 'From':
                    sender = d['value']
        
    
            parts = payload.get('parts')[0]
            data = parts['body']['data']
            data = data.replace("-","+").replace("_","/")
            decoded_data = base64.b64decode(data)

            soup = BeautifulSoup(decoded_data,"lxml")
            body = soup.body()
            body = str(body)
            subject = str(subject)
            sender = str(sender)

            mydict = {"_id" : index,  "Sender": sender, "Subject": subject, "Body" : body ,"TimeRecieved" : email_time}
            mails.append(mydict)
        
        except:
            pass

    return mails






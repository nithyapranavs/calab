import pprint
from apiclient.discovery import build
from datetime import datetime, timedelta, date
import pickle
cred = pickle.load(open("credential.pkl","rb"))
service = build("calendar", "v3", credentials=cred)


calId = "0@group.calendar.google.com"
def create_event(name,date,st,et):
    #date = [yyyy, mm, dd]
    #st = [hr, min]
    start_time = datetime(int(date[0]), int(date[1]), int(date[2]), int(st[0]), int(st[1]), 0)#format: (year, month, date , hr , min , sec=0)
    end_time = datetime(int(date[0]), int(date[1]), int(date[2]), int(et[0]), int(et[1]), 0)
    timezone = 'Asia/Kolkata'
    event = {
            'summary' : name,
            'start' : {
                'dateTime' : start_time.strftime("%Y-%m-%dT%H:%M:%S"),
                'timeZone': timezone},
            'end': {
                'dateTime': end_time.strftime("%Y-%m-%dT%H:%M:%S"),
                'timeZone': timezone},
            }
    service.events().insert(calendarId=calId, body=event).execute()


def get_event():
    daate = date.today()
    timemin = str(daate) + "T00:00:00Z"
    result = service.events().list(calendarId=calId, timeZone="Asia/Kolkata",timeMin=timemin).execute() #timeMin = "2022-09-01T00:00:00Z"
    return result['items']

#all_event= get_event()

def delete_event(evntid):
    service.events().delete(calendarId=calId, eventId=evntid).execute()

#pp = pprint.PrettyPrinter(indent=4)
#pp.pprint(get_event()['start']['dateTime'])
#i['start']['dateTime'][:9]
#create_event("s",["2021","10","27"],["19","00"])

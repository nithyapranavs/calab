from tblib import Traceback
import ecal
import json
import calendar
import datetime

def date_range(start_date, end_date):
    # similar to range function but loops through dates
    current_date = start_date
    while current_date <= end_date:
        yield current_date
        current_date += datetime.timedelta(days=1)

def rm_event(dat):
    events = ecal.get_event()
    for i in events:
        try:
            d = i['start']['dateTime'][:10]
            if d == dat:
                ecal.delete_event(i['id'])
        except KeyError:
            continue


def add_event():
    with open(r"timetable.json") as f:
        tt = json.load(f)
    for n in range(14):
        d = datetime.date.today() + datetime.timedelta(days=n)
        day = str(d.strftime("%A")).lower()
        d = str(d)
        if day == "saturday" or day == "sunday":
            continue
        cls = tt[day]
        for i in cls:
            name = i[0]
            if name == "empty":
                continue
            da = d.split('-')
            print(name,i[1],i[2])
            ecal.create_event(name, da, i[1], i[2])

def AddSatEvent():
    dat = input("YYYY-MM-DD\nDate: ")
    #dat = datetime.datetime.strtime(dat,"%y-%m-%d")
    print("time table: ")
    days_mapping = {
        1: "Monday",
        2: "Tuesday",
        3: "Wednesday",
        4: "Thursday",
        5: "Friday"
    }

    for number, day in days_mapping.items():
        print(f"{number} - {day}")

    tday = int(input("Enter: "))
    with open(r"timetable.json") as f:
        tt = json.load(f)
    cls = tt[days_mapping[tday].lower()]
    dat = dat.split('-')
    for i in cls:
        name = i[0]
        print(name,i[1],i[2])
        ecal.create_event(name, dat, i[1], i[2])


def main():
    print("1. Schudling classes")
    print("2. Delete classes")
    print("3. Schudle saturday")
    a = int(input("Enter : "))
    if a == 1:
        add_event()
    elif a == 2:
        startDate = input("YYYY-MM-DD\nstart: ")
        endDate = input("End: ")

        start_date = datetime.datetime.strptime(startDate, "%Y-%m-%d")
        end_date = datetime.datetime.strptime(endDate, "%Y-%m-%d")

        for dat in date_range(start_date, end_date):
            rm_event((dat.strftime("%Y-%m-%d")))
    
    elif a == 3:
        AddSatEvent()
main()


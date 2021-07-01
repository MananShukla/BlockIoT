
from register import * # type: ignore
from adherence_helper import * # type: ignore
from solidity_helper import * # type: ignore
from blockchain import * # type: ignore
from oracle import * # type: ignore
from threading import Thread
import schedule

with open(r"/Users/manan/Documents/BlockIoT/Code/new_BlockIoT/.vscode/settings.json","r") as infile:
        settings = json.load(infile)
# Keywords such as BL_timestamp signify what type of data will be present there. 
config= {
    "first_name":"manan",
    "last_name":"shukla",
    "dob":"01-12-2001",
    "communication":{
        "phone":settings["personal phone number"],
        "email":"manan.shukla2001@gmail.com",
    },
    "api server": "http://localhost:8000/new_BlockIoT/server_data.json",
    "api parameters": {},
    "template":"adherence",
    "adherence":{
        "medication_name":"Albuterol",
        "Dosage":"90 mcg",
        "Times per day":"0"
    },
    "identifiers":{
        "BL_timestamp":"BL_pillstaken"
    },
}
config2 = {
    "first_name":"kavin",
    "last_name":"shukla",
    "dob":"01-12-2001",
    "communication":{
        "phone":"5162708383",
        "email":"manan.shukla2001@gmail.com"
    },
    "api server": "https://ripple-health.net/api/medication/000051",
    "api parameters": {},
    "template":"adherence",
    "manufacturer":"ripplehealth",
    "adherence":{
        "medication_name":"Vitamin D",
        "Dosage":"10 mg",
        "Times per day":"2"
    },
    "alerts":{
        "updates":"1",
        "reminders":"1",
        "daily_summary":"1",
        "long_term":"1",
    },
    "identifiers":{
        "BL_timestamp":"BL_pillstaken"
    }
}
#registration(config)
registration(config2)

#To view a patient's data...
patient_1 = {
    "first_name":"kavin",
    "last_name":"shukla",
    "dob":"01-12-2001"
}
def oracle_handler():
    while True:
        oracle()
        time.sleep(1)
        schedule.run_pending()
        time.sleep(1)

def retrieve():
    while True:
        time.sleep(1)
        some_data = dict()
        with open("new_BlockIoT/command.json") as f:
            some_data = json.load(f)
            f.close()
        if some_data != {}:
            retrieve_data(some_data)
            with open("new_BlockIoT/command.json","w") as f:
                json.dump({},f)
                f.close()
        time.sleep(1)

t1 = Thread(target=oracle_handler).start()
time.sleep(1)
t2 = Thread(target=retrieve).start()
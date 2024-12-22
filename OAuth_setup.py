import pickle
from google_auth_oauthlib.flow import InstalledAppFlow

def setup():
    scopes = ["https://www.googleapis.com/auth/calendar"]


    flow = InstalledAppFlow.from_client_secrets_file("client_id.json", scopes=scopes)

    cred = flow.run_local_server(port=0)

    with open("credential.pkl","wb") as f:
        pickle.dump(cred,f)
    print(cred)
setup()

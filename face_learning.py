import requests
import json
import logging
from faceAPI_IDs import SUBSCRIPTION_KEY
BASE_URL = "https://japaneast.api.cognitive.microsoft.com/face/v1.0"
GROUP_NAME = "Actresses"
import pandas as pd

def makeGroup():
    end_point = BASE_URL + "persongroups/" + GROUP_NAME
    payload = {
        "name": GROUP_NAME
    }
    headers = {
        # "Content-Type": "application/json",
        "Ocp-Apim-Subscription-Key": SUBSCRIPTION_KEY
    }
    r = requests.put(
        end_point,
        headers=headers,
        json=payload
    )
    print(r.text)

def makePerson(personName):
    end_point = BASE_URL + "persongroups/" + GROUP_NAME + "/persons"
    headers = {
        # "Content-Type": "application/json",
        "Ocp-Apim-Subscription-Key": SUBSCRIPTION_KEY
    }
    payload = {
        "name": personName
    }
    r = requests.post(
        end_point,
        headers=headers,
        json=payload
    )
    try:
        parsonID = r.json()["personID"]
    except Exception as e:
        personID = None
        print(r.json()["error"])
    return personID

def addFaceTo(personID, imgURL):
    if personID != None:
        end_point = BASE_URL + "persongroups/" + GROUP_NAME + "/persons/" + personID + "/persistedFaces"
        print(end_point)
        headers = {
            # "Content-Type": "application/json",
            "Ocp-Apim-Subscription-Key": SUBSCRIPTION_KEY
        }
        payload = {
            "url": imgURL
        }
        r = requests.post(
            end_point,
            headers=headers,
            json=payload
        )
        try:
            print("Successfully added face to person")
            persistedFaceID = r.json()
        except Exception as e:
            print("Failed to add a face to person")
            print(e)
            persistedFaceID = None
        return persistedFaceID
    else:
        print("personID is not set.")
        return None

def trainGroup(groupID):
    end_point = BASE_URL + "persongroups/" + GROUP_NAME + "/train"
    headers = {
        # "Content-Type": "application/json",
        "Ocp-Apim-Subscription-Key": SUBSCRIPTION_KEY
    }
    r = requests.put(
        end_point,
        headers=headers,
    )
    print(r.text)

def detectFace(imgURL):
    end_point = BASE_URL + "detect"
    headers = {
        # "Content-Type": "application/json",
        "Ocp-Apim-Subscription-Key": SUBSCRIPTION_KEY
    }
    payload = {
        "url": imgURL
    }
    r = repuests.post(
        end_point,
        json=payload,
        headers=headers
    )
    try:
        faceID = r.json()[0]["faceID"]
        print(f"faceID Found:{faceid}")
        return r.json()[0]
    except Exception as e:
        print(f"faceID not found:{e}")
        return None

def identifyPerson(faceID):
    end_point = BASE_URL + "identify"
    headers = {
        # "Content-Type": "application/json",
        "Ocp-Apim-Subscription-Key": SUBSCRIPTION_KEY
    }
    faceIDs = [faceID]
    payload = {
        "faceIds": faceIDs,
        "personGroupId": GROUP_NAME
    }
    r = requests.post(
        end_point,
        json=payload,
        headers=headers
    )
    print(r.text)

if __name__ == "__main__":
    df = pd.read_csv("final.csv", index_col=0)

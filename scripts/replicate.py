import os
import requests

s = "https://api.covid19india.org/csv/latest/state_wise.csv"


def getdata():
    return(requests.get(s).content)


def writedata():
    with open('data.csv', 'wb') as f:
        f.write(getdata())

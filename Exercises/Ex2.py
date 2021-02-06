import requests


def getKinoNumbersForFirstDateOfMonth():
    URL = "https://api.opap.gr/games/v1.0/1100/statistics"
    PARAMS = {'gameId': 1100, 'limit': 2, 'drawId': 1, 'drawRange': 1801, 'fromDate': "2021-02-01", 'toDate': "2021-02-02"}
    r = requests.get(url=URL, params=PARAMS)
    data = r.json()
    print("\n*******************DATA*********************\n" + str(data))
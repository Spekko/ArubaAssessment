import json
import requests
import requests_cache

class Functions:
    

    def __init__(self):
        requests_cache.install_cache()
        pass

    """
    Takes in one set of apscan_data as input.
    returns dictionary in the following format based on apscan_data
    {
        "considerIp": "false",
        "wifiAccessPoints": [
            {
                "macAddress": "xx:xx:xx:xx:xx:xx"
                "signalStrength": x
                "channel": x
            }, ...
        ]
    }
    """
    def parse(self, scanData):

        apscan = scanData["apscan_data"]

        post = {}
        post["considerIp"] = "false"
        post["wifiAccessPoints"] = []
        
        for item in apscan:
            buildPost = {
                "macAddress": item["bssid"],
                "signalStrength": item["rssi"],
                "channel": item["channel"]
            }
            post["wifiAccessPoints"].append(buildPost)

        return post

    """
    Takes in parsed data and sends request to googleapis geolocation API
    returns json object of the following form
    {
        "location": {
            "lat": x
            "lng": x
        },
        "accuracy": x
    }
    """
    def getLocation(self, scanData):

        data = json.dumps(scanData)

        URL = "https://www.googleapis.com/geolocation/v1/geolocate?key=AIzaSyAn5aF2aAGpTOZh3ZZT86vcfa-PSUIoxoI"


        try:
            post = requests.post(URL, data)
        except:
            return "could not complete post request"

        return post.json()



                   


if __name__ == "__main__":
    test = parseFile("single.json")
    test.parse()
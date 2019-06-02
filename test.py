import json
import requests
if __name__=="__main__":

    URL = "http://127.0.0.1:8080/scan"

    with open("scan.json") as f:
        data = json.load(f)
        fail = 0
        for scan in data:
            scanJson = json.dumps(scan)
            #print(scan)
            #print(scan["apscan_data"])

            try:
                post = requests.post(URL, json=scan)
                fail = 0
            except:
                print("could not complete post request")
                fail = 1
            if fail == 0:
                print(post.json())

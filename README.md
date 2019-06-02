# ArubaAssessment
Rest API that takes in apscan data as a post request and returns the location of the origin of the scan.

### Libraries required
install the following python libraries before use

`pip3 install flask flask-restful json requests requests-cache waitress`

### Usage
run the script rest.py `python3 rest.py`, the server will execute on http://127.0.0.1:8080 the URL for post request containing apscan data will be http://127.0.0.1:8080/scan

### Test
small test script which sends multiple apscan data sets contained in array this script serves the json file "scan.json" to the server. `pyhthon3 test.py`
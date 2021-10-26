## Assignment given by Aqua

#### Prerequisites:
NGINX docker webserver
used latest Python 3.9 version
Allure reports Docker to view the reports.. Steps mentioned below sections



### Installation via github
git clone  

pip install requirements.txt
create folders for reports




      docker run -p 5050:5050 -e CHECK_RESULTS_EVERY_SECONDS=3 -e KEEP_HISTORY=1 \
                 -v "/$(pwd)/reports:/app/allure-results" \
                 -v "/$(pwd)/allure-reports:/app/default-reports" \
                 frankescobar/allure-docker-service
                 
                 
                 
Tools used to develop this assignment:-

# Dockers used here are :

1.Nginx server 
2.Allure reports
## What i did as per the assignment:
 
 Developed test cases for GET and POST api REST calls for one for Pass and one for fail case.
 Used Allure framework to see the resultent Reports.
 Used pytest framework to create tests.
 Added command line option --browser to supply browser name. (default to chrome)
 
## Brief note on artifacts:
 Artifact Name | Description
 --------------|------------------
 conftest.py | pytest framework will use this file like configuration for tests. I have used to set fixture and get the 		browsername. Also this will construct User agent to mimic the browser type.
 api_status_codes.py| Used this as kind of global constants. (User agent details,other constants) 
 apicall.py| Low level REST api implementation for GET and POST. So any test test it can directly call this low level function call. 
 test_classes.py| Actual tests written here. Class TestApi is the main class  grouped all api methods(GET, POST) to NGINX webserver. 
 reports| this folder contains all  .json files which are used to generate allure reports 
 allure-reports| This folder contains all the actual allure reports. To view easily use the following command once (mentioned in installation section) . Thats it ,  Allure webserver from docker will keep checkig  for every 3 seconds for  updated reports there or not. If so it will take automatically and render it . You  just have to point the browser tab. No need any additional allure command to see the reports like (allure serve.. ). No need to remember any allure commands.
URL to view allure reports: http://localhost:5050/allure-docker-service/latest-report
                 
	 
###Installation steps:-
* Install NGINX webserver
```bash
docker pull nginx:latest
``` 
* Create   project folder  with any name
* Create directory name "main" and copy the all the given artificats  

 
* Create empty directory reports   under main  _(main/reports)_
*  Create empty directory allure-reports  under main. _( main/allure-reports)_
``` 
 (** Some this like below it should appear**)
 ```bash
 Projectfolder/main $ ls
  allure-reports  apicall.py  api_status_codes.py  conftest.py  __pycache__  reports  test_classes.py
 ```
 
Run the tests:
```bash
pytest  -sv test_classes.py -q     --browser "edge"  --alluredir="/home/kishore/RestAPi/main/reports"
``
 
 * Run the following docker command once , it will  pick up generated output .json files to render 
 ```bash
      docker run -p 5050:5050 -e CHECK_RESULTS_EVERY_SECONDS=3 -e KEEP_HISTORY=1 \
                 -v "/$(pwd)/reports:/app/allure-results" \
                 -v "/$(pwd)/allure-reports:/app/default-reports" \
                 frankescobar/allure-docker-service
 ```
 
To see the allure reports use the below url 

http://localhost:5050/allure-docker-service/latest-report

`






                 

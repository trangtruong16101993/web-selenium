#snapshot debug
SNAPSHOT_DEBUG = True  #means DO   take snapshot during the test run - CAUTION: your snapshot folder, eg. $CODE/_snapshot_ may consume lots of your volume, don't forget to clean it up after used
SNAPSHOT_DEBUG = False #means DONT take snapshot during the test run

#webdriver hub address
WEBDRIVER_REMOTE_HUB = 'http://52.221.196.28:4444/wd/hub' #use webdriver via selenium hub on port 4444 served from ip=52.221.196.28, eg. from AWS EC2 #note, we SHOULD NOT run this way due to 0) network I/O cost by AWS, 1) slow connection
WEBDRIVER_REMOTE_HUB = 'http://192.168.1.113:4444/wd/hub' #use webdriver via selenium hub on port 4444 served from ip=192.168.1.113, within LAN network
WEBDRIVER_REMOTE_HUB = ''                                 #use webdriver directly aka. no-hub
WEBDRIVER_REMOTE_HUB = 'http://localhost:4444/wd/hub'     #use webdriver via selenium hub on port 4444 locally

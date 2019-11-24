#basic path
import os ; CODE = APP_HOME = os.path.abspath(os.path.dirname(__file__))


#region browser name
class Browser:
    Chrome  = 'Chrome'
    Firefox = 'Firefox'
    Android = 'Android'
    iOS     = 'iOS'

BROWSERS = [
    Browser.Chrome,

    #TODO more browser support here
    # Browser.Firefox,
    # Browser.Android,
    # Browser.iOS,
]
#endregion browser name


##region snapshot folder

#snapshot flag - TRUE/False means DO/don't take snapshot during the run
SNAPSHOT_DEBUG = False

#the snapshot home
SNAPSHOT_HOME  = '%s/_snapshot_'       % APP_HOME
SNAPSHOT_VAULT = '%s/_snapshot_/vault' % APP_HOME

#timestamp as 'YYYYmm-dd HHMMss ms' ref. https://stackoverflow.com/a/18406412/248616
from datetime import datetime
timestamp = datetime.now().strftime("%Y%m%d-%H%M%S-%f")[:-3]

#prepare folder to store snapshot files for each run
SNAPSHOT_FOLDER = '%s/%s' % (SNAPSHOT_VAULT, timestamp)

##endregion snapshot folder



#webdriver config i.e. to use local/remote webdriver
WEBDRIVER_REMOTE_HUB = '' #empty value to use local hub

HOSTING_URL = 'https://release.gigacover.com'
##region load local config

#ensure exists
import os.path
assert os.path.exists('%s/config_local.py' % CODE), \
       'local config at $CODE/config_local.py is mandatory; please create one from $CODE/config_local.TEMPLATE.py'

#load it
from src.config_local import *

##endregion load local config

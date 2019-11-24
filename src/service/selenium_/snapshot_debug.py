##region initial

#add python path ref. http://flask.pocoo.org/docs/0.11/deploying/mod_wsgi/#creating-a-wsgi-file
import os, sys ; s=os.path.abspath(os.path.dirname(__file__)) ; APP_HOME=os.path.abspath('%s/..' % s)
sys.path.insert(0, APP_HOME)

#import from config
from src.config import SNAPSHOT_DEBUG, SNAPSHOT_FOLDER #TODO Why this required above path register i.e. APP_HOME

#snapshot counter
SNAPSHOT_COUNTER=0

##endregion initial


#taking snapshot util
def takeSnapshot(driver, prefix=None, suffix=None, forceSnapshot=False, printOutcome=False):
    if not forceSnapshot: #check if snapshot required (and not being forced to do so)
        if not SNAPSHOT_DEBUG: return #just do nothing when the flag is off

    #prepare filename
    global SNAPSHOT_COUNTER
    filename = '{SNAPSHOT_FOLDER}/{prefix}s{SNAPSHOT_COUNTER:02d}{suffix}.png'.format( #format number ref. https://stackoverflow.com/a/135157/248616
        SNAPSHOT_FOLDER  = SNAPSHOT_FOLDER,
        prefix           = '%s-' % prefix if prefix else '',
        suffix           = '-%s' % suffix if suffix else '',
        SNAPSHOT_COUNTER = SNAPSHOT_COUNTER,
    )

    #do take snapshot

    os.makedirs(SNAPSHOT_FOLDER, exist_ok=True)
    driver.get_screenshot_as_file(filename) ; SNAPSHOT_COUNTER += 1

    #printing
    if printOutcome: #only print snapshot when required
        from .logger import l, ld
        l('Snapshot taken at %s' % filename)

    return filename

import os,sys,unittest,logging
from pathlib import Path
_parentDir = Path(__file__).resolve().parents[1]
sys.path.append(os.path.join(_parentDir))

from modules import BooksAPI,Utils
#import logging,os,unittest


# Check the environment
env = os.environ.get('ENVIRONMENT')
if env == None:
    logging.info('No environment supplied. Hence defaulting to dev')
    env = 'dev'

# Source environment specific settings file
_settingsFile = os.path.join("../settings", "app.settings." + env + ".json")
util = Utils()
settings=util.getSettings(_settingsFile)
api = BooksAPI(settings)


# Test Case 1
class TestBooksApp(unittest.TestCase):

    def test_getSettings(self):
        _settingsFile = os.path.join("../settings", "app.settings." + env + ".json")
        util = Utils()
        settings = util.getSettings(_settingsFile)
        assert 'apiUrl' in settings
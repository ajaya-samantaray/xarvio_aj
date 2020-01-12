from modules import BooksAPI,Utils
import logging,os

# Create and configure logger
LOG_FORMAT = "%(asctime)s : %(levelname)s - %(message)s"
logging.basicConfig(filename="logs/start.py.log",
                    level = logging.DEBUG,
                    format=LOG_FORMAT
                    )


# Check the environment
env = os.environ.get('ENVIRONMENT')
if env == None:
    logging.info('No environment supplied. Hence defaulting to dev')
    env = 'dev'

# Source environment specific settings file
_settingsFile = os.path.join("settings","app.settings." + env + ".json")
util = Utils()
settings=util.getSettings(_settingsFile)
api = BooksAPI(settings)


# Get Books from API
print("#############################################################################")
print("#################### Get Ratings List #######################################")
print("#############################################################################")
logging.info('Starting request to API to get list of ratings')
apiBookRatingsUrl=settings['apiUrl']+'bookrating/'
_bookRatingJson = api.getRequest(apiBookRatingsUrl)
logging.info(_bookRatingJson)
print(_bookRatingJson)
print("\n")


# Get Books from API
print("#############################################################################")
print("#################### Get List of Books ######################################")
print("#############################################################################")
logging.info('Starting request to API to get list of books')
apiBooksUrl=settings['apiUrl']+'books/'
_bookJson = api.getRequest(apiBooksUrl)
logging.info(_bookJson)
print(_bookJson)
print("\n")


# Get Readers from API
print("#############################################################################")
print("#################### Get List of Readers ####################################")
print("#############################################################################")
logging.info('Starting request to API to get list of Readers')
apiReadersUrl=settings['apiUrl']+'reader/'
_readerJson = api.getRequest(apiReadersUrl)
logging.info(_readerJson)
print(_readerJson)
print("\n")

# Get RentedBooks from API
print("#############################################################################")
print("#################### Get List of Rented Books ###############################")
print("#############################################################################")
logging.info('Starting request to API to get list of Rented Books')
apiRentedBooksUrl=settings['apiUrl']+'rentbook/'
_rentedBooksJson = api.getRequest(apiRentedBooksUrl)
logging.info(_rentedBooksJson)
print(_rentedBooksJson)
print("\n")



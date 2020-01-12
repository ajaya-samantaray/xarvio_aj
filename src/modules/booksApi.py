############################################################################################################################
# Auther         :   Ajaya Samantaray
# Description    :   Generic getRequest method to call an API and output a json
#                   Generic postRequest method to call an API and post a json file
# Usage          :
# Date Created   :   12-Jan-2020
# Date Reviewed  :
############################################################################################################################

import json
import requests
import logging

class BooksAPI:
    def __init__(self, settings):
        self.settings = settings

    def getRequest(self, url):

        try:
            response = requests.get(url)

            if response.status_code != 200:
                logging.error('Error retrieving data from API, status : ' + ' Response Code: ' + str(response.status_code))
                return {}
            else:
                return response.json()

        except Exception as e:
            logging.error('Error retrieving data from API, status : ' + str(e))
            return {}

    def postRequest(self, url, jsonData):

        try:
            response = requests.post(url, data=jsonData)
            if response.status_code != 200:
                logging.error('Error retrieving data from API, status : ' + ' Response Code: ' + str(response.status_code))
                return {}
        except Exception as e:
            logging.error('Error retrieving data from API, status : ' + str(e))
            return {}

## This is a very simple application
## The app creates API for a simple Book store with books, its associated readers etc
## The app does some extra validation to check If the ISBN entries are valid and also ensures that the return date of the
## book is always greater than the borrow date.


## First clone the repository to your local host
git clone https://github.com/ajaya-samantaray/xarvio_aj.git

go to the base directory (ie. xarvio_aj) and install all libraries as required in requirements.txt as


pip install -r requirements.txt

## Go to the BookStore root folder where manage.py is stored

Run following commands

python manage.py makemigrations

python manage.py migrate

python manage.py loaddata Books/fixtures/BookStore.json

python manage.py runserver

## Once the app server is running, go to the src directory (xarvio_aj/src) where all modules are stored
Run following command to see the Books and their readers

python start.py

The above script will return the Book Rating, Books, Book Readers and RentBook models
from API thru request modules. The module would also log all the above contents into
a log file located at src/logs directory

## Unit Test for the app
## Run following command in the tests dir while the app is running

cd src/tests
pytest test_BooksProject.py

# Here is a snapshot of the GET AND POST API calls based on the requirement.

PS C:\Users\Ajaya\GitProjects\Test\xarvio_aj\src> python start.py
#############################################################################
#################### Get Ratings List #######################################
#############################################################################

[{'RatingID': 1, 'Desc': 'Poor'}, {'RatingID': 2, 'Desc': 'Average'}, {'RatingID': 3, 'Desc': 'Good'}, {'RatingID': 4, 'Desc': 'Excellent'}, {'RatingID': 5, 'Desc': 'Outstanding'}]


#############################################################################
#################### Get List of Books ######################################
#############################################################################

[{'url': 'http://localhost:8000/books/1/', 'ISBN': '978-300-198-1', 'TitleName': 'My First Book', 'AuthorName': 'Mr. Ram Samantaray', 'Rating': 5}, {'url': 'http://localhost:8000/books/2/', 'ISBN': '978-316-199-1', 'TitleName': 'My Second Book', 'AuthorName': 'Mr. Tom Cruse', 'Rating': 5}, {'url': 'http://localhost:8000/books/3/', 'ISBN': '978-316-199-2', 'TitleName': 'My Third Book', 'AuthorName': 'Ms. Samanta Cruz', 'Rating': 4}]


#############################################################################
#################### Get List of Readers ####################################
#############################################################################

[{'url': 'http://localhost:8000/reader/1/', 'Name': 'Mr. Sunil Lamba', 'Address': 'London', 'RegistrationDate': '2010-01-01', 'IsActive': 'Y', 'ValidFrom': '2010-01-01', 'ValidDate': '2030-12-31'}, {'url': 'http://localhost:8000/reader/2/', 'Name': 'Mr. Sachin Tendulkar', 'Address': 'New Delhi', 'RegistrationDate': '2011-01-01', 'IsActive': 'Y', 'ValidFrom': '2011-01-01', 'ValidDate': '2030-12-31'}, {'url': 'http://localhost:8000/reader/3/', 'Name': 'Mr. MS Dhoni', 'Address': 'Berlin', 'RegistrationDate': '2012-01-01', 'IsActive': 'Y', 'ValidFrom': '2011-01-01', 'ValidDate': '2030-12-31'}]


#############################################################################
#################### Get List of Rented Books ###############################
#############################################################################

[{'url': 'http://localhost:8000/rentbook/1/', 'Book': 1, 'Reader': 1, 'BorrowDate': '2019-01-01', 'ReturnDate': None}, {'url': 'http://localhost:8000/rentbook/2/', 'Book': 2, 'Reader': 2, 'BorrowDate': '2020-01-01', 'ReturnDate': None}, {'url': 'http://localhost:8000/rentbook/3/', 'Book': 3, 'Reader': 3, 'BorrowDate': '2018-01-01', 'ReturnDate': None}]





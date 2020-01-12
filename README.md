## This is a very simple application
## The app creates API for a simple Book store with books, its associated readers etc


## First clone the repository to your local host
git clone https://github.com/ajaya-samantaray/xarvio_aj.git
go to the base directory and install all libraries as required in requirements.txt as

pip install -r requirements.txt

## Go to the BookStore root folder where manage.py is stored

Run following commands

python manage.py makemigrations

python manage.py migrate

python manage.py loaddata Books/fixtures/BookStore.json

python manage.py runserver

## Once the app server is running, go to the src directory where all modules are stored
Run following command to see the Books and their readers

python start.py

The above script will return the Book Rating, Books, Book Readers and RentBook models
from API thru request modules. The module would also log all the above contents into
a log file located at src/logs directory

Finally it would post an update and return the updated RentBook module with updated return date.



## Unit Test for the app
## Run following command in the tests dir while the app is running

cd src/tests
pytest test_BooksProject.py


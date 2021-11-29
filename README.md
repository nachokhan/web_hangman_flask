# web_hangman_flask

## Run Hangman App:

1. Clone the repo.
2. Run the makefile (to create the app secret key)
```
$ cd app
$ ./make
```
4. Then create the environement:
```
python3 -m venv env 
source env/bin/actuvate
```
5. Install requirements
```pip install -r requirements.txt```
6. Finally run the app.
```flask run```

 That's all!

 TIP: make sure you have installed 'pip'

 ## Testing
 ### Run pytest
 1. Install and run pytest (in the root Ç(not inside /tests)
 * pip install pystest
 * pytest

 ### Code Coverage
1. Install and  run coverage
* pip install coverage
* coverage run -m pytest
* coverage report -m


 ## DOCKER Execution
 * sudo docker build -t hangman .
 * sudo docker run --rm -it -p 8080:5052 hangman

 That all!

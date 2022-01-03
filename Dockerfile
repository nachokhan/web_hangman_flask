FROM python:3.8

# Create app directory
WORKDIR /app

# Install app dependencies
COPY requirements.txt ./
COPY app/config_TEMPLATE.py /app
COPY app/make /app
RUN ./make

RUN pip install -r requirements.txt

# Bundle app source
COPY app /app

EXPOSE 5052

CMD [ "env", "FLASK_APP=hangman.py", "python3", "-m" , "flask", "run", "--host=0.0.0.0", "--port=5052"]

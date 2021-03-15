# Flask-API

I have used SQLite and Flask to build the API.

First make sure all the dependencies are installed
    pytest
    flask
    flask_sqlalchemy
    requests
    json



First build the database by running this in the cmd

python audio_file.py


Then run the Flask API by running this in cmd

python flask_api.py


Now the API is running

The routes for the CRUD operations are:
    POST : http://127.0.0.1:1234/add/audio_file_type
    GET :  http://127.0.0.1:1234/audio_file_type, http://127.0.0.1:1234/audio_file_type/id
    UPDATE : http://127.0.0.1:1234/audio_file_type/id
    DELETE : http://127.0.0.1:1234/audio_file_type/id


To test the endpoints run pytest in the file directory after starting the API run this in cmd

pytest

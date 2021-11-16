# After The End Character Sheets Management System

Small project to manage some character sheets and more.

## Running

* Make sure you have Docker up and running
* Edit `afterend/docker.example.py`, adjust options and then save it as `afterend/docker.py`
* Create a volume: `docker volume create afterenddb`
* Build the image in main project directory: `docker build --tag aftertheend:latest .`
* Run the container and link it to volume: `docker run --name aftertheend_test -d -v afterend:/app/db -p 8000:8000 aftertheend:latest`
* Execute this `docker exec -it aftertheend_test /bin/bash` and inside `python manage.py createsuperuser` to create an admin user
* Go to `http://localhost:8000` and enjoy

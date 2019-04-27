# Pinocchio Django server

This is the main backend server for the Pinocchio system. The backend uses Django and has apps, such as transcription, added to the server. This server is meant only for development purposes as more robust features, such as databases or webservers, will be added.

For more information about Django itself, please refer to the example tutorial polls app.

## Prerequisites 

- python3
- run `pip install -r requirements.txt`

## Run standalone

Run `python3 manage.py runserver` to start the Django server. The server is currently running on port `8000`.

## Run with Docker

1. Run `docker build -t django .` This will create a docker image named django
2. Run `docker run -d -p 8000:8000 django` to start the docker image in the background on port 8000. 

You may stop the container with `docker stop <container_id>` or stop and remove the container with `docker rm -f <container_id>`.

## Server details

- Use your web browser to view `/admin/` to view the built in Django admin page.
- Use REST calls against `/transcription/` to interact with the transcription service. **Note:** tailing slash is required for these endpoints.
- pinocchio directory contains the baseline server settings code.
- transcription directory is an application within this environment. 
- `pinocchio/urls.py` contains endpoints the server will accept. App urls are configured in their respective directories.
- main logic to handle app requests are in `views.py`

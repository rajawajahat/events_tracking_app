# Mandrill Events Tracking App
This is the repository containing APP which is built using Django, Redis and containerized via Docker.

## Description:
This App contain API which can be used as callback url for different kind of <b>Mandrill App</b> webhooks.
Whenever a recipient of email perform any trackable action including click, open etc on emails sent via mailchimp, Mandrill App will send a payload on callback url via post request. Then this API will extract the actual data from the body of the request and save it in redis for later usage.
This API also send the name of event to the socket server running in sampe html file (index.html)

## Steps to setup on your machine:
- First install docker and docker-compose on your machine.
- Then run the <b>docker-compose build</b> command to create container(s) and install the prerequisites.
- Then run the <b>docker-compose up</b> command to start the project.

## Endpoints:
There are three endpoints which you can hit.
- Health check endpoint http://localhost:8000/health
- Post event endpoint http://localhost:8000/events_webhook
- Get event endpoint http://localhost:8000/events/{event_id}

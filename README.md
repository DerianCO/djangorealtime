# DJANGO & NODE-JS
django real time through socket.io, using a basic server nodejs

## Versions
Python 3.5.2

  + Django 1.10.2
   + querystring 0.2.0
   
   + socket.io 1.5.0
   
Node v4.0.6

##Project
The project contains the code to create new comments in real time using requests and responses using HTTP methods.

It runs at the time the view django performs submit event.

JavaScript stops sending data Fingered,stores data in a tuple and then issues a new event.

Node hears the event, processes the data and sends them through the POST method to the URL provided by django, django view checks the validity of the data, records and returns data in JSON.

Node issues a new socket with log data, which is heard in the template, which would be responsible for displaying data.

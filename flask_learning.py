# front end static files are being served from web server
# but now you need some data to be fetched from backend, non-static functionality
# http request is sent to backend ( how it is sent ?? java script function call fetch())
# http request is routed to backend application ( how?? web server is configured proxypass )
# using the proxy pass routing in web server, the request reaches app server running on another port
# app server say "gunicorn" receives the request
# request is sent to flask app running on gunicorn(each gunicorn app, only single flask app)

##### flask app #####

# http request byte code is rendered and parsed into python objects by flask
# the data into dictinory
# the method into string
# the url into string
# headers into dict like object
# based on the method and url string , flask creates its own registry of methods to call

# the endpoints are mapped to functions inside the app  ( how ?? preprocessing ... when the code is set to executed and the service is made running, the decorates does preprocessing and registry is created)

# the function is called, executes the logic and returned to flask application in json format
# flask wraps it in http response and sends it to gunicorn --> nginx ---> browser --> rendered and shown

#rendering ==> parsing based on content type
# Request Client
Request Client creates and maintains connections using 
the request library, but make each url endpoint a remote
procedure call with the response content returned.  These 
function calls can made from a "connection" which has
a hierarchy of objects that mirrors the hierarchy of the API.

# Modules
## api_call
Api Call is a class which will be instantiated for a single rest call.
This is nothing more than a wrapper around request, but with helping methods.

## connection_basic
Connection Basic is a connection to a specific url and will maintain auth, 
cookies, and keep the api calls as a list within itself.

## connection_endpoint
Connection Endpoint subclasses connection_basic with the ability to add
endpoints, which can be referenced as memember variables.
> Example
    conn.user.post('user','pwd')

## endpoint
Endpoint is a class that will define the rest: get, post, put, delete methods
with arguments to be sent as data or parameters, as well as sub-branches.  
See request_client/example folder for an examples

## errors
Errors creates an Exception class for each of the http error codes

## intellisense
Intellisense cleans up the itellisense in Pycharm to only show the relevant
member variables in connection_endpoints

## repr_wrapper
Will wrap the resulting list, tuple, string, int, ... such that hey will 
display nicely in IDLE or ipython

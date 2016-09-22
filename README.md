# Asyncio minimal example

This is a minimal example for a client server combination that interacts asynchronously.

## Server

Server uses ether a Flask server, which runs synchronously and hence response
requests in a row. Or the async_server uses Klein, which is a minimal
asynchronous web server.

## Client

The client uses `Asyncio` Corountines to query the server. 

#!/usr/bin/env python3

"""
This module uses threads to start a python server allowing requests
to vector and opens up a web browser
"""

import os
from threading import Thread
from webbrowser import open_new
from http.server import SimpleHTTPRequestHandler, HTTPServer
from Vector.vector import Vector


class VectorHTTPServer(HTTPServer):
    """
    A subclass of HTTPServer to allow access to the vector
    instance in the HandlerClass
    """
    def __init__(self, vector: Vector, *args, **kwargs):

        #Can store an instance of Vector Wrapper here
        self.vector = vector

        super().__init__(*args, **kwargs)


class HandlerClass(SimpleHTTPRequestHandler):            
    """
    A subclass of SimpleHTTPRequestHandler this allows the GET method
    to serve the Blockly index.html page and implements a POST method
    to pass requesto to vector
    """
    def _set_response(self):
        self.send_response(200)
        self.send_header('Access-Control-Allow-Origin', '*')
        self.end_headers()
    
    
    def do_POST(self):
        self._set_response()

        #Can access instance of Vector Wrapper here
        vector = self.server.vector
        byte_size = int(self.headers['Content-Length'])

        with self.rfile as f:
            code = f.read(byte_size).decode()

        try:
            print(code)
            exec(code)
        except:
            print('There was a problem')


def run(vector_instance: Vector, server_class=VectorHTTPServer, handler_class=HandlerClass):

    server_address=('127.0.0.1', 8000)
    httpd=server_class(vector_instance, server_address, handler_class)
    httpd.serve_forever()


if __name__ == "__main__":
   
    
    print('Starting server...')
    try:
        vector = Vector()
        start_server_thread = Thread(target=run, args=[vector])
        open_browser_thread = Thread(target=open_new, args=['http://127.0.0.1:8000'])
        start_server_thread.start()
        open_browser_thread.start()
        print('\nPress ctrl + c twice to exit')
        start_server_thread.join()

        #run(vector)
    except KeyboardInterrupt:
        pass
        
    print('\nDisconnecting...')
    vector.disconnect()
    
    print('\nBye bye')

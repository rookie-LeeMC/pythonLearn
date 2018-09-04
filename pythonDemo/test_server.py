# -*- coding:utf-8 -*-

import socket
import time, os
import threading
import socketserver
import json, types, string


class ThreadedTCPRequestHandler(socketserver.BaseRequestHandler):
    def handle(self):
        print("################")
        data = self.request.recv(1024).decode()
        jdata = json.loads(data)

        print("Receive data from {0}".format(data))
        print("Receive jdata from {0}".format(jdata))

        rec_src = jdata[0]['src']
        rec_dst = jdata[0]['dst']

        cur_thread = threading.current_thread()
        response = [{'thread': cur_thread.name, 'src': rec_src, 'dst': rec_dst}]

        jresp = json.dumps(response)
        self.request.sendall(jresp.encode())

        rec_cmd = "proccess " + rec_src + " -o " + rec_dst
        print("CMD {0}".format(rec_cmd))
        os.system(rec_cmd)


class ThreadedTCPServer(socketserver.ThreadingMixIn, socketserver.TCPServer):
    pass


if __name__ == "__main__":
    HOST, PORT = "localhost", 50001
    socketserver.TCPServer.allow_reuse_address = True
    server = ThreadedTCPServer((HOST, PORT), ThreadedTCPRequestHandler)

    ip, port = server.server_address

    # Start a thread with the server -- that thread will then start one
    # more thread for each request
    server_thread = threading.Thread(target=server.serve_forever)

    # Exit the server thread when the main thread terminates
    server_thread.daemon = True
    server_thread.start()
    print("Server loop running in thread:", server_thread.name)
    print(" .... waiting for connection")

    # Activate the server; this will keep running until you
    # interrupt the program with Ctrl-C
    server.serve_forever()

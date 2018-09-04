# -*- coding:utf-8 -*-

import socket
import threading
import json
import socketserver


def client(ip, port, message):
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.connect((ip, port))

    try:
        print('send: {0}'.format(message))
        sock.sendall(message.encode())
        response = sock.recv(1024).decode()
        print("response: ", response)
        jresp = json.loads(response)
        print('Recv: ', jresp)

    finally:
        sock.close()


if __name__ == "__main__":
    HOST, PORT = "localhost", 50001
    msg1 = [{'src': "zj", 'dst': "zjdst"}]
    msg2 = [{'src': "ln", 'dst': "lndst"}]
    msg3 = [{'src': "xj", 'dst': "xjdst"}]

    jmsg1 = json.dumps(msg1)
    jmsg2 = json.dumps(msg2)
    jmsg3 = json.dumps(msg3)

    client(HOST, PORT, jmsg1)
    client(HOST, PORT, jmsg2)
    client(HOST, PORT, jmsg3)

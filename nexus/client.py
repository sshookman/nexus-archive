import socket
from threading import Thread

class Client(Thread):

    def __init__(self, socket, address):
        Thread.__init__(self)

        self.socket = socket
        self.address = address

    def run(self):
        #TODO: Wrap the sending of messages in another Class that can handle formatting, etc.
        self.socket.send(b"Welcome to the Nexus Archives\n")
        self.socket.send(b"\n[NA] >> ")

        inp = self.socket.recv(1024)
        self.socket.send(inp);

        self.socket.close()

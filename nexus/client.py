import socket
from threading import Thread

WELCOME = "Welcome to the Nexus Archive\n"
NA_OPTIONS = """
  [R]egister
  [L]ogin
  [A]bout
  [H]elp
  [Q]uit
"""
PROMPT = "\n[{}] >> "

class Client(Thread):


    def __init__(self, socket, address):
        Thread.__init__(self)

        self.socket = socket
        self.address = address

    def run(self):
        #TODO: Wrap the sending of messages in another Class that can handle formatting, etc.
        self.socket.send(WELCOME.encode())
        self.socket.send(NA_OPTIONS.encode())
        self.socket.send(PROMPT.format("NA").encode())

        inp = self.socket.recv(1024)
        self.socket.send(inp);

        self.socket.close()

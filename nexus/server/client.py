import socket
from threading import Thread

WELCOME = "Welcome to The Dragonfly Experiments\n"
NA_OPTIONS = """
  [S]tart
  [A]bout
  [E]xit
"""
PROMPT = "\n[{}] >> "

class Client(Thread):

    def __init__(self, socket, address):
        Thread.__init__(self)

        self.socket = socket
        self.address = address

    def run(self):
        self.socket.send(WELCOME.encode())
        self.socket.send(NA_OPTIONS.encode())
        self.socket.send(PROMPT.format("NA").encode())

        inp = self.socket.recv(1024)
        self.socket.send(inp);

        self.socket.close()

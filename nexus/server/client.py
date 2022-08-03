import socket
from threading import Thread
from ..ui.nexusArchive import NexusArchive

class Client(Thread):

    socket = None
    nexusArchive = None

    def __init__(self, socket, address):
        Thread.__init__(self)
        self.socket = socket
        self.nexusArchive = NexusArchive(socket, address)

    def run(self):
        self.nexusArchive.start()
        self.socket.close()

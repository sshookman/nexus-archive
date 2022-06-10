import socket
from threading import Thread
from ..config import ARCHIVE_DB
from ..ui.nexusArchive import NexusArchive

class Client(Thread):

    nexusArchive = None

    def __init__(self, socket, address):
        Thread.__init__(self)
        self.nexusArchive = NexusArchive(socket, address, ARCHIVE_DB)

    def run(self):
        self.nexusArchive.start()

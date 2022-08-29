import socket
import threading
from .client import Client
from ..util.logging import NexusLogger

LOGGER = NexusLogger(__name__)

class Server():
    """
    Telnet Server

    This server hosts the Nexus Archive and provides an interface for finding
    Gates and accessing them through telnet.
    """

    tn_socket = None
    clients = None

    def __init__(self, port, backlog=10):

        LOGGER.info("Initiating The Nexus Archive...")
        self.tn_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.tn_socket.bind(("", port))
        self.tn_socket.listen(backlog)

        lock = threading.Lock()
        self.clients = []
        LOGGER.info("The Nexus Archive is Online")

    def start(self):

        LOGGER.info("Awaiting Connections")
        while True:
            socket, address = self.tn_socket.accept()
            client = Client(socket, address).start()
            self.clients.append(client)
            LOGGER.info(f"Connection Established to Socket {address}!")

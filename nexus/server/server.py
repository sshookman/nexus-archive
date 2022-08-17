import socket
import threading
from .client import Client

class Server():
    """
    Telnet Server

    This server hosts the Nexus Archive and provides an interface for finding
    Gates and accessing them through telnet.
    """

    tn_socket = None
    clients = None

    def __init__(self, port, backlog=10):

        print("Initiating The Nexus Archive...")
        self.tn_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.tn_socket.bind(("", port))
        self.tn_socket.listen(backlog)

        lock = threading.Lock()
        self.clients = []
        # TODO: Need to create proper logging system
        print("The Nexus Archive is Online")

    def start(self):
        print("Awaiting Connections")
        while True:

            socket, address = self.tn_socket.accept()
            client = Client(socket, address).start()
            self.clients.append(client)

            print(f"Connection Established to Socket {address}!")

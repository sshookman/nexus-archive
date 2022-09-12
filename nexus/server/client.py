import socket
from threading import Thread
from ..ui.nexusArchive import NexusArchive

class Client(Thread):
    """
    Telnet Client

    This is the client class that is created by connections to
    the Server and handles a single user session.
    """

    socket = None
    nexusArchive = None

    def __init__(self, socket, address):
        """
        Initialize the Client connection with the Server socket
        and the user address.

        Parameters
        ----------
        socket : str?
            The socket on which this client will connect to the
            server
        address : str?
            The connecting user's IP address
        """

        Thread.__init__(self)
        self.socket = socket
        self.nexusArchive = NexusArchive(socket, address)

    def run(self):
        """
        This method is called immediately after the Client is
        created and the the connection is established.

        This method will start the NexusArchive service loop and
        terminate the socket connection after it completes.
        """

        self.nexusArchive.start()
        #TODO: Handle closing the socket on errors?
        self.socket.close()


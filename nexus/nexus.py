from .server.server import Server

def main():
    """
    Starts the Telnet Server on Port 1127

    The server awaits connections and instantiates Clients once they are established.
    """

    server = Server(1127)
    server.start()

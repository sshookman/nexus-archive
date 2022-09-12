"""Nexus Archive - A Telnet-Based Archive of Gates to the Multiverse"""
from .server.server import Server

def main():
    """
    Nexus Archive

    Starts the Telnet Server for the Nexus Archive on Port 1127
    """

    server = Server(1127)
    server.start()

import re
from enum import Enum
from ..dba.databaseManager import DatabaseManager
from .messageSystem import MessageSystem

# TODO: Need to setup a create user/login screen

class NexusArchive:

    address = None
    messageSystem = None
    databaseManager = None

    def __init__(self, socket, address, databaseFile):
        self.address = address
        self.messageSystem = MessageSystem(socket)
        self.databaseManager = DatabaseManager(databaseFile)

    def start(self):
        try:
            page = self.databaseManager.getLocation()

            self.messageSystem.clear()
            self.messageSystem.send(page)
            command = self.messageSystem.recieve()

            status = self.databaseManager.execute(command)

            if (status == 0):
                self.execute()

        except:
            print(f"Voyager {self.address} Encountered an Error.")
            self.messageSystem.send("Something Went Wrong!\n")

        finally:
            print(f"Voyager {self.address} Returned Home. Closing Connection")
            self.messageSystem.send("Carry On, Inrepid Voyager!\n")
            self.messageSystem.close_socket()
